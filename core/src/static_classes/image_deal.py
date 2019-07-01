import json
import os
import re
from functools import reduce
from re import match, split

import PIL.Image
import numpy
import wx
from PIL import Image

from core.src.static_classes.png2svg import rgba_image_to_svg_pixels
from core.src.static_classes.static_data import GlobalData
from core.src.structs_classes.painting_work_structs.atlas_structs import PerAtlas
from core.src.structs_classes.painting_work_structs.extract_structs import PerInfo
from core.src.structs_classes.painting_work_structs.group_split import PerImage
from core.src.structs_classes.painting_work_structs.image_resize import PerResize


class ImageWork(object):
    # azur lane remain func
    @staticmethod
    def az_cut_pic_builder(size):
        """
        :param size: the input img size(wide,high)
        :return: a callable func
        """

        def cut_pic(info):
            a = [round(float(info[1]) * size[0]), round((1 - float(info[2])) * size[1])]

            return a

        return cut_pic

    @staticmethod
    def az_draw(pic, pos):
        pic.paste(pos[0], pos[1])
        return pic

    @staticmethod
    def az_division_builder(val1, val2, pic):
        def division(val):
            print_p = [val1[val[0] - 1], val1[val[1] - 1], val1[val[2] - 1]]
            cut_p = [val2[val[0] - 1], val2[val[1] - 1], val2[val[2] - 1]]

            print_area = [min(print_p[0][0], print_p[1][0], print_p[2][0]),
                          min(print_p[0][1], print_p[1][1], print_p[2][1])]

            cut_x = round(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]))
            cut_y = round(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])))

            end_x = round(
                (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])))
            end_y = round(
                (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])))

            cut_size = (cut_x, cut_y, end_x, end_y)

            cut = pic.crop(cut_size)
            return cut, print_area

        return division

    @staticmethod
    def az_paint_restore(mesh_path: str, tex_path: str):
        """
        a higher func version for extract AzurLane painting
        :param mesh_path: mesh_file address,str
        :param tex_path: texture file address
        :return: PIL.Image -> the final pic
        """
        img = PIL.Image.open(tex_path)

        size = img.size

        tex_cuter = ImageWork.az_cut_pic_builder(size)

        with open(mesh_path, 'r', encoding='utf-8')as file:
            files_line = file.readlines()

        draw_pic = filter(lambda x: match(r'^v\s-*\d+\s-*\d+\s-*\d+\n$', x), files_line)
        tex_pos = filter(lambda x: match(r'^vt\s0\.\d+\s0\.\d+\n$', x), files_line)
        print_pos = filter(lambda x: match(r'^f\s\d+/\d+/\d+\s\d+/\d+/\d+\s\d+/\d+/\d+\n$', x), files_line)

        draw_pic = map(lambda x: split(r'\D+', x), draw_pic)
        tex_pos = map(lambda x: split(r'[^0-9.]+', x), tex_pos)
        print_pos = map(lambda x: split(r'\D+', x), print_pos)

        draw_pic = (map(lambda x: [int(x[1]), int(x[2])], draw_pic))
        tex_pos = (map(tex_cuter, tex_pos))
        print_pos = (map(lambda x: [int(x[1]), int(x[4]), int(x[7])], print_pos))
        draw_pic = list(draw_pic)
        pos = draw_pic.copy()
        x_poses, y_poses = zip(*pos)

        x_pic = (max(x_poses))
        y_pic = (max(y_poses))

        pic = PIL.Image.new("RGBA", (x_pic, y_pic), (255, 255, 255, 0))

        draw_pic = (map(lambda x: [(x[0]), (y_pic - x[1])], draw_pic))

        division = ImageWork.az_division_builder(list(draw_pic), list(tex_pos), img)

        restore = (map(division, print_pos))

        pic_out = reduce(ImageWork.az_draw, restore, pic)

        return pic_out

    # global func
    @staticmethod
    def g_show_in_screen(pic, bitmap):
        """
        show the target image in the BitMapCtrl
        :param pic: target image
        :param bitmap:
        :return:None
        """
        temp = wx.Bitmap.FromBufferRGBA(pic.width, pic.height, pic.tobytes())
        bitmap.SetBitmap(temp)

    @staticmethod
    def g_transform_image(pic, size, is_expend=True, bg_color=(255, 255, 255, 0)):
        size = tuple(size)
        pic_size = pic.size
        bg = PIL.Image.new("RGBA", size, bg_color)
        # bg.show()

        scale = min(bg.size[0] / pic.size[0], bg.size[1] / pic.size[1])
        size = (round(pic.size[0] * scale), round(pic.size[1] * scale))

        if is_expend and pic.size[0] <= size[0] and pic.size[1] <= size[1]:
            pic = pic
        else:
            pic = pic.resize(size, PIL.Image.ANTIALIAS)

        x = round(bg.size[0] / 2 - pic.size[0] / 2)
        y = round(bg.size[1] / 2 - pic.size[1] / 2)
        bg.paste(pic, (x, y, x + pic.size[0], y + pic.size[1]))
        return bg, pic_size

    @staticmethod
    def g_load_and_transform(path, size):
        pic = PIL.Image.open(path)

        return ImageWork.g_transform_image(pic, size)

    # ark nights painting work func
    @staticmethod
    def p_ak_painting_main(alpha_path, tex_path):
        """
        for mrfz
        :param alpha_path:
        :param tex_path:
        :return:
        """
        if os.path.isfile(tex_path) and os.path.isfile(alpha_path):
            tex_img = PIL.Image.open(tex_path)
            alpha_img = PIL.Image.open(alpha_path)

            assert tex_img.size == alpha_img.size

            info_array = numpy.array(tex_img)
            alpha_array = numpy.array(alpha_img)

            alpha_array = alpha_array[:, :, 0]

            info_array[:, :, -1] = alpha_array

            img = PIL.Image.fromarray(info_array.astype("uint8")).convert("RGBA")

            return img

    @staticmethod
    def p_restore_tool(now_info: PerInfo):
        """拼图用的函数
        """
        try:
            pic = ImageWork.p_ak_painting_main(now_info.mesh_path, now_info.tex_path)

            pic.save(now_info.save_path)
        except RuntimeError as info:
            return False, str(info)
        except ValueError as info:
            return False, "math" + str(info)
        except AssertionError:
            return False, "尺寸匹配错误"
        else:
            return True, "成功还原：%s" % now_info.cn_name

    @staticmethod
    def p_restore_tool_one(mesh_path, pic_path, save_as, ):
        """拼图用的函数"""

        pic = ImageWork.p_ak_painting_main(mesh_path, pic_path)

        assert isinstance(save_as, str)
        pic.save(save_as)

    @staticmethod
    def p_restore_tool_no_save(mesh_path, pic_path, size: tuple):
        """拼图用的函数"""
        pic = ImageWork.p_ak_painting_main(mesh_path, pic_path)

        return ImageWork.g_transform_image(pic, size)

    # atlas split work func
    @staticmethod
    def atlas_split_main(img, atlas_file):
        info_pattern = re.compile(r'(.+)\n'
                                  r'\s{2}rotate:\s(false|true)\n'
                                  r'\s{2}xy:\s(\d+),\s(\d+)\n'
                                  r'\s{2}size:\s(\d+),\s(\d+)\n'
                                  r'\s{2}orig:\s\d+,\s\d+\n'
                                  r'\s{2}offset:\s0,\s0\n'
                                  r'\s{2}index:\s-1')
        group = {}

        # 加载分割文件
        with open(atlas_file, 'r', encoding="utf-8")as files:
            file_work = files.read()

        info = info_pattern.findall(file_work)

        for body in info:
            mod_name = body[0]
            group[mod_name] = {}
            group[mod_name]['rotate'] = json.loads(body[1])
            group[mod_name]['xy'] = [int(body[2]), int(body[3])]
            group[mod_name]['size'] = [int(body[4]), int(body[5])]

        values = {}
        for var in group.keys():

            xy = group[var]['xy']
            size = group[var]['size']

            if group[var]['rotate']:
                rect = (xy[0], xy[1], size[1] + xy[0], size[0] + xy[1])
            else:
                rect = (xy[0], xy[1], size[0] + xy[0], size[1] + xy[1])

            val = img.crop(rect)
            if group[var]['rotate']:
                val = val.rotate(-90, expand=True)

            values[var] = val

        return values

    @staticmethod
    def atlas_split_export_builder(is_use_svg=False, scale=1):
        def atlas_split_export(value: PerAtlas):
            try:
                if value.is_need_work():
                    work_image = ImageWork.p_ak_painting_main(value.mesh_path, value.tex_path)
                else:
                    work_image = PIL.Image.open(value.tex_path)
                img_group = ImageWork.atlas_split_main(work_image, value.atlas_path)

                os.makedirs(value.save_path, exist_ok=True)

                for key in img_group.keys():
                    if is_use_svg:
                        svg_info = rgba_image_to_svg_pixels(img_group[key])
                        with open(os.path.join(value.save_path, key + ".svg"), 'w') as file:
                            file.write(svg_info)
                    else:
                        pic = img_group[key]
                        if scale == 1:
                            pic.save(os.path.join(value.save_path, key + ".png"))
                        else:
                            pic = pic.resize((round(pic.width * scale), round(pic.height * scale)), PIL.Image.BILINEAR)
                            pic.save(os.path.join(value.save_path, key + ".png"))

            except Exception as info:
                return False, str(info)
            else:
                return True, "successfully"

        return atlas_split_export

    @staticmethod
    def atlas_split_view(value: PerAtlas, size):

        try:
            if value.is_need_work():
                work_image = ImageWork.p_ak_painting_main(value.mesh_path, value.tex_path)
            else:
                work_image = PIL.Image.open(value.tex_path)
            img_group = ImageWork.atlas_split_main(work_image, value.atlas_path)

            for key in img_group.keys():
                img_group[key] = ImageWork.g_transform_image(img_group[key], size)

        except Exception as info:
            return False, info
        else:
            return True, img_group

    """矩阵切割部分"""

    # array split work func
    @staticmethod
    def array_split_main(img, val_x, val_y, size_w, size_h, size, inside):
        value = img.crop(
            [(val_x - 1) * size_w,
             size[1] - val_y * size_h,
             val_x * size_w,
             size[1] - (val_y - 1) * size_h
             ])
        value = value.crop([inside, inside, size_w - inside, size_h - inside])

        return value

    @staticmethod
    def array_split_build_list_builder(split_guider: dict = ...):
        def array_split_build_list(value: PerImage, ):
            if isinstance(split_guider, dict):
                if value.is_need_work():
                    img = ImageWork.p_ak_painting_main(value.mesh_path, value.tex_path)
                else:
                    img = PIL.Image.open(value.tex_path)
                img_list = []
                size = img.size
                size_w = split_guider["size_w"]
                size_h = split_guider["size_h"]
                inside = split_guider["inside"]

                value_y = int(img.height / size_h)
                value_x = int(img.width / size_w)

                for val_x in range(1, value_x + 1):
                    for val_y in range(1, value_y + 1):
                        value = ImageWork.array_split_main(img, val_x, val_y, size_w, size_h, size, inside)
                        img_list.append(value)

                return img_list

        return array_split_build_list

    @staticmethod
    def array_split_quick_view_single(img, val_x, val_y, size_w, size_h, inside, s_size):
        size = img.size

        val = ImageWork.array_split_main(img, val_x, val_y, size_w, size_h, size, inside)

        val, size = ImageWork.g_transform_image(val, s_size)

        return val

    @staticmethod
    def array_split_view_builder(split_guider: dict = ...):
        def view(value, size):
            try:
                val_list = ImageWork.array_split_build_list_builder(split_guider)(value)
                re_val = []
                for val in val_list:
                    re_val.append(ImageWork.g_transform_image(val, size))

                return True, re_val
            except Exception as _:
                return False, _

        return view

    @staticmethod
    def array_split_export_builder(split_guider: dict = ...):
        def export(value: PerImage):
            try:
                val_list = ImageWork.array_split_build_list_builder(split_guider)(value)

                path = value.save_path

                os.makedirs(path, exist_ok=True)

                for index in range(len(val_list)):
                    val = val_list[index]
                    val.save(os.path.join(path, f"{index}.png"))
            except Exception as info:
                return False, info
            else:
                return True, "successfully"

        return export

    """图像拉伸部分"""

    # image resize func
    @staticmethod
    def image_resize_main(img: Image.Image, type_is, value_w=0, value_h=0):
        data = GlobalData()
        if type_is == data.irt_default or type_is == data.irt_scale:
            if type_is == data.irt_default:
                scale = [16, 9]
            else:
                scale = [value_w, value_h]
            size = [0, 0]
            size_img = img.size
            wh = size_img[0] / size_img[1]
            sc = scale[0] / scale[1]

            if wh < sc:
                size[0] = round(size_img[1] / scale[1] * scale[0])
                size[1] = round(size_img[1])
            elif wh == sc:
                size = size_img

            else:
                size[1] = round(size_img[0] / scale[0] * scale[1])
                size[0] = round(size_img[0])

        else:
            size = [value_w, value_h]

        pic = img.resize(size)

        return pic

    @staticmethod
    def image_resize_view(value: PerResize, size, type_is, value_w=0, value_h=0):
        try:
            if value.is_need_work():
                img = ImageWork.p_ak_painting_main(value.mesh_path, value.tex_path)
            else:
                img = PIL.Image.open(value.tex_path)

            pic = ImageWork.image_resize_main(img, type_is, value_w, value_h)

            pic, size = ImageWork.g_transform_image(pic, size)

        except Exception as info:
            return False, info
        else:
            return True, pic

    @staticmethod
    def image_resize_export_builder(type_is, value_w=0, value_h=0):
        def export(value: PerResize):
            try:
                if value.is_need_work():
                    img = ImageWork.p_ak_painting_main(value.mesh_path, value.tex_path)
                else:
                    img = PIL.Image.open(value.tex_path)

                pic = ImageWork.image_resize_main(img, type_is, value_w, value_h)

                pic.save(value.save_path)

            except Exception as info:
                return False, info
            else:
                return True, "successfully"

        return export
