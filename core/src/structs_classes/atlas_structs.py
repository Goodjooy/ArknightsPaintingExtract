import os
import re
from collections import Iterable

import wx

from core.src.structs_classes.extract_structs import PerInfo, PerWorkList


class PerAtlas(PerInfo):
    def __init__(self, name, val, has_cn):
        super(PerAtlas, self).__init__(name, val, has_cn)
        self._atlas_path = "Empty"
        self.more_atlas = []

        self.atlas_id = ...
        self.more_atlas_ids = []

        self.is_able_split = False

        self.region_id = None

    @staticmethod
    def to_atlas(value: PerInfo):
        val = PerAtlas(value.name, value.val, value.has_cn)

        for key, v in value.__dict__.items():
            val.__setattr__(key, v)

        val.tree_ID = ...
        val.tex_id = ...
        val.more_tex_per_id = []
        val.mesh_id = ...
        val.more_mesh_per_id = []

        val.is_able_work = val.is_able()

        return val

    @property
    def atlas_path(self):
        return self._atlas_path

    @atlas_path.setter
    def atlas_path(self, value):
        if isinstance(value, str):
            self._atlas_path = value
            self.is_able_split = self.is_able()

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
        val = os.path.isfile(self._tex_path) and os.path.isfile(self._atlas_path)
        return val

    def is_need_work(self):
        return super(PerAtlas, self).is_able()

    def set_atlas(self, index):
        self.atlas_path = self.more_atlas[index]
        return self.atlas_id, f"Atlas文件路径：{self.atlas_path}"

    def append_to_tree(self, tree: wx.TreeCtrl, tree_root: wx.TreeItemId):
        """
        添加到树
        :param tree: tree 对象
        :param tree_root: 根id
        :return:
        """
        self.more_mesh_per_id.clear()
        self.more_tex_per_id.clear()
        self.more_atlas_ids.clear()

        self.tree_ID = tree.AppendItem(tree_root, self.cn_name)

        key = tree.AppendItem(self.tree_ID, f"名称：{self.cn_name}")
        if self.is_able_work:
            tree.SetItemTextColour(key, wx.Colour(253, 86, 255))
        tree.AppendItem(self.tree_ID, f"原始文件名：{self.name}")

        self.tex_id = tree.AppendItem(self.tree_ID, f"Texture文件路径：{self.tex_path}")
        self.mesh_id = tree.AppendItem(self.tree_ID, f"Mesh文件路径：{self.mesh_path}")
        self.atlas_id = tree.AppendItem(self.tree_ID, f"Atlas文件路径：{self.atlas_path}")

        more_atlas = tree.AppendItem(self.tree_ID, "其他Atlas文件")
        for each_path in self.more_atlas:
            val = tree.AppendItem(more_atlas, each_path)
            self.more_atlas_ids.append(val)

        self.region_id = tree.AppendItem(self.tree_ID, f"切割效果预览")

    def extract_atlas(self, value: PerInfo):
        val = PerAtlas.to_atlas(value)
        val._atlas_path = self._atlas_path
        val.more_atlas = self.more_atlas

        val.atlas_id = self.atlas_id
        val.more_atlas_ids = self.more_atlas_ids

        val.region_id = self.region_id

        val.is_able_split = self.is_able_split

        val.is_able_work = val.is_able()
        return val

    def is_inside_id(self, id_got):
        if id_got == self.region_id:
            return True
        elif id_got == self.atlas_id:
            return True
        elif id_got in self.more_atlas_ids:
            return True
        else:
            return super(PerAtlas, self).is_inside_id(id_got)

    def find_sub_key(self, id_got):
        if id_got == self.region_id:
            return True, True, self.data.td_region_type, 0, self
        elif id_got == self.atlas_id:
            return True, True, self.data.td_atlas_type, 0, self
        elif id_got in self.more_atlas_ids:
            return True, False, self.data.td_atlas_type, self.more_atlas_ids.index(id_got), self
        else:
            return super(PerAtlas, self).find_sub_key(id_got)


class AtlasList(PerWorkList):
    def __init__(self, items: Iterable = None):
        super(AtlasList, self).__init__(items)

    @staticmethod
    def to_atlas(item: PerWorkList):
        val = map(lambda x: PerAtlas.to_atlas(x), item)

        return AtlasList(val)

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

            value = PerAtlas(name, val, has_cn)

            self[name] = value

            return name
        else:
            return name

    def set_atlas(self, value, name):
        """
        添加atlas切割文件
        :param name: 新添加的mesh地址的指向项目名称，为None会根据value获取
        :param value: 新添加的mesh地址
        :return:
        """
        has_ = False
        if isinstance(value, str) and os.path.isfile(value):

            key = name
            if re.match(r'.+\s#\d+\.(?:atlas|atlas\.txt)', value, re.IGNORECASE):
                has_ = True

            val: PerAtlas = self._info_dict[key]
            if value not in val.more_atlas:
                val.more_atlas.append(value)

            if val.atlas_path.lower() == "empty":
                val.atlas_path = value
            if os.path.split(value)[0].lower().endswith("mesh"):
                val.atlas_path = value
            if not has_:
                val.atlas_path = value

    def extract_tex(self, items: PerWorkList):
        def work(val_inside):
            if val_inside.name in items:
                return val_inside.extract_atlas(items[val_inside.name])
            else:
                return val_inside

        val = map(work, self)
        return AtlasList(val)
