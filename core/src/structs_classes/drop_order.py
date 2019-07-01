import os
import re
from collections import Callable

import wx

import core.src.structs_classes.painting_work_structs.extract_structs as es
from core.src.frame_classes.design_frame import MainFrame, MyDialogHandleSplit
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.painting_work_structs.atlas_structs import AtlasList
from core.src.structs_classes.painting_work_structs.basic_class import BasicInfoList
from core.src.structs_classes.painting_work_structs.handle_split import HandleSplitHolder


class BasicDragOrder(wx.FileDropTarget):
    def __init__(self, parent: BasicInfoList, view_work: BasicInfoList, work_on_tree, work_on_root, info_set, setting,
                 g_names, group_setter: Callable):
        super(BasicDragOrder, self).__init__()

        self.group_setter = group_setter
        self.setting = setting
        self.work_on_root = work_on_root
        self.work_on_tree = work_on_tree
        self.view_work = view_work
        self.parent = parent
        self.g_names = g_names

        self.data = GlobalData()

        self.is_given = False

        self.info_set = info_set

        self.paths = None

    @property
    def value_group(self):
        if not self.is_given:
            self.is_given = True
            return self.parent

    def file_filter(self, file_names):
        dir_name = (filter(lambda val: not os.path.isfile(val), file_names))
        dir_name = map(lambda val: FileFilter.all_file(val), dir_name)
        list(map(lambda val: file_names.extend(val), dir_name))

        file_names = (filter(lambda val: os.path.isfile(val), file_names))

        self.paths = list(filter(lambda val: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(val)) is None,
                                 file_names))

        return self.paths

    def file_deal_work(self, file_names):
        return True

    def finish_work(self):
        if isinstance(self.group_setter, Callable):
            self.group_setter(self.parent)

    def OnDropFiles(self, x=0, y=0, filenames=None):
        self.is_given = False
        value = self.file_deal_work(filenames)

        self.finish_work()
        return value


class DragOrderPainting(BasicDragOrder):
    def __init__(self, parent: es.PerWorkList, view_work: es.PerWorkList, frame: MainFrame, work_on_tree, work_on_root,
                 setting, g_names, gorup_setter: Callable, class_type=es.PerWorkList, update_type: Callable = None):
        super(DragOrderPainting, self).__init__(parent, view_work, work_on_tree, work_on_root, frame.m_staticText_info,
                                                setting, g_names, gorup_setter)
        self.update_type = update_type
        self.class_type = class_type
        self.frame = frame
        self.parent = self.class_type(self.parent)

    def file_deal_work(self, file_names):
        try:

            paths = self.file_filter(file_names)

            returned_tex, tex_info = FileFilter.file_deal(paths, self.parent, False,
                                                          self.setting[self.data.sk_input_filter_tex],
                                                          True, '', self.g_names, self.data.fi_texture_type)

            returned_mesh, mesh_info = FileFilter.file_deal(paths, self.parent, False,
                                                            self.setting[self.data.sk_input_filter_mesh],
                                                            True, "[alpha]", self.g_names, self.data.fi_mesh_type,
                                                            "_alpha")
            if returned_tex:
                self.frame.m_gauge_state.SetValue(50)
            if returned_mesh:
                self.frame.m_gauge_state.SetValue(100)

            self.view_work = self.class_type(self.parent)

            self.work_on_tree.DeleteChildren(self.work_on_root)
            self.parent.show_in_tree(self.work_on_tree, self.work_on_root)

        except RuntimeError:
            return False

        else:

            return True

    def finish_work(self):
        if isinstance(self.update_type, Callable):
            self.update_type()

        super(DragOrderPainting, self).finish_work()


class DragOrderAtlas(BasicDragOrder):
    def __init__(self, parent: AtlasList, view_work: AtlasList, frame: MainFrame, work_on_tree, work_on_root,
                 setting, g_names, group_setter: Callable):
        super(DragOrderAtlas, self).__init__(parent, view_work, work_on_tree, work_on_root, frame.m_staticText_info,
                                             setting, g_names, group_setter)
        self.frame = frame

        self.parent = AtlasList(self.parent)

    def file_deal_work(self, file_names):

        try:
            file_names = list(file_names)
            self.info_set.SetLabel(f"开始导入{len(file_names)}个文件")

            paths = self.file_filter(file_names)

            atlas_return, info = FileFilter.file_deal(paths, self.parent, False,
                                                      r"^.+\.(?:atlas|atlas\.txt)$", type_set=self.data.fi_atlas_type
                                                      , names=self.g_names, replace_str=".atlas")
            if atlas_return:
                self.frame.m_gauge_state.SetValue(100)

            self.view_work = AtlasList(self.parent)

            self.parent = self.parent
            self.frame.m_a_treeCtrl_atlas.DeleteChildren(self.work_on_root)
            self.parent.show_in_tree(self.work_on_tree, self.work_on_root)

        except RuntimeError:
            return False
        else:
            return True


class DragOrderHandleSplit(wx.FileDropTarget):
    def __init__(self, parent: MyDialogHandleSplit, value: HandleSplitHolder):
        super(DragOrderHandleSplit, self).__init__()
        self.value = value
        self.parent = parent

    def OnDropFiles(self, x, y, filenames):
        try:
            files = filter(lambda x_s: os.path.isfile(x_s), filenames)

            file = list(files)[0]
            self.value.val = file

            self.value.load_img()

            pic, size = ImageWork.g_transform_image(self.value.img, self.parent.m_bitmap_view_img.GetSize())

            temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
            self.parent.m_bitmap_view_img.SetBitmap(temp)

            self.parent.m_staticText_info.SetLabel(f"完成导入图片 {file};\t尺寸：{size}")

            return True
        except Exception as info:
            print(info)
            return False
