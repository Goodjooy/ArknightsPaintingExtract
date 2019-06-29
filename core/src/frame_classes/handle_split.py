import os
import re
from threading import Thread

import wx
from PIL import Image

from core.src.frame_classes.design_frame import MyDialogHandleSplit
from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.drop_order import DragOrderHandleSplit
from core.src.structs_classes.painting_work_structs.handle_split import HandleSplitHolder


class HandleSplit(MyDialogHandleSplit):
    def __init__(self, parent):
        super(HandleSplit, self).__init__(parent)

        self.value = HandleSplitHolder()

        drop = DragOrderHandleSplit(self, self.value)
        self.SetDropTarget(drop)

        self._step = 1

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

        self.step = 1

        self.enter = True

        self.m_textCtrl_wieth.SetLabel(self.w.__str__())
        self.m_textCtrl_height.SetLabel(self.h.__str__())
        self.m_textCtrl_left.SetLabel(self.x.__str__())
        self.m_textCtrl_botton.SetLabel(self.y.__str__())

        self.m_comboBox_step.SetLabel(self.step.__str__())

        self.size = None

        self.enter = False

        self.region_list = []
        self.select = -1

    def is_able(self, x, y, w, h):
        if self.value.img is ...:
            return False
        self.size = self.value.img.size

        if x + w > self.size[0] or y + h > self.size[1]:
            return False
        return True

    def quick_transform(self, img):
        size = self.m_bitmap_region.GetSize()
        pic, size = ImageWork.g_transform_image(img, size, False, bg_color=(0, 155, 155, 255))

        ImageWork.g_show_in_screen(pic, self.m_bitmap_region)

    def quick_view(self):
        if self.w * self.h == 0:
            return
        img = self.value.quick_split(self.x, self.y, self.h, self.w)
        self.quick_transform(img)

    def select_region(self, event, index_give=0):
        if event is not None:
            index = event.GetSelection()
        else:
            index = index_give
        name = self.region_list[index]
        val = self.value.split_group[name]
        img = self.value.quick_split(**val)

        self.quick_transform(img)

        self.m_textCtrl_botton.SetLabel(val["y"].__str__())
        self.m_textCtrl_left.SetLabel(val["x"].__str__())
        self.m_textCtrl_wieth.SetLabel(val["w"].__str__())
        self.m_textCtrl_height.SetLabel(val["h"].__str__())

        self.select = index

    def enter_x(self, event):
        if self.enter:
            return
        val = event.GetString()
        tip = re.match(r"^\d*$", val)
        if tip is not None and self.is_able(int(val), self.y, self.w, self.h):
            self.x = int(val)
            self.quick_view()
        else:
            self.m_textCtrl_left.SetLabel(self.x.__str__())

    def enter_height(self, event):
        if self.enter:
            return
        val = event.GetString()
        tip = re.match(r"^\d*$", val)
        if tip is not None and self.is_able(self.x, self.y, self.w, int(val)):
            self.h = int(val)
            self.quick_view()
        else:
            self.m_textCtrl_height.SetLabel(self.h.__str__())

    def enter_y(self, event):
        if self.enter:
            return
        val = event.GetString()
        tip = re.match(r"^\d*$", val)
        if tip is not None and self.is_able(self.x, int(val), self.w, self.h):
            self.y = int(val)
            self.quick_view()
        else:
            self.m_textCtrl_botton.SetLabel(self.y.__str__())

    def enter_width(self, event):
        if self.enter:
            return
        val = event.GetString()
        tip = re.match(r"^\d*$", val)
        if tip is not None and self.is_able(self.x, self.y, int(val), self.h):
            self.w = int(val)
            self.quick_view()
        else:
            self.m_textCtrl_wieth.SetLabel(self.w.__str__())

    def wheel_y(self, event):
        val = event.GetWheelRotation()
        if val >= 0:
            key = -1
        else:
            key = 1
        self.m_textCtrl_botton.SetLabel(f"{self.y + self.step * key}")

    def wheel_h(self, event):
        val = event.GetWheelRotation()
        if val >= 0:
            key = -1
        else:
            key = 1
        self.m_textCtrl_height.SetLabel(f"{self.h + self.step * key}")

    def wheel_x(self, event):
        val = event.GetWheelRotation()
        if val >= 0:
            key = -1
        else:
            key = 1
        self.m_textCtrl_left.SetLabel(f"{self.x + self.step * key}")

    def wheel_w(self, event):
        val = event.GetWheelRotation()
        if val >= 0:
            key = -1
        else:
            key = 1
        self.m_textCtrl_wieth.SetLabel(f"{self.w + self.step * key}")

    def wheel_region(self, event):
        val = event.GetWheelRotation()
        if val > 0:
            index = 1
        else:
            index = -1
        index += self.select

        if 0 <= index < len(self.region_list):
            self.select_region(None, index)

    def step_len(self, event):
        if self.enter:
            return
        val = event.GetString()
        tip = re.match(r"^\d*$", val)
        if tip is not None:
            self.step = int(val)
        else:
            self.m_comboBox_step.SetLabel(self.step.__str__())
        pass

    def step_wheel(self, event):
        val = event.GetWheelRotation()
        if val >= 0:
            key = -1
        else:
            key = 1
        if self.step + key <= 0:
            return
        self.m_comboBox_step.SetLabel(f"{self.step + key}")
        self.step += key

    def save(self, event):
        dialog = wx.DirDialog(self, "保存")

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()

            path = os.path.join(path, "out")

            os.makedirs(path, exist_ok=True)

            def work():
                num = 0
                for name in self.region_list:
                    val = self.value.split_group[name]
                    img = self.value.quick_split(**val)

                    img.save(os.path.join(path, name + ".png"))
                    num += 1
                    work_val = round((num / self.region_list.__len__()) * 100)
                    self.m_gauge_val.SetValue(work_val)

                    self.m_staticText_info.SetLabel(f"完成导出：{name}")

            th = Thread(target=work)
            th.start()

    def add_region(self, event):
        if self.is_able(self.x, self.y, self.w, self.h):
            dialog = wx.TextEntryDialog(self, u"设置名称", u"设置名称")
            if dialog.ShowModal() == wx.ID_OK:
                val = dialog.GetValue()
                if val in self.region_list:
                    return
                self.value.add_split_group(self.w, self.h, self.x, self.y, val)

                self.region_list.append(val)
                self.m_listBox4.Append(val)

                self.m_staticText_info.SetLabel(f"添加子模块：{val}")

    def del_region(self, event):
        val = self.region_list.pop(self.select)
        self.value.split_group.pop(val)

        self.m_listBox4.Clear()
        self.m_listBox4.Set(self.region_list)

        self.m_staticText_info.SetLabel(f"移除子模块：{val}")


if __name__ == '__main__':
    app = wx.App()
    frame = HandleSplit(None)

    frame.Show()

    app.MainLoop()
