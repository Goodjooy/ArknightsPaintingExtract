import json
import os
import re
import shutil
import sys
import time
from collections import Callable

import wx

from core.src.frame_classes.design_frame import MainFrame as Mf
from core.src.frame_classes.setting_frame import Setting
from core.src.static_classes.file_read import FileFilter
from core.src.static_classes.image_deal import ImageWork
from core.src.static_classes.search_order import SearchOrder
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.atlas_structs import AtlasList
from core.src.structs_classes.drop_order import DragOrderPainting, DragOrderAtlas
from core.src.structs_classes.extract_structs import PerWorkList
from core.src.structs_classes.group_split import ImageList
from core.src.thread_classes.extract_thread import RestoreThread
from core.src.thread_classes.quick_view import QuickRestore


class MainFrame(Mf):
    """
    主窗口类
    """

    def __init__(self, parent, path=os.getcwd()):
        super(MainFrame, self).__init__(parent)
        # 添加图标
        icon = wx.Icon(os.path.join(path, "core\\assets\\Tools.ico"))
        self.SetIcon(icon)
        # 舰娘名称文件
        self.g_names = {}
        with open(os.path.join(path, "core\\assets\\names.json"), "r")as file:
            self.g_names = json.load(file)
        # 设置文件
        with open(os.path.join(path, "core\\assets\\setting.json"), 'r')as file:
            self.g_setting_info = json.load(file)

        self.thread_main: RestoreThread = ...
        # 常参储存类
        self.data = GlobalData()
        # 之窗口（只有一个）
        self.g__dialog = None
        self.work_path = path

        """立绘还原部分 p:painting extract"""
        self.p_root = self.m_p_treeCtrl_info.AddRoot(u"")
        # 数据储存结构实例
        self.p_painting_work = PerWorkList()
        self.p_view_work = PerWorkList()
        # 查找tree索引的信息
        self.p_pos, self.p_type_is, self.p_name, self.p_index = None, None, None, None
        # 设置拖动绑定
        self.p_drop = DragOrderPainting(self.p_painting_work, self.p_view_work, self, self.m_p_treeCtrl_info,
                                        self.p_root)
        self.m_p_treeCtrl_info.SetDropTarget(self.p_drop)
        # 立绘还原线程
        self.p_thread_quick = None
        # 进入退出状态
        self.p_enter_exit = False
        # 保存路径，脚本路径
        self.p_save_path = ""
        # ，搜索，筛选器
        self.p_search_type = False
        self.p_filter_type = False
        # 选择项
        self.p_select_data = None

        """atlas 切割部分 atlas ：a"""
        self.a_root = self.m_a_treeCtrl_atlas.AddRoot(u"")

        self.a_atlas_group = AtlasList()
        self.a_atlas_view = AtlasList()

        self.a_tree_type = None
        self.a_tree_is_single = None
        self.a_tree_index = None
        self.a_tree_target = None
        self.a_select_id = None

        self.a_drop = DragOrderAtlas(self.a_atlas_group, self.a_atlas_view, self)
        self.m_a_treeCtrl_atlas.SetDropTarget(self.a_drop)

        self.a_is_search = False

        self.a_region_view_img = {}
        self.a_last_region_id = None

        """矩阵切割部分"""
        self.ar_root = self.m_ar_treeCtrl_array.AddRoot(u"")

        self.ar_img_group = ImageList()
        self.ar_img_view = ImageList()

        self.ar_tree_type = None
        self.ar_tree_is_single = None
        self.ar_tree_index = None
        self.ar_tree_target = None
        self.ar_select_id = None

        self.ar_drop = DragOrderPainting(self.ar_img_group, self.ar_img_view, self, self.m_ar_treeCtrl_array,
                                         self.ar_root)
        self.m_ar_treeCtrl_array.SetDropTarget(self.ar_drop)

        self.ar_is_search = False

        self.ar_region_img = {}
        self.ar_last_select_id = None

        with open(os.path.join(path, "core\\assets\\split_group.json"), 'r')as file:
            temp = json.load(file)
            self.ar_split_group = temp["value"]
            self.ar_name_group = ["<---*--->"]
        self.ar_name_group.extend(temp["name"])
        self.ar_use_split = 0

        self.m_ar_choice_type.Set(self.ar_name_group)
        self.m_ar_choice_type.SetSelection(self.ar_use_split)

    @staticmethod
    def run():
        """
        运行入口函数
        """
        app = wx.App()
        frame = MainFrame(None)

        frame.Show()

        app.MainLoop()

    # 以下为辅助函数，新增部分
    def change_path(self, pos, type_is, target):
        """
        修改指向文件方法
        :param pos: tree中选择类型（单个，列表中文件）
        :param type_is: 选中类型 （tex,mesh）
        :param target: 指向目标方法 type：PerInfo
        """
        if pos:
            if type_is:
                dialog = wx.SingleChoiceDialog(self, "选择更改Texture文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                    id, data = target.set_tex(index)

                    self.m_p_treeCtrl_info.SetItemText(id, data)
            else:
                dialog = wx.SingleChoiceDialog(self, "选择更改Mesh文件", "选择更改文件", target.get_select(type_is))
                if dialog.ShowModal() == wx.ID_OK:
                    index = dialog.GetSelection()
                    id, data = target.set_mesh(index)

                    self.m_p_treeCtrl_info.SetItemText(id, data)

    def a_split_view(self, val):
        img = self.a_region_view_img[val]

        pic, size = ImageWork.transform_image(img, self.m_bitmap_show.GetSize())

        temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())

        self.m_bitmap_show.SetBitmap(temp)

    def a_split_work(self, val, target):
        if self.a_last_region_id is not None:
            if val == self.a_last_region_id:
                return
            else:
                self.m_a_treeCtrl_atlas.DeleteChildren(self.a_last_region_id)
                self.a_region_view_img.clear()
        self.a_last_region_id = val

        is_ok, img_group = ImageWork.atlas_split_view(target, self.m_bitmap_show.GetSize())
        if is_ok:
            for name, img in img_group.items():
                key = self.m_a_treeCtrl_atlas.AppendItem(val, name)
                self.a_region_view_img[key] = img[0]

            self.m_a_treeCtrl_atlas.Expand(val)

    # 以下为原有函数
    def restart(self):
        """
        重置还原线程
        """
        self.thread_main = RestoreThread(1, 'restore', self.p_painting_work.build_able(),
                                         self.p_painting_work.build_unable(), self, self.g_setting_info,
                                         self.g_names, self.p_save_path)

        self.m_staticText_info.SetLabel("重置还原进度！")

        self.m_gauge_state.SetValue(0)

    # export
    def export_choice(self):
        """
        导出选择项
        """
        self.g__dialog = wx.DirDialog(self, "保存", os.getcwd(), style=wx.DD_NEW_DIR_BUTTON)

        if self.g__dialog.ShowModal() == wx.ID_OK:
            self.m_gauge_state.SetValue(0)
            self.p_save_path = self.g__dialog.GetPath()

            self.m_staticText_info.SetLabel("什么都没发生")
            # self.export_all(self.save_path, PerWorkList([self.select_data, ]))

        self.m_gauge_state.SetValue(100)

        if self.g_setting_info[self.data.sk_finish_exit]:
            self.exit()

    def export_all(self, path, for_work: PerWorkList = None, func: Callable = ...):
        """
        导出输入列表中的项
        :param func: 执行方法
        :param path: 保存的路径
        :param for_work: 输入的列表
        """
        data = self.data

        if self.g_setting_info[data.sk_make_new_dir]:
            path += r"\明日方舟-导出"

        os.makedirs(path, exist_ok=True)

        self.restart()
        self.p_save_path = path
        self.m_gauge_state.SetValue(0)

        if isinstance(for_work, PerWorkList):
            able = for_work.build_able()
        else:
            able = self.p_painting_work.build_able()

        # 跳过已经存在的处理
        if self.g_setting_info[data.sk_skip_exist]:
            target_path_list = FileFilter.all_file(path)

            skip = able.build_skip(target_path_list)
            able = able.remove(skip)

        # 启动线程
        self.thread_main.add_save_path(self.p_save_path)
        self.thread_main.update_value(able, for_work.build_unable())
        if isinstance(func, Callable):
            self.thread_main.work_function = func

        if self.thread_main.is_alive():
            self.thread_main.stop_(True)
            while self.thread_main.is_alive():
                time.sleep(1)
            self.thread_main.start()
        else:
            self.thread_main.start()

    def copy_file(self):
        """
        拷贝不可还原文件
        """
        data = self.data
        self.g__dialog = wx.DirDialog(self, "保存", os.getcwd(),
                                      style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON
                                            | wx.DD_DEFAULT_STYLE)
        if self.g__dialog.ShowModal() == wx.ID_OK:
            unable = self.p_painting_work.build_unable()
            path = self.g__dialog.GetPath()
            if self.g_setting_info[data.sk_output_group] == data.feg_by_type:
                path += "\\拷贝"
            num = 0
            self.m_gauge_state.SetValue(0)
            for name in unable:
                num += 1
                name.add_save(path)
                shutil.copyfile(name.tex_path, name.save_path)

                self.m_gauge_state.SetValue(round(100 * (num / len(unable))))

        if self.g_setting_info[data.sk_open_output_dir]:
            os.system(r'start "%s"' % self.p_save_path)
        if self.g_setting_info[data.sk_finish_exit]:
            self.exit()

    def __search(self, value):
        """
        搜索封装方法
        :param value: 搜索关键字
        """
        is_regex = self.g_setting_info[self.data.sk_regex_search]
        is_inverse = self.g_setting_info[self.data.sk_inverse]

        if value != '':
            try:
                if not self.p_filter_type:
                    indexes = SearchOrder.find(value, self.p_painting_work.build_search(), is_regex=is_regex,
                                               is_inverse=is_inverse)
                    self.p_view_work = self.p_painting_work.build_from_indexes(indexes)
                else:
                    indexes = SearchOrder.find(value, self.p_view_work.build_search(), is_regex=is_regex,
                                               is_inverse=is_inverse)
                    self.p_view_work = self.p_view_work.build_from_indexes(indexes)

                self.p_search_type = True

                self.p_enter_exit = True
                self.m_p_treeCtrl_info.DeleteChildren(self.p_root)
                self.p_view_work.show_in_tree(self.m_p_treeCtrl_info, self.p_root)
                self.p_enter_exit = False

            except re.error as info:
                self.m_staticText_info.SetLabel("非法的正则表达式：%s；错误为：%s" % (value, str(info)))
            else:
                self.m_staticText_info.SetLabel("合法的正则表达式：%s" % value)
        else:
            self.p_search_type = False

            self.p_enter_exit = True
            self.m_p_treeCtrl_info.DeleteChildren(self.p_root)
            self.p_painting_work.show_in_tree(self.m_p_treeCtrl_info, self.p_root)
            self.p_enter_exit = False

    # 以下为回调函数

    # 立绘处理部分
    def p_on_info_select(self, event):
        """选择tree中的元素时使用"""
        if not self.p_enter_exit:
            self.m_p_button_change.Enable(False)
            val = event.GetItem()

            if not self.p_search_type and not self.p_filter_type:
                is_ok, name = self.p_painting_work.find_by_id(val)
            else:
                is_ok, name = self.p_view_work.find_by_id(val)
            if is_ok:
                self.m_staticText_info.SetLabel(f"选择：{name.cn_name}")

                self.p_select_data = self.p_name = name
                self.p_thread_quick = QuickRestore(name, self)
                self.p_thread_quick.start()
            # 寻找tex或mesh路径句柄
            else:
                if not self.p_search_type and not self.p_filter_type:
                    is_ok, pos, type_is, index, name = self.p_painting_work.find_in_each(val)
                else:
                    is_ok, pos, type_is, index, name = self.p_view_work.find_in_each(val)
                if is_ok:
                    pass
                # 显示图片，如果可以
                if is_ok:
                    # 可用修改
                    self.m_p_button_change.Enable(True)
                    self.p_pos, self.p_type_is, self.p_name, self.p_index = pos, type_is, name, index

                    is_able, value = name.build_sub(pos, type_is, index)
                    if is_able:
                        self.p_thread_quick = QuickRestore(value, self)
                        self.p_thread_quick.start()
                        self.p_select_data = value
                        is_able = "可预览"
                    else:
                        is_able = "不可预览"

                    if pos:
                        pos = "单个类型"
                    else:
                        pos = "列表"
                    if type_is == 0:
                        type_is = "texture文件"
                    else:
                        type_is = "mesh文件"

                    self.m_staticText_info.SetLabel(
                        f"选择： {name.cn_name}中的{pos}{type_is}: {self.m_p_treeCtrl_info.GetItemText(val)}，{is_able}")

    def p_choice_file(self, event):
        if self.p_pos == self.data.td_single:
            self.change_path(self.p_pos, self.p_type_is, self.p_name)
        else:
            if self.p_type_is == self.data.td_texture_type:
                self.p_name.set_tex(self.p_index)
            else:
                self.p_name.set_mesh(self.p_index)

        self.p_thread_quick = QuickRestore(self.p_name, self)
        self.p_thread_quick.run()

    def p_work(self, event):
        data = self.data
        show = ["导出全部可还原", "拷贝全部不可还原", "导出选择项", "导出当前列表项"]
        if len(self.p_painting_work.build_able()) == 0:
            show[data.et_all] += "（不可用）"
        if len(self.p_painting_work.build_unable()) == 0:
            show[data.et_copy_only] += "（不可用）"
        if self.p_name is None:
            show[data.et_select] += "（不可用）"
        if self.p_filter_type or self.p_search_type:
            if self.p_view_work.__len__() == 0:
                show[data.et_list_item] += "（不可用）"
        else:
            if len(self.p_painting_work) == 0:
                show[data.et_list_item] += "（不可用）"

        self.g__dialog = wx.SingleChoiceDialog(self, "选择类型", "选择导出类型", show)

        if self.g__dialog.ShowModal() == wx.ID_OK:
            index = self.g__dialog.GetSelection()
            if index == data.et_all:
                if len(self.p_painting_work.build_able()) == 0:
                    wx.MessageBox("不可用！", "错误")
                    return

                title = '保存'
                title += "-明日方舟"

                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()

                    if self.p_painting_work.build_able().__len__() > 0:
                        self.export_all(temp, self.p_painting_work)

            if index == data.et_copy_only:
                if len(self.p_painting_work.build_unable()) == 0:
                    wx.MessageBox("不可用！！", "错误")
                    return
                self.copy_file()
            if index == data.et_select:
                if self.p_name is None:
                    wx.MessageBox("不可用！！", "错误")
                    return

                self.export_choice()
            if index == data.et_list_item:

                if self.p_filter_type or self.p_search_type:
                    if self.p_view_work.__len__() == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return
                else:
                    if len(self.p_painting_work) == 0:
                        wx.MessageBox("不可用！！", "错误")
                        return

                title = '保存'
                title += "-明日方舟"

                address = os.getcwd()
                dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

                if dialog.ShowModal() == wx.ID_OK:
                    temp = dialog.GetPath()

                    if self.p_painting_work.build_able().__len__() > 0:
                        self.export_all(temp, self.p_view_work)

    def p_filter_work(self, event):
        index = event.GetSelection()
        value = self.data.fp_pattern_group[index]

        if index == self.data.tf_all:
            self.p_filter_type = False

            self.p_enter_exit = True
            self.m_p_treeCtrl_info.DeleteChildren(self.p_root)
            self.p_painting_work.show_in_tree(self.m_p_treeCtrl_info, self.p_root)
            self.p_enter_exit = False
        else:
            if self.p_search_type:
                self.p_view_work = self.p_view_work.build_from_pattern(value)
            else:
                self.p_view_work = self.p_painting_work.build_from_pattern(value)

            self.p_filter_type = True

            self.p_enter_exit = True
            self.m_p_treeCtrl_info.DeleteChildren(self.p_root)
            self.p_view_work.show_in_tree(self.m_p_treeCtrl_info, self.p_root)
            self.p_enter_exit = False

    def p_search(self, event):
        if self.g_setting_info[self.data.sk_auto_search]:
            if event is None:
                value = self.m_p_searchCtrl_tree.GetValue()
            else:
                value = event.GetString()

            self.__search(value)

    def p_search_work(self, event):
        if event is None:
            value = self.m_p_searchCtrl_tree.GetValue()
        else:
            value = event.GetString()

        self.__search(value)

    def p_cancel_work(self, event):
        if self.g_setting_info[self.data.sk_regex_search]:
            self.m_p_searchCtrl_tree.SetValue("^.+$")
            self.__search("^.+$")
        else:
            self.m_p_searchCtrl_tree.SetValue("")
            self.__search("")

    def p_setting(self, event):
        self.g__dialog = Setting(self, self.g_setting_info, self.work_path)

        self.g__dialog.ShowModal()

        self.g_setting_info = self.g__dialog.get_setting()

    # atlas 切割部分
    def a_update_atlas(self, event):
        self.a_atlas_group = self.a_atlas_group.extract_tex(self.p_painting_work)
        self.m_a_treeCtrl_atlas.DeleteChildren(self.a_root)
        self.a_atlas_group.show_in_tree(self.m_a_treeCtrl_atlas, self.a_root)

    def a_change_atlas(self, event):
        if self.a_tree_type == self.data.td_atlas_type:
            if self.a_tree_is_single:
                self.g__dialog = wx.SingleChoiceDialog(self, "选择atlas文件", "请选择", self.a_tree_target.more_atlas)

                if self.g__dialog.ShowModal() == wx.ID_OK:
                    index = self.g__dialog.GetSelection()
                    id, data = self.a_tree_target.set_atlas(index)

                    self.m_a_treeCtrl_atlas.SetItemText(id, data)

            else:
                id, data = self.a_tree_target.set_atlas(self.a_tree_index)

                self.m_a_treeCtrl_atlas.SetItemText(id, data)

    def a_export(self, event):
        if self.a_is_search:
            work_on = self.a_atlas_view
        else:
            work_on = self.a_atlas_group
        title = '保存'
        title += "-明日方舟"

        address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if work_on.build_able().__len__() > 0:
                self.export_all(temp, work_on, ImageWork.atlas_split_export)

    def a_search(self, event):
        value = event.GetString()
        if value != r"^.*$":
            try:
                indexes = SearchOrder.find(value, self.a_atlas_group.build_search(), is_regex=True,
                                           is_inverse=False)
                self.a_atlas_view = self.a_atlas_group.build_from_indexes(indexes)

                self.a_is_search = True

                self.m_a_treeCtrl_atlas.DeleteChildren(self.a_root)
                self.a_atlas_view.show_in_tree(self.m_a_treeCtrl_atlas, self.a_root)
            except re.error as info:
                self.m_staticText_info.SetLabel(f"非法的正则表达式！ 为{value},错误：{info}")
        else:
            self.a_atlas_view.clear()
            self.a_is_search = False
            self.m_a_treeCtrl_atlas.DeleteChildren(self.a_root)
            self.a_atlas_group.show_in_tree(self.m_a_treeCtrl_atlas, self.a_root)

    def a_tree_select(self, event):
        """选择tree中的元素时使用"""
        type_group = ("texture2d贴图", "mesh网格", "atlas文件", "切割预览")
        if self.a_is_search:
            work_on = self.a_atlas_view
        else:
            work_on = self.a_atlas_group

        val = event.GetItem()
        self.a_select_id = val

        # 第一步，检测单独元素选择
        is_ok, target = work_on.find_by_id(val)
        if is_ok:
            self.a_tree_target = target

            self.m_staticText_info.SetLabel(f'【Atlas区】选择：{target.cn_name}')
        elif val in self.a_region_view_img.keys():
            self.a_split_view(val)
        else:
            # 内部元素检查
            is_ok, is_single, type_is, index, target = work_on.find_in_each(val)
            if is_ok:
                self.a_tree_is_single = is_single
                self.a_tree_type = type_is
                self.a_tree_index = index
                self.a_tree_target = target

                self.m_staticText_info.SetLabel(f'【Atlas区】选择：{target.cn_name}中的{type_group[type_is]},单个为{is_single}')

                if type_is == self.data.td_region_type:
                    # 切割
                    self.a_split_work(val, target)

    # 阵列切割区
    def ar_export(self, event):
        if self.ar_is_search:
            work_on = self.ar_img_view
        else:
            work_on = self.ar_img_group
        title = '保存'
        title += "-明日方舟"

        address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if work_on.build_able().__len__() > 0:
                self.export_all(temp, work_on, ImageWork.array_split_export_builder(self.ar_split_group[self.ar_use_split - 1]))

    def ar_new_spliter(self, event):
        pass

    def ar_remove_spliter(self, event):
        pass

    def ar_search(self, event):
        value = event.GetString()
        if value != r"^.*$":
            try:
                indexes = SearchOrder.find(value, self.ar_img_group.build_search(), is_regex=True,
                                           is_inverse=False)
                self.ar_img_view = self.ar_img_group.build_from_indexes(indexes)

                self.ar_is_search = True

                self.m_ar_treeCtrl_array.DeleteChildren(self.ar_root)
                self.ar_img_view.show_in_tree(self.m_ar_treeCtrl_array, self.ar_root)
            except re.error as info:
                self.m_staticText_info.SetLabel(f"非法的正则表达式！ 为{value},错误：{info}")
        else:
            self.ar_img_view.clear()
            self.ar_is_search = False
            self.m_ar_treeCtrl_array.DeleteChildren(self.a_root)
            self.ar_img_group.show_in_tree(self.m_ar_treeCtrl_array, self.ar_root)

    def ar_tree_select(self, event):
        """选择tree中的元素时使用"""
        type_group = ("texture2d贴图", "mesh网格", "atlas文件", "切割预览")
        if self.ar_is_search:
            work_on = self.ar_img_view
        else:
            work_on = self.ar_img_group

        val = event.GetItem()
        self.ar_select_id = val

        # 第一步，检测单独元素选择
        is_ok, target = work_on.find_by_id(val)
        if is_ok:
            self.ar_tree_target = target

            self.m_staticText_info.SetLabel(f'【阵列切割区】选择：{target.cn_name}')
        elif val in self.ar_region_img.keys():
            self.ar_split_view(val)
        else:
            # 内部元素检查
            is_ok, is_single, type_is, index, target = work_on.find_in_each(val)
            if is_ok:
                self.ar_tree_is_single = is_single
                self.ar_tree_type = type_is
                self.ar_tree_index = index
                self.ar_tree_target = target

                self.m_staticText_info.SetLabel(f'【阵列切割区】选择：{target.cn_name}中的{type_group[type_is]},单个为{is_single}')

                if type_is == self.data.td_region_type:
                    # 切割
                    self.ar_split_work(val, target)

    def ar_type_change(self, event):
        self.ar_use_split = event.GetSelection()

    def exit(self, event=None):
        self.p_enter_exit = True
        self.m_p_treeCtrl_info.DeleteChildren(self.p_root)
        self.m_p_treeCtrl_info.Destroy()
        self.Destroy()
        sys.exit()

    def ar_split_view(self, val):
        img = self.ar_region_img[val]

        pic, size = ImageWork.transform_image(img, self.m_bitmap_show.GetSize())

        temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())

        self.m_bitmap_show.SetBitmap(temp)

    def ar_split_work(self, val, target):
        if self.ar_use_split == 0:
            return
        if self.ar_last_select_id is not None:
            if val == self.ar_last_select_id:
                return
            else:
                self.m_ar_treeCtrl_array.DeleteChildren(self.ar_last_select_id)
                self.ar_region_img.clear()
        self.ar_last_select_id = val

        is_ok, img_group = ImageWork.array_split_view_builder(self.ar_split_group[self.ar_use_split - 1]) \
            (target, self.m_bitmap_show.GetSize())
        if is_ok:
            for index in range(len(img_group)):
                key = self.m_ar_treeCtrl_array.AppendItem(val, f'No.{index + 1}')
                self.ar_region_img[key] = img_group[index][0]

            self.m_ar_treeCtrl_array.Expand(val)
