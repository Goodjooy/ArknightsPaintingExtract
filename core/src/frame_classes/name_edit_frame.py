from core.src.frame_classes.design_frame import MyDialogNames


class NameEditFrame(MyDialogNames):
    def __init__(self, parent):
        super(NameEditFrame, self).__init__(parent)
        self.parent = parent

        self.pattern = r"^(enemy|char|build_char|npc)_([0-9]{3,4})_(.+?)(?=$|_)_?(.+)?$"
