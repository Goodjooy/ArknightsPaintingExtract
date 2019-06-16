from core.src.frame_classes.design_frame import MyDialogSplit


class DefineSplit(MyDialogSplit):
    def __init__(self, parent, work_group):
        super(DefineSplit, self).__init__(parent)

        self.work_group = work_group
        self.frame = parent

    def initial(self, event):
        pass

    def use_image(self, event):
        pass

    def view_down(self, event):
        pass

    def view_up(self, event):
        pass

    def view_left(self, event):
        pass

    def view_right(self, event):
        pass

    def view_img(self, event):
        pass

    def resize(self, event):
        pass

    def show_init_img(self, event):
        pass

    def save_setting(self, event):
        pass

    def cancel_setting(self, event):
        pass

    def use_setting(self, event):
        pass

    def cut_img( self, event ):
        pass
