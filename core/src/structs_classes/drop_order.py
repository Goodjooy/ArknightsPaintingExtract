import os
import re

import wx

import core.src.structs_classes.extract_structs as es
from core.src.frame_classes.design_frame import MainFrame
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.atlas_structs import AtlasList


class DragOrderPainting(wx.FileDropTarget):
    def __init__(self, parent: es.PerWorkList, view_work: es.PerWorkList, frame: MainFrame,work_on_tree,work_on_root):
        super(DragOrderPainting, self).__init__()
        self.work_on_root = work_on_root
        self.work_on_tree = work_on_tree
        self.view_work = view_work
        self.frame = frame

        self.parent = parent
        self.data = GlobalData()

    def OnDropFiles(self, x, y, filenames):
        file_names = filenames
        try:
            file_names = list(file_names)
            self.frame.m_staticText_info.SetLabel(f"开始导入{len(filenames)}个文件")

            dir_name = (filter(lambda x: not os.path.isfile(x), file_names))
            dir_name = map(lambda x: FileFilter.all_file(x), dir_name)
            list(map(lambda x: file_names.extend(x), dir_name))

            file_names = (filter(lambda x: os.path.isfile(x), file_names))

            paths = list(filter(lambda x: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(x)) is None, file_names))

            returned_tex, tex_info = FileFilter.file_deal(paths, self.parent, False,
                                                          self.frame.g_setting_info[self.data.sk_input_filter_tex],
                                                          True, '', self.frame.g_names, self.data.fi_texture_type)

            returned_mesh, mesh_info = FileFilter.file_deal(paths, self.parent, False,
                                                            self.frame.g_setting_info[self.data.sk_input_filter_mesh],
                                                            True, "[alpha]", self.frame.g_names, self.data.fi_mesh_type,
                                                            "_alpha")
            if returned_tex:
                self.frame.m_gauge_state.SetValue(50)
            if returned_mesh:
                self.frame.m_gauge_state.SetValue(100)

            self.view_work = es.PerWorkList(self.parent)

            self.work_on_tree.DeleteChildren(self.work_on_root)
            self.parent.show_in_tree(self.work_on_tree, self.work_on_root)

        except RuntimeError:
            return False

        else:

            return True


class DragOrderAtlas(wx.FileDropTarget):
    def __init__(self, parent: AtlasList, view_work: AtlasList, frame: MainFrame):
        super(DragOrderAtlas, self).__init__()
        self.view_work = view_work
        self.frame = frame

        self.parent = parent
        self.data = GlobalData()

    def OnDropFiles(self, x, y, filenames):
        file_names = filenames
        try:
            file_names = list(file_names)
            self.frame.m_staticText_info.SetLabel(f"开始导入{len(filenames)}个文件")

            dir_name = (filter(lambda x: not os.path.isfile(x), file_names))
            dir_name = map(lambda x: FileFilter.all_file(x), dir_name)
            list(map(lambda x: file_names.extend(x), dir_name))

            file_names = (filter(lambda x: os.path.isfile(x), file_names))

            paths = list(filter(lambda x: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(x)) is None, file_names))

            atlas_return, info = FileFilter.file_deal(paths, self.parent, False,
                                                      r"^.+\.(?:atlas|atlas\.txt)$", type_set=self.data.fi_atlas_type
                                                      , names=self.frame.g_names, replace_str=".atlas")
            if atlas_return:
                self.frame.m_gauge_state.SetValue(100)

            self.view_work = es.PerWorkList(self.parent)

            self.frame.m_a_treeCtrl_atlas.DeleteChildren(self.frame.a_root)
            self.parent.show_in_tree(self.frame.m_a_treeCtrl_atlas, self.frame.a_root)

        except RuntimeError:
            return False

        else:

            return True
