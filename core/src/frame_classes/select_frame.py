from core.src.frame_classes.design_frame import MyDialogSelect
from core.src.structs_classes.painting_work_structs.extract_structs import PerWorkList


class SelectionDialog(MyDialogSelect):
    def __init__(self, parent, items: PerWorkList):
        super(SelectionDialog, self).__init__(parent)
        self.items = items

        self.m_listBox_select_list.Set(self.items.build_view())

        self.indexes=[]

    def view_img( self, event ):
        pass

