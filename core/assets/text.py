import os
import re
from tkinter.messagebox import showinfo

from core.src.static_classes.image_deal import ImageWork

#showinfo("lala", "lala")

from core.src.structs_classes.atlas_structs import PerAtlas

if __name__ == '__main__' and False:
    size_w = 182
    approve = 0
    path = "D:\\Users\\qz228\\Desktop\\明日方舟-导出"

    save = "text_use"

    import PIL.Image

    img = PIL.Image.open(os.path.join(path, "SpriteAtlasTexture-CHARACTER_AVATAR-2048x2048-fmt34.png"))
    img: PIL.Image
    size = img.size
    img_list = []
    for val_x in range(1, 12):
        for val_y in range(1, 12):
            value = img.crop(
                [(val_x - 1) * size_w + approve,
                 size[1] - val_y * size_w - approve,
                 val_x * size_w + approve,
                 size[1] - (val_y - 1) * size_w - approve
                 ])
            value = value.crop([1, 1, 181, 181])
            img_list.append(value)
            value.save(f"{save}\\{val_x}+{val_y}.png")

if __name__ == '__main__' and False:
    B = re.compile(r'{(\d+)}')
    string = "{1}char_285_medic2{0}{1}{1}"

    A = B.findall(string)
    print(A)
    print(type(A))

if __name__ == '__main__':
    import PIL.Image
    img=PIL.Image.open("img.jpg")
    val = ImageWork.image_resize_main(img,1,1,2)
    val.show()
