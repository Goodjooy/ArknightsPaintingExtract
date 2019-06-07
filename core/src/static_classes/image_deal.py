import os
from functools import reduce

import PIL.Image
from re import match, split

import numpy

from core.src.structs_classes.extract_structs import PerInfo


class ImageWork(object):
    @staticmethod
    def cut_pic_builder(size):
        """
        :param size: the input img size(wide,high)
        :return: a callable func
        """

        def cut_pic(info):
            a = [round(float(info[1]) * size[0]), round((1 - float(info[2])) * size[1])]

            return a

        return cut_pic

    @staticmethod
    def draw(pic, pos):
        pic.paste(pos[0], pos[1])
        return pic

    @staticmethod
    def division_builder(val1, val2, pic):
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

        tex_cuter = ImageWork.cut_pic_builder(size)

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

        division = ImageWork.division_builder(list(draw_pic), list(tex_pos), img)

        restore = (map(division, print_pos))

        pic_out = reduce(ImageWork.draw, restore, pic)

        return pic_out

    @staticmethod
    def deal_mrfz(alpha_path, tex_path):
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
    def restore_tool(now_info: PerInfo):
        """拼图用的函数
        """
        try:
            pic = ImageWork.deal_mrfz(now_info.mesh_path, now_info.tex_path)

            pic.save(now_info.save_path)
        except RuntimeError as info:
            return False, str(info)
        except ValueError as info:
            return False, "math" + str(info)
        except AssertionError as info:
            return False, "尺寸匹配错误"
        else:
            return True, "成功还原：%s" % now_info.cn_name

    @staticmethod
    def restore_tool_one(mesh_path, pic_path, save_as, ):
        """拼图用的函数"""

        pic = ImageWork.deal_mrfz(mesh_path, pic_path)

        assert isinstance(save_as, str)
        pic.save(save_as)

    @staticmethod
    def restore_tool_no_save(mesh_path, pic_path, size: tuple):
        """拼图用的函数"""
        pic = ImageWork.deal_mrfz(mesh_path, pic_path)
        pic_size = pic.size
        bg = PIL.Image.new("RGBA", size, (255, 255, 255, 0))

        scale = min(bg.size[0] / pic.size[0], bg.size[1] / pic.size[1])
        size = (round(pic.size[0] * scale), round(pic.size[1] * scale))

        pic = pic.resize(size, PIL.Image.ANTIALIAS)
        x = round(bg.size[0] / 2 - pic.size[0] / 2)
        y = round(bg.size[1] / 2 - pic.size[1] / 2)
        bg.paste(pic, (x, y, x + pic.size[0], y + pic.size[1]))
        return bg, pic_size

    @staticmethod
    def pic_transform(path, size):
        pic = PIL.Image.open(path)
        pic_size = pic.size
        bg = PIL.Image.new("RGBA", size, (255, 255, 255, 0))

        scale = min(bg.size[0] / pic.size[0], bg.size[1] / pic.size[1])
        size = (round(pic.size[0] * scale), round(pic.size[1] * scale))

        pic = pic.resize(size, PIL.Image.ANTIALIAS)
        x = round(bg.size[0] / 2 - pic.size[0] / 2)
        y = round(bg.size[1] / 2 - pic.size[1] / 2)
        bg.paste(pic, (x, y, x + pic.size[0], y + pic.size[1]))
        return bg, pic_size
