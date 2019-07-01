#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import operator
from collections import deque
from io import StringIO
from optparse import OptionParser

from PIL import Image

logging.basicConfig()
log = logging.getLogger('png2svg')


def add_tuple(a, b):
    return tuple(map(operator.add, a, b))


def sub_tuple(a, b):
    return tuple(map(operator.sub, a, b))


def neg_tuple(a):
    return tuple(map(operator.neg, a))


def direction(edge):
    return sub_tuple(edge[1], edge[0])


def magnitude(a):
    return int(pow(pow(a[0], 2) + pow(a[1], 2), .5))


def normalize(a):
    mag = magnitude(a)
    assert mag > 0, "Cannot normalize a zero-length vector"
    return tuple(map(operator.truediv, a, [mag] * len(a)))


def svg_header(width, height):
    return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%d" height="%d"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
""" % (width, height)


def rgba_image_to_svg_pixels(im, opaque=None):
    s = StringIO()
    s.write(svg_header(*im.size))

    width, height = im.size
    for x in range(width):
        for y in range(height):
            here = (x, y)
            rgba = im.getpixel(here)
            if opaque and not rgba[3]:
                continue
            s.write(
                """<rect x="%d" y="%d" width="1" height="1" style="fill:rgb%s; fill-opacity:%.3f; stroke:none;" 
                />\n""" % (
                    x, y, rgba[0:3], float(rgba[3]) / 255))
    s.write("""</svg>\n""")
    return s.getvalue()


def joined_edges(assorted_edges, keep_every_point=False):
    pieces = []
    piece = []
    directions = deque([
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ])
    while assorted_edges:
        if not piece:
            piece.append(assorted_edges.pop())
        current_direction = normalize(direction(piece[-1]))
        while current_direction != directions[2]:
            directions.rotate(-1)
        for i in range(1, 4):
            next_end = add_tuple(piece[-1][1], directions[i])
            next_edge = (piece[-1][1], next_end)
            if next_edge in assorted_edges:
                assorted_edges.remove(next_edge)
                if i == 2 and not keep_every_point:
                    # same direction
                    piece[-1] = (piece[-1][0], next_edge[1])
                else:
                    piece.append(next_edge)
                if piece[0][0] == piece[-1][1]:
                    if not keep_every_point and normalize(direction(piece[0])) == normalize(direction(piece[-1])):
                        piece[-1] = (piece[-1][0], piece.pop(0)[1])
                        # same direction
                    pieces.append(piece)
                    piece = []
                break
        else:
            raise Exception("Failed to find connecting edge")
    return pieces


def rgba_image_to_svg_contiguous(im, opaque=None, keep_every_point=False):
    # collect contiguous pixel groups

    adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = Image.new("1", im.size, 0)

    color_pixel_lists = {}

    width, height = im.size
    for x in range(width):
        for y in range(height):
            here = (x, y)
            if visited.getpixel(here):
                continue
            rgba = im.getpixel((x, y))
            if opaque and not rgba[3]:
                continue


if __name__ == '__main__':
    img = Image.open(r"D:\Users\qz228\Desktop\明日方舟-导出\明日方舟-导出\build_char_002_amiya\F_L_Hand.png")
    val = rgba_image_to_svg_pixels(img)
    print(val)
    with open(r"D:\Users\qz228\Desktop\aaa.svg", 'w')as file:
        file.write(val)
