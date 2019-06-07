import re
from collections import Iterable

import wx

from core.src.structs_classes.basic_class import BasicInfo, BasicInfoList


class PerFormat(BasicInfo):
    def __init__(self, name: str, values=dict):
        super(PerFormat, self).__init__(name, values)

        self.tree_id = None

        self.ex_key = self.val["ex_key"]
        self.ex_format = self.val["ex_format"]
        self.ex_id = None

        self.num_key = self.val["num_key"]
        self.num_format = self.val["num_format"]
        self.num_id = None

        self.name_key = self.val["name_key"]
        self.name_format = self.val["name_format"]
        self.name_id = None

        self.skin_key = self.val["skin_key"]
        self.skin_format = self.val["skin_format"]
        self.skin_id = None

        self.match_size = self.val["size"]
        self.size_id = None

        self.format_str = self.val["format"]
        self.format_group = self.val["format_group"]
        self.format_id = None
        self.format_group_id = None

        self.__pattern = re.compile(r"^(enemy|char|build_char|npc)_([0-9]{3,4})_(.+?)(?=$|_)_?(.+)?$")
        self.format_pattern = re.compile(r'{(\d+)}')

    def is_support(self, value, size):
        if size == self.match_size:
            ex, num, name, skin = self.__pattern.match(value).groups()
            if ex == self.ex_key and num == self.num_key and name == self.name_key and skin == self.skin_key:
                return True
        return False

    def format(self, value, size):
        if self.is_support(value, size):
            target = self.format_str
            group = set(self.format_pattern.findall(target))

            for val in group:
                target = target.replace("{%s}" % val, self.format_group[val])

            return target
        return None

    def to_dict(self):
        return {"ex_key": self.ex_key, "ex_format": self.ex_format, "num_key": self.num_key,
                "num_format": self.num_format, "name_key": self.name_key, "name_format": self.name_format,
                "skin_key": self.skin_key, "skin_format": self.skin_format, "size": self.match_size,
                "format": self.format_str, "format_group": self.format_group}

    def add_2_tree(self, tree: wx.TreeCtrl, root):
        self.tree_id = tree.AppendItem(root, self.name)

        self.ex_id = tree.AppendItem(self.tree_id, f"前缀标识符：{self.ex_key};前缀名称：{self.ex_format}")
        self.num_id = tree.AppendItem(self.tree_id, f"编号标识符：{self.num_key};编号名称：{self.num_format}")
        self.name_id = tree.AppendItem(self.tree_id, f"名称标识符：{self.name_key};名称名称：{self.name_format}")
        self.skin_id = tree.AppendItem(self.tree_id, f"皮肤/精英化标识符：{self.skin_key};皮肤/精英化名称：{self.skin_format}")

        return self.tree_id


class FormatList(BasicInfoList):
    def __init__(self, name, item: Iterable):
        super(FormatList, self).__init__(item)

        self.name = name

        self.root = None
        self.body_id = []

    def get_able_format(self, value):
        val = list(filter(lambda x: x.is_support(value), self))
        return val[0]

    def add_to_tree(self, tree: wx.TreeCtrl, root):
        self.root = tree.AppendItem(root, self.name)

        for val in self:
            tree_id = val.add_2_tree(tree, self.root)
            self.body_id.append(tree_id)

        return self.root
