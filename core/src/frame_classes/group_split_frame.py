import re

import wx
from PIL import Image

from core.src.frame_classes.design_frame import MyDialogSplit
from core.src.static_classes.image_deal import ImageWork
from core.src.structs_classes.painting_work_structs.group_split import ImageList


class DefineSplit(MyDialogSplit):
    def __init__(self, parent, work_group: ImageList, name):
        super(DefineSplit, self).__init__(parent)

        self.work_group = work_group.build_able()
        self.frame = parent

        self.image: Image.Image = ...

        self.view_index = 0

        self.use_item = None

        self.spilter = {}
        self.is_save = False

        self.width = 0
        self.height = 0
        self.inside = 0

        self.name = name

        self._pos_x = 1
        self._pos_y = 1

        self.view_region_list = []

    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        if value < 1:
            return
        if value * self.width >= self.image.width:
            return
        else:
            self._pos_x = value

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        if value < 1:
            return
        if value * self.height >= self.image.height:
            return
        else:
            self._pos_y = value

    def show_img(self):
        init_img, size = ImageWork.g_load_and_transform(self.use_item.tex_path,
                                                        self.m_bitmap_view.GetSize())
        ImageWork.g_show_in_screen(init_img, self.m_bitmap_view)

    def view_region(self):
        img = ImageWork.array_split_quick_view_single(Image.open(self.use_item.tex_path), self.pos_x, self.pos_y,
                                                      self.width, self.height, self.inside, self.m_bitmap_view.Size)
        ImageWork.g_show_in_screen(img, self.m_bitmap_view)

    def initial(self, event):
        value = self.work_group.build_view()
        self.m_listBox_img_list.Set(value)

        self.use_item = self.work_group[self.view_index]
        self.image = Image.open(self.use_item.tex_path)

        self.show_img()

    def use_image(self, event):
        index = event.GetSelection()

        self.use_item = self.work_group[index]
        self.view_index = index
        self.image = Image.open(self.use_item.tex_path)

        self.show_img()

    def show_init_img(self, event):
        self.show_img()

    def save_setting(self, event):
        self.spilter["value"] = {
            "size_w": self.width,
            "size_h": self.height,
            "inside": self.inside
        }
        self.spilter["name"] = self.name

        self.is_save = True

        self.Destroy()

    def cancel_setting(self, event):
        self.Destroy()

    def use_setting(self, event):
        self.spilter["value"] = {
            "size_w": self.width,
            "size_h": self.height,
            "inside": self.inside
        }
        self.spilter["name"] = self.name

        self.is_save = True

    def cut_img(self, event):
        if self.width * self.height == 0:
            wx.MessageBox("切割尺寸为0！", "错误", wx.OK | wx.ICON_WARNING)
        else:
            self.view_region()

            group = ImageWork.array_split_view_builder({
                "size_w": self.width,
                "size_h": self.height,
                "inside": self.inside
            })
            is_ok, items = group(self.use_item, self.m_bitmap_view.GetSize())

            if is_ok:
                self.view_region_list = items

                view_list = [f"切割块：{x + 1}" for x in range(len(self.view_region_list))]

                self.m_listBox_spilt_groups.Clear()
                self.m_listBox_spilt_groups.Set(view_list)

    def view_down(self, event):
        self.pos_y -= 1
        self.view_region()

    def view_up(self, event):
        self.pos_y += 1
        self.view_region()

    def view_left(self, event):
        self.pos_x -= 1
        self.view_region()

    def view_right(self, event):
        self.pos_x += 1
        self.view_region()

    def view_img(self, event):
        index = event.GetSelection()
        value, size = ImageWork.g_load_and_transform(self.work_group[index].tex_path, self.m_bitmap_view.GetSize())
        ImageWork.g_show_in_screen(value, self.m_bitmap_view)

    def width_enter(self, event):
        value = event.GetString()
        if re.match(r'^\d+$', value):
            self.width = int(value)
        else:
            self.m_textCtrl_split_wide.SetLabel(str(self.width))

    def height_enter(self, event):
        value = event.GetString()
        if re.match(r'^\d+$', value):
            self.height = int(value)
        else:
            self.m_textCtrl_split_high.SetLabel(str(self.height))

    def inside_enter(self, event):
        value = event.GetString()
        if re.match(r'^\d+$', value):
            self.inside = int(value)
        else:
            self.m_textCtrl_inside_size.SetLabel(str(self.inside))

    def width_wheel(self, event):
        value = event.GetWheelRotation()
        step = value // abs(value)

        self.m_textCtrl_split_wide.SetLabel(str(self.width + step))

    def height_wheel(self, event):
        value = event.GetWheelRotation()
        step = value // abs(value)

        self.m_textCtrl_split_high.SetLabel(str(self.height + step))

    def inside_wheel(self, event):
        value = event.GetWheelRotation()
        step = value // abs(value)

        self.m_textCtrl_inside_size.SetLabel(str(self.inside + step))

    def view_per_region(self, event):
        index = event.GetSelection()

        ImageWork.g_show_in_screen(self.view_region_list[index], self.m_bitmap_view)
