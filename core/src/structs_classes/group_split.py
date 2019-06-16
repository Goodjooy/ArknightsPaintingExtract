import os

import wx
from PIL import Image

from core.src.structs_classes.extract_structs import PerInfo, PerWorkList


class PerImage(PerInfo):
    def __init__(self, name, val, has_cn):
        super(PerImage, self).__init__(name, val, has_cn)
        self.region_id = None
        self.image_data: Image.Image = ...

    @property
    def save_path(self):
        return self._save_path

    @save_path.setter
    def save_path(self, value):
        if self._is_save_as_cn:
            self._save_path = os.path.join(value, self.cn_name)
        else:

            self._save_path = os.path.join(value, self.name)

    def is_able(self):
        if os.path.isfile(self.tex_path):
            return True
        else:
            return False

    def is_need_work(self):
        return super(PerImage, self).is_able()

    def append_to_tree(self, tree: wx.TreeCtrl, tree_root: wx.TreeItemId):
        super(PerImage, self).append_to_tree(tree, tree_root)

        self.region_id = tree.AppendItem(self.tree_ID, "预览切割")

    def is_inside_id(self, id):
        if id == self.region_id:
            return True
        else:
            return super(PerImage, self).is_inside_id(id)

    def find_sub_key(self, id):
        if id == self.region_id:
            return True, True, self.data.td_region_type, 0, self
        else:
            return super(PerImage, self).find_sub_key(id)

    def open_image(self):
        if self.is_able():
            self.image_data = Image.open(self.tex_path)

    def release_img(self):
        if self.image_data is Image.Image:
            self.image_data.__del__()


class ImageList(PerWorkList):
    def append_name(self, name, val: dict, *, has_cn=False):
        if name not in self._key_list:

            if name not in val.keys():
                has_cn = False
                val = name
            else:
                has_cn = True
                val = val[name]

            if val == "":
                val = name
                has_cn = False

            value = PerImage(name, val, has_cn)

            self[name] = value

            return name
        else:
            return name
