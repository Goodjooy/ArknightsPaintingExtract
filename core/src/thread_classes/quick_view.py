import threading

import wx

from core.src.frame_classes.design_frame import MainFrame
from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.painting_work_structs.extract_structs import PerInfo


class QuickRestore(threading.Thread):

    def __init__(self, info: PerInfo, father: MainFrame = None, work_path='', full=None,
                 back=2):
        threading.Thread.__init__(self)

        self.info = info
        self.father = father

        self.path = work_path
        self.full = full

        self.back = back

    def run(self):
        try:
            size = tuple(self.father.m_panel9.GetSize())
            if self.info.is_able_work:
                pic, pic_size = ImageWork.p_restore_tool_no_save(self.info.mesh_path, self.info.tex_path, size)
                info_str = f"可还原立绘预览：{self.info.cn_name}；尺寸：{pic_size}"
            elif self.info.lay_in != '':
                pic, pic_size = ImageWork.g_load_and_transform(self.info.lay_in, size)
                info_str = f"导出目标同名文件预览：{self.info.cn_name}；尺寸：{pic_size}"
            else:
                pic, pic_size = ImageWork.g_load_and_transform(self.info.tex_path, size)
                info_str = f"原始文件预览：{self.info.cn_name}；尺寸：{pic_size}"

            self.father.m_staticText_info.SetLabel(info_str)
            self.father.m_bitmap_show.ClearBackground()

            self.father.view_img(pic, False)

        except RuntimeError as info:
            # self.father.append_error(info)
            print(info)
            raise
        except AssertionError as info:
            self.father.m_staticText_info.SetLabel(f"fail to view {self.info.cn_name},size not match!{info}")

    #     if self.father.any_error():
    #         self.father.m_notebook_info.SetSelection(2)
