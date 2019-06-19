import os

from PIL import Image

from core.src.structs_classes.basic_class import BasicInfo


class HandleSplitHolder(BasicInfo):
    def __init__(self):
        super(HandleSplitHolder, self).__init__("none", None)
        self.img: Image.Image = ...
        self.split_group = {}

    def load_img(self):
        if os.path.isfile(self.val):
            self.img = Image.open(self.val)

    def add_split_group(self, w=0, h=0, x=0, y=0, name=""):
        val = {"w": w, "h": h, "x": x, "y": y}
        self.split_group[name] = val

    def quick_split(self, x=0, y=0, h=0, w=0):
        val = self.img.crop([x, y, x + w, y+h])
        return val
