import os

import wx

from .extract_structs import PerInfo, PerWorkList


class PerResize(PerInfo):
    def __init__(self, name, val, has_cn):
        super(PerResize, self).__init__(name, val, has_cn)

        self.view_id = None

    def append_to_tree(self, tree: wx.TreeCtrl, tree_root: wx.TreeItemId):
        super(PerResize, self).append_to_tree(tree, tree_root)

        self.view_id = tree.AppendItem(self.tree_ID, "预览拉伸效果")

    def is_inside_id(self, id_got):
        if id_got == self.view_id:
            return True
        else:
            super(PerResize, self).is_inside_id(id_got)

    def find_sub_key(self, id_got):
        if id_got == self.view_id:
            return True, True, self.data.td_view_type, 0, self
        else:
            super(PerResize, self).find_sub_key(id_got)

    def is_able(self):
        if os.path.isfile(self.tex_path):
            return True
        else:
            return False

    def is_need_work(self):
        return super(PerResize, self).is_able()


class ImageResizeList(PerWorkList):
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

            value = PerResize(name, val, has_cn)

            self[name] = value

            return name
        else:
            return name
