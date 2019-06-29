# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Arknights Paintng Extract", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 512,288 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_work_type = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook_work_type.SetMinSize( wx.Size( 325,-1 ) )
		self.m_notebook_work_type.SetMaxSize( wx.Size( 325,-1 ) )

		self.m_panel_painting = wx.Panel( self.m_notebook_work_type, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_painting.SetMinSize( wx.Size( 325,-1 ) )
		self.m_panel_painting.SetMaxSize( wx.Size( 325,-1 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		m_p_choice_filterChoices = [ u"全部", u"仅小人贴图集", u"仅NPC", u"仅敌人贴图集", u"仅干员初始立绘", u"仅干员精英化立绘", u"仅皮肤立绘" ]
		self.m_p_choice_filter = wx.Choice( self.m_panel_painting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_p_choice_filterChoices, 0 )
		self.m_p_choice_filter.SetSelection( 0 )
		bSizer8.Add( self.m_p_choice_filter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_panel_painting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_p_searchCtrl_tree = wx.SearchCtrl( self.m_panel_painting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_p_searchCtrl_tree.ShowSearchButton( True )
		self.m_p_searchCtrl_tree.ShowCancelButton( True )
		bSizer8.Add( self.m_p_searchCtrl_tree, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

		self.m_p_treeCtrl_info = wx.TreeCtrl( self.m_panel_painting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer3.Add( self.m_p_treeCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_p_button_work = wx.Button( self.m_panel_painting, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_p_button_work, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel_painting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_p_button_change = wx.Button( self.m_panel_painting, wx.ID_ANY, u"选择对应文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_p_button_change, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel_painting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_p_button_setting = wx.Button( self.m_panel_painting, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_p_button_setting, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )


		self.m_panel_painting.SetSizer( bSizer3 )
		self.m_panel_painting.Layout()
		bSizer3.Fit( self.m_panel_painting )
		self.m_notebook_work_type.AddPage( self.m_panel_painting, u"立绘还原", True )
		self.m_panel5 = wx.Panel( self.m_notebook_work_type, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_a_searchCtrl_atlas = wx.SearchCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_a_searchCtrl_atlas.ShowSearchButton( True )
		self.m_a_searchCtrl_atlas.ShowCancelButton( True )
		bSizer27.Add( self.m_a_searchCtrl_atlas, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_a_treeCtrl_atlas = wx.TreeCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer27.Add( self.m_a_treeCtrl_atlas, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_a_button_updata = wx.Button( self.m_panel5, wx.ID_ANY, u"更新导入数据", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_a_button_updata, 0, wx.ALL, 5 )

		self.m_staticline26 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer30.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_a_button_change_atlas = wx.Button( self.m_panel5, wx.ID_ANY, u"更换匹配atlas", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_a_button_change_atlas, 0, wx.ALL, 5 )

		self.m_staticline27 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer30.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_a_button_export = wx.Button( self.m_panel5, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_a_button_export, 0, wx.ALL, 5 )


		bSizer27.Add( bSizer30, 0, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer27 )
		self.m_panel5.Layout()
		bSizer27.Fit( self.m_panel5 )
		self.m_notebook_work_type.AddPage( self.m_panel5, u"atlas切割", False )
		self.m_panel6 = wx.Panel( self.m_notebook_work_type, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer271 = wx.BoxSizer( wx.VERTICAL )

		self.m_ar_searchCtrl_array = wx.SearchCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_ar_searchCtrl_array.ShowSearchButton( True )
		self.m_ar_searchCtrl_array.ShowCancelButton( True )
		bSizer271.Add( self.m_ar_searchCtrl_array, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_ar_treeCtrl_array = wx.TreeCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer271.Add( self.m_ar_treeCtrl_array, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )

		m_ar_choice_typeChoices = [ u"<---*--->" ]
		self.m_ar_choice_type = wx.Choice( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ar_choice_typeChoices, 0 )
		self.m_ar_choice_type.SetSelection( 0 )
		bSizer301.Add( self.m_ar_choice_type, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline261 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer301.Add( self.m_staticline261, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bpButton9 = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		bSizer301.Add( self.m_bpButton9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline40 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer301.Add( self.m_staticline40, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bpButton10 = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		bSizer301.Add( self.m_bpButton10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline271 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer301.Add( self.m_staticline271, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_ar_button_export = wx.Button( self.m_panel6, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.m_ar_button_export, 0, wx.ALL, 5 )


		bSizer271.Add( bSizer301, 0, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer271 )
		self.m_panel6.Layout()
		bSizer271.Fit( self.m_panel6 )
		self.m_notebook_work_type.AddPage( self.m_panel6, u"阵列切割", False )
		self.m_panel7 = wx.Panel( self.m_notebook_work_type, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer272 = wx.BoxSizer( wx.VERTICAL )

		self.m_rs_searchCtrl_resize = wx.SearchCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_rs_searchCtrl_resize.ShowSearchButton( True )
		self.m_rs_searchCtrl_resize.ShowCancelButton( True )
		bSizer272.Add( self.m_rs_searchCtrl_resize, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_rs_treeCtrl_info = wx.TreeCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer272.Add( self.m_rs_treeCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer302 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_rs_bpButton_exoprt = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_rs_bpButton_exoprt.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer302.Add( self.m_rs_bpButton_exoprt, 0, wx.ALL, 5 )

		self.m_staticline42 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer302.Add( self.m_staticline42, 0, wx.EXPAND |wx.ALL, 5 )

		m_rs_choice_typeChoices = [ u"默认", u"比例", u"尺寸" ]
		self.m_rs_choice_type = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_rs_choice_typeChoices, 0 )
		self.m_rs_choice_type.SetSelection( 0 )
		bSizer302.Add( self.m_rs_choice_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline41 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer302.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_rs_textCtrl_wide = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_rs_textCtrl_wide.SetMinSize( wx.Size( 75,-1 ) )
		self.m_rs_textCtrl_wide.SetMaxSize( wx.Size( 75,-1 ) )

		bSizer40.Add( self.m_rs_textCtrl_wide, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_rs_staticText_type = wx.StaticText( self.m_panel7, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_rs_staticText_type.Wrap( -1 )

		self.m_rs_staticText_type.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "@Adobe 黑体 Std R" ) )

		bSizer40.Add( self.m_rs_staticText_type, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_rs_textCtrl_high = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_rs_textCtrl_high.SetMinSize( wx.Size( 75,-1 ) )
		self.m_rs_textCtrl_high.SetMaxSize( wx.Size( 75,-1 ) )

		bSizer40.Add( self.m_rs_textCtrl_high, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer302.Add( bSizer40, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer272.Add( bSizer302, 0, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer272 )
		self.m_panel7.Layout()
		bSizer272.Fit( self.m_panel7 )
		self.m_notebook_work_type.AddPage( self.m_panel7, u"图片拉伸", False )

		bSizer43.Add( self.m_notebook_work_type, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_gauge_state = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_state.SetValue( 0 )
		bSizer43.Add( self.m_gauge_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( bSizer43, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_simplebook1 = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel9 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_panel9, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel9.SetSizer( bSizer12 )
		self.m_panel9.Layout()
		bSizer12.Fit( self.m_panel9 )
		self.m_simplebook1.AddPage( self.m_panel9, u"a page", False )
		self.m_panel_text = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_info = wx.TextCtrl( self.m_panel_text, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_DONTWRAP|wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer41.Add( self.m_textCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_text.SetSizer( bSizer41 )
		self.m_panel_text.Layout()
		bSizer41.Fit( self.m_panel_text )
		self.m_simplebook1.AddPage( self.m_panel_text, u"a page", False )

		bSizer6.Add( self.m_simplebook1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer1.Add( self.m_staticText_info, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exit )
		self.Bind( wx.EVT_MOVE_END, self.resize )
		self.m_notebook_work_type.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.work_chage )
		self.m_p_choice_filter.Bind( wx.EVT_CHOICE, self.p_filter_work )
		self.m_p_searchCtrl_tree.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.p_cancel_work )
		self.m_p_searchCtrl_tree.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.p_search_work )
		self.m_p_searchCtrl_tree.Bind( wx.EVT_TEXT, self.p_search )
		self.m_p_searchCtrl_tree.Bind( wx.EVT_TEXT_ENTER, self.p_search_work )
		self.m_p_treeCtrl_info.Bind( wx.EVT_TREE_SEL_CHANGED, self.p_on_info_select )
		self.m_p_button_work.Bind( wx.EVT_BUTTON, self.p_work )
		self.m_p_button_change.Bind( wx.EVT_BUTTON, self.p_choice_file )
		self.m_p_button_setting.Bind( wx.EVT_BUTTON, self.p_setting )
		self.m_a_searchCtrl_atlas.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.a_cancel )
		self.m_a_searchCtrl_atlas.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.a_search )
		self.m_a_searchCtrl_atlas.Bind( wx.EVT_TEXT_ENTER, self.a_search )
		self.m_a_treeCtrl_atlas.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.a_re_split )
		self.m_a_treeCtrl_atlas.Bind( wx.EVT_TREE_SEL_CHANGED, self.a_tree_select )
		self.m_a_button_updata.Bind( wx.EVT_BUTTON, self.a_update_atlas )
		self.m_a_button_change_atlas.Bind( wx.EVT_BUTTON, self.a_change_atlas )
		self.m_a_button_export.Bind( wx.EVT_BUTTON, self.a_export )
		self.m_ar_searchCtrl_array.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.ar_cancel )
		self.m_ar_searchCtrl_array.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.ar_search )
		self.m_ar_searchCtrl_array.Bind( wx.EVT_TEXT_ENTER, self.ar_search )
		self.m_ar_treeCtrl_array.Bind( wx.EVT_TREE_SEL_CHANGED, self.ar_tree_select )
		self.m_ar_choice_type.Bind( wx.EVT_CHOICE, self.ar_type_change )
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.ar_new_spliter )
		self.m_bpButton10.Bind( wx.EVT_BUTTON, self.ar_remove_spliter )
		self.m_ar_button_export.Bind( wx.EVT_BUTTON, self.ar_export )
		self.m_rs_searchCtrl_resize.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.rs_cancel )
		self.m_rs_searchCtrl_resize.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.rs_search )
		self.m_rs_searchCtrl_resize.Bind( wx.EVT_TEXT_ENTER, self.rs_search )
		self.m_rs_treeCtrl_info.Bind( wx.EVT_TREE_SEL_CHANGED, self.rs_item_select )
		self.m_rs_bpButton_exoprt.Bind( wx.EVT_BUTTON, self.rs_export )
		self.m_rs_choice_type.Bind( wx.EVT_CHOICE, self.rs_type_select )
		self.m_rs_choice_type.Bind( wx.EVT_MOUSEWHEEL, self.rs_type_wheel )
		self.m_rs_textCtrl_wide.Bind( wx.EVT_MOUSEWHEEL, self.rs_wide_wheel )
		self.m_rs_textCtrl_wide.Bind( wx.EVT_TEXT, self.rs_wide_input )
		self.m_rs_textCtrl_high.Bind( wx.EVT_MOUSEWHEEL, self.rs_high_wheel )
		self.m_rs_textCtrl_high.Bind( wx.EVT_TEXT, self.rs_high_input )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def resize( self, event ):
		event.Skip()

	def work_chage( self, event ):
		event.Skip()

	def p_filter_work( self, event ):
		event.Skip()

	def p_cancel_work( self, event ):
		event.Skip()

	def p_search_work( self, event ):
		event.Skip()

	def p_search( self, event ):
		event.Skip()


	def p_on_info_select( self, event ):
		event.Skip()

	def p_work( self, event ):
		event.Skip()

	def p_choice_file( self, event ):
		event.Skip()

	def p_setting( self, event ):
		event.Skip()

	def a_cancel( self, event ):
		event.Skip()

	def a_search( self, event ):
		event.Skip()


	def a_re_split( self, event ):
		event.Skip()

	def a_tree_select( self, event ):
		event.Skip()

	def a_update_atlas( self, event ):
		event.Skip()

	def a_change_atlas( self, event ):
		event.Skip()

	def a_export( self, event ):
		event.Skip()

	def ar_cancel( self, event ):
		event.Skip()

	def ar_search( self, event ):
		event.Skip()


	def ar_tree_select( self, event ):
		event.Skip()

	def ar_type_change( self, event ):
		event.Skip()

	def ar_new_spliter( self, event ):
		event.Skip()

	def ar_remove_spliter( self, event ):
		event.Skip()

	def ar_export( self, event ):
		event.Skip()

	def rs_cancel( self, event ):
		event.Skip()

	def rs_search( self, event ):
		event.Skip()


	def rs_item_select( self, event ):
		event.Skip()

	def rs_export( self, event ):
		event.Skip()

	def rs_type_select( self, event ):
		event.Skip()

	def rs_type_wheel( self, event ):
		event.Skip()

	def rs_wide_wheel( self, event ):
		event.Skip()

	def rs_wide_input( self, event ):
		event.Skip()

	def rs_high_wheel( self, event ):
		event.Skip()

	def rs_high_input( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogSetting
###########################################################################

class MyDialogSetting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 512,512 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox_ex_cn = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"使用中文名作为导出文件名（如果可用）", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_ex_cn, 0, wx.ALL, 5 )

		self.m_checkBox_new_dir = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"在导出目标目录下新建导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_new_dir, 0, wx.ALL, 5 )

		self.m_staticline8 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_open_dir = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"完成后打开导出目标文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_open_dir.SetValue(True)
		bSizer10.Add( self.m_checkBox_open_dir, 0, wx.ALL, 5 )

		self.m_checkBox_skip_exist = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"跳过目标目录中已经存在的同名文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_skip_exist, 0, wx.ALL, 5 )

		self.m_checkBox_clear_list = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"导入时清空原有列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_clear_list, 0, wx.ALL, 5 )

		self.m_checkBox_finish_exit = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"完成任务后退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_finish_exit, 0, wx.ALL, 5 )

		self.m_checkBox_ex_copy = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"导出全部时同时拷贝不可还原", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_ex_copy, 0, wx.ALL, 5 )

		self.m_staticline10 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_regex_search = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"正则表达式筛选模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_regex_search, 0, wx.ALL, 5 )

		self.m_checkBox_inverse = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"搜索反选", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_inverse, 0, wx.ALL, 5 )

		self.m_checkBox_use_auto_search = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"使用自动搜索", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_use_auto_search.SetValue(True)
		bSizer10.Add( self.m_checkBox_use_auto_search, 0, wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer10 )
		self.m_panel2.Layout()
		bSizer10.Fit( self.m_panel2 )
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer9.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox_input_filterChoices = [ u"全部", u"仅小人贴图集", u"仅NPC", u"仅敌人贴图集", u"仅干员初始立绘", u"仅干员精英化立绘", u"仅皮肤立绘" ]
		self.m_radioBox_input_filter = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"导入文件筛选", wx.DefaultPosition, wx.DefaultSize, m_radioBox_input_filterChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_input_filter.SetSelection( 6 )
		bSizer11.Add( self.m_radioBox_input_filter, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline9 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_output_groupChoices = [ u"不分类", u"按干员名称分类", u"按立绘类型分类" ]
		self.m_radioBox_output_group = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"导出文件分类", wx.DefaultPosition, wx.DefaultSize, m_radioBox_output_groupChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_output_group.SetSelection( 0 )
		bSizer11.Add( self.m_radioBox_output_group, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_name_defind = wx.Button( self.m_panel3, wx.ID_ANY, u"打开导出名称设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button_name_defind, 0, wx.ALL, 5 )

		self.m_staticline13 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer12.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_handle = wx.Button( self.m_panel3, wx.ID_ANY, u"手动切割器", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button_handle, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer11 )
		self.m_panel3.Layout()
		bSizer11.Fit( self.m_panel3 )
		bSizer9.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer8.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.set_info )
		self.m_button_name_defind.Bind( wx.EVT_BUTTON, self.open_name_defined )
		self.m_button_handle.Bind( wx.EVT_BUTTON, self.handle_work )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.apply_press )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.cancel_press )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ok_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def set_info( self, event ):
		event.Skip()

	def open_name_defined( self, event ):
		event.Skip()

	def handle_work( self, event ):
		event.Skip()

	def apply_press( self, event ):
		event.Skip()

	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogSelect
###########################################################################

class MyDialogSelect ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"选择元素", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 600,400 ), wx.DefaultSize )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		m_listBox_select_listChoices = []
		self.m_listBox_select_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_select_listChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_SORT )
		self.m_listBox_select_list.SetMinSize( wx.Size( 250,-1 ) )
		self.m_listBox_select_list.SetMaxSize( wx.Size( 250,-1 ) )

		bSizer40.Add( self.m_listBox_select_list, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer40.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap_view = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_bitmap_view, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer39.Add( bSizer40, 1, wx.EXPAND, 5 )

		self.m_staticline34 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer39.Add( self.m_staticText_info, 0, wx.ALL, 5 )

		self.m_staticline35 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		bSizer39.Add( m_sdbSizer4, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer39 )
		self.Layout()
		bSizer39.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.cancel_press )
		self.m_sdbSizer4OK.Bind( wx.EVT_BUTTON, self.ok_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogSplit
###########################################################################

class MyDialogSplit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"阵列切割设置", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_view = wx.StaticBitmap( self.m_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_bitmap_view, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer37 )
		self.m_scrolledWindow3.Layout()
		bSizer37.Fit( self.m_scrolledWindow3 )
		bSizer36.Add( self.m_scrolledWindow3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline35 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer36.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"阵列切割宽", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer40.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl_split_wide = wx.TextCtrl( self, wx.ID_ANY, u"182", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl_split_wide, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"阵列切割高", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer40.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl_split_high = wx.TextCtrl( self, wx.ID_ANY, u"182", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl_split_high, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"内含尺寸", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer40.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl_inside_size = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrl_inside_size, 0, wx.ALL, 5 )


		bSizer39.Add( bSizer40, 0, wx.EXPAND, 5 )

		self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer39.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"预切割预览", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer41.Add( self.m_staticText19, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 3, 3, 0, 0 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_bpButton_up = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_bpButton_up, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer1.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_bpButton_left = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_left.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_bpButton_left, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton_cut = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_cut.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_CUT, wx.ART_BUTTON ) )
		gSizer1.Add( self.m_bpButton_cut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton_right = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_right.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_bpButton_right, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer1.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_bpButton_down = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_bpButton_down, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer1.Add( self.m_staticText18, 0, wx.ALL, 5 )


		bSizer41.Add( gSizer1, 0, 0, 5 )

		self.m_staticline37 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer41.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"显示原始图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button19, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer39.Add( bSizer41, 0, wx.EXPAND, 5 )


		bSizer38.Add( bSizer39, 0, wx.EXPAND, 5 )

		self.m_staticline40 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer38.Add( self.m_staticline40, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_img_listChoices = []
		self.m_listBox_img_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_img_listChoices, 0 )
		bSizer42.Add( self.m_listBox_img_list, 1, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_staticline41 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_slider_scale = wx.Slider( self, wx.ID_ANY, 1, 1, 8, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_MIN_MAX_LABELS|wx.SL_SELRANGE )
		bSizer42.Add( self.m_slider_scale, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer38.Add( bSizer42, 1, wx.EXPAND, 5 )


		bSizer36.Add( bSizer38, 0, wx.EXPAND, 5 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )

		self.m_staticline39 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer35.Add( self.m_staticline39, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer35.Add( self.m_staticText_info, 0, wx.ALL, 5 )

		self.m_staticline38 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer35.Add( self.m_staticline38, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Save )
		self.m_sdbSizer5Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Apply )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		bSizer35.Add( m_sdbSizer5, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.initial )
		self.m_bpButton_up.Bind( wx.EVT_BUTTON, self.view_up )
		self.m_bpButton_left.Bind( wx.EVT_BUTTON, self.view_left )
		self.m_bpButton_cut.Bind( wx.EVT_BUTTON, self.cut_img )
		self.m_bpButton_right.Bind( wx.EVT_BUTTON, self.view_right )
		self.m_bpButton_down.Bind( wx.EVT_BUTTON, self.view_down )
		self.m_button19.Bind( wx.EVT_BUTTON, self.show_init_img )
		self.m_listBox_img_list.Bind( wx.EVT_LISTBOX, self.view_img )
		self.m_listBox_img_list.Bind( wx.EVT_LISTBOX_DCLICK, self.use_image )
		self.m_slider_scale.Bind( wx.EVT_SCROLL_CHANGED, self.resize )
		self.m_sdbSizer5Apply.Bind( wx.EVT_BUTTON, self.use_setting )
		self.m_sdbSizer5Cancel.Bind( wx.EVT_BUTTON, self.cancel_setting )
		self.m_sdbSizer5Save.Bind( wx.EVT_BUTTON, self.save_setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def initial( self, event ):
		event.Skip()

	def view_up( self, event ):
		event.Skip()

	def view_left( self, event ):
		event.Skip()

	def cut_img( self, event ):
		event.Skip()

	def view_right( self, event ):
		event.Skip()

	def view_down( self, event ):
		event.Skip()

	def show_init_img( self, event ):
		event.Skip()

	def view_img( self, event ):
		event.Skip()

	def use_image( self, event ):
		event.Skip()

	def resize( self, event ):
		event.Skip()

	def use_setting( self, event ):
		event.Skip()

	def cancel_setting( self, event ):
		event.Skip()

	def save_setting( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogNames
###########################################################################

class MyDialogNames ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"导出名称设置", pos = wx.DefaultPosition, size = wx.Size( 692,603 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText112 = wx.StaticText( self, wx.ID_ANY, u"^(enemy|char|build_char|npc)_([0-9]{3,4})_(.+?)_?(.+)?$", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		bSizer13.Add( self.m_staticText112, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_searchCtrl_names = wx.SearchCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		self.m_searchCtrl_names.ShowSearchButton( True )
		self.m_searchCtrl_names.ShowCancelButton( True )
		bSizer21.Add( self.m_searchCtrl_names, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline22 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bpButton_add_item = wx.BitmapButton( self.m_panel4, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_add_item.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		bSizer21.Add( self.m_bpButton_add_item, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton_del_item = wx.BitmapButton( self.m_panel4, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_del_item.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		bSizer21.Add( self.m_bpButton_del_item, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( bSizer21, 0, wx.EXPAND, 5 )

		self.m_treeCtrl_info_item = wx.TreeCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer14.Add( self.m_treeCtrl_info_item, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer14 )
		self.m_panel4.Layout()
		bSizer14.Fit( self.m_panel4 )
		bSizer16.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer16.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_scrolledWindow_work = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_work.SetScrollRate( 5, 5 )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline24 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"名称设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer17.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_button_set_size = wx.Button( self.m_scrolledWindow_work, wx.ID_ANY, u"设置标识尺寸", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button_set_size, 0, wx.ALL, 5 )

		self.m_staticline23 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_name_key = wx.Button( self.m_scrolledWindow_work, wx.ID_ANY, u"设置名称标识符", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_button_name_key, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"名称对应中文名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer19.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl_name = wx.TextCtrl( self.m_scrolledWindow_work, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_textCtrl_name, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )

		self.m_staticline16 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer201 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_skin_key = wx.Button( self.m_scrolledWindow_work, wx.ID_ANY, u"设置皮肤/精英化标识符", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_button_skin_key, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"皮肤/精英化名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer201.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl_skin = wx.TextCtrl( self.m_scrolledWindow_work, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_textCtrl_skin, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer201, 1, wx.EXPAND, 5 )

		self.m_staticline21 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_ex_key = wx.Button( self.m_scrolledWindow_work, wx.ID_ANY, u"设置前缀标识符", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_button_ex_key, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"前缀捕获名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer211.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl_ex = wx.TextCtrl( self.m_scrolledWindow_work, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl_ex, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer211, 1, wx.EXPAND, 5 )

		self.m_staticline20 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline20, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer2111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_count_key = wx.Button( self.m_scrolledWindow_work, wx.ID_ANY, u"设置编号标识符", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2111.Add( self.m_button_count_key, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"编号捕获名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		bSizer2111.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl_count = wx.TextCtrl( self.m_scrolledWindow_work, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2111.Add( self.m_textCtrl_count, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer2111, 1, wx.EXPAND, 5 )

		self.m_staticline221 = wx.StaticLine( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline221, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow_work, wx.ID_ANY, u"格式化形式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer17.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl_format = wx.TextCtrl( self.m_scrolledWindow_work, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_textCtrl_format, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton_add_format = wx.BitmapButton( self.m_scrolledWindow_work, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_add_format.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		bSizer20.Add( self.m_bpButton_add_format, 0, wx.ALL, 5 )

		self.m_bpButton_del_format = wx.BitmapButton( self.m_scrolledWindow_work, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_del_format.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		bSizer20.Add( self.m_bpButton_del_format, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer20, 0, wx.ALIGN_RIGHT, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_scrolledWindow_work, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_ALWAYS_SB )
		bSizer17.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4Save = wx.Button( self.m_scrolledWindow_work, wx.ID_SAVE )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Save )
		self.m_sdbSizer4Cancel = wx.Button( self.m_scrolledWindow_work, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		bSizer17.Add( m_sdbSizer4, 0, wx.ALIGN_RIGHT, 5 )


		self.m_scrolledWindow_work.SetSizer( bSizer17 )
		self.m_scrolledWindow_work.Layout()
		bSizer17.Fit( self.m_scrolledWindow_work )
		bSizer16.Add( self.m_scrolledWindow_work, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )

		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Apply )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer13.Add( m_sdbSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_searchCtrl_names.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search )
		self.m_searchCtrl_names.Bind( wx.EVT_TEXT_ENTER, self.search )
		self.m_bpButton_add_item.Bind( wx.EVT_BUTTON, self.item_add )
		self.m_bpButton_del_item.Bind( wx.EVT_BUTTON, self.item_del )
		self.m_treeCtrl_info_item.Bind( wx.EVT_TREE_SEL_CHANGED, self.select_item )
		self.m_button_name_key.Bind( wx.EVT_BUTTON, self.set_name_key )
		self.m_button_skin_key.Bind( wx.EVT_BUTTON, self.set_skin_key )
		self.m_button_ex_key.Bind( wx.EVT_BUTTON, self.srt_ex_key )
		self.m_button_count_key.Bind( wx.EVT_BUTTON, self.set_count_key )
		self.m_bpButton_add_format.Bind( wx.EVT_BUTTON, self.add_format )
		self.m_bpButton_del_format.Bind( wx.EVT_BUTTON, self.del_format )
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.cancel_change )
		self.m_sdbSizer4Save.Bind( wx.EVT_BUTTON, self.save_change )
		self.m_sdbSizer2Apply.Bind( wx.EVT_BUTTON, self.apply_press )
		self.m_sdbSizer2Cancel.Bind( wx.EVT_BUTTON, self.cancel_press )
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.ok_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def search( self, event ):
		event.Skip()


	def item_add( self, event ):
		event.Skip()

	def item_del( self, event ):
		event.Skip()

	def select_item( self, event ):
		event.Skip()

	def set_name_key( self, event ):
		event.Skip()

	def set_skin_key( self, event ):
		event.Skip()

	def srt_ex_key( self, event ):
		event.Skip()

	def set_count_key( self, event ):
		event.Skip()

	def add_format( self, event ):
		event.Skip()

	def del_format( self, event ):
		event.Skip()

	def cancel_change( self, event ):
		event.Skip()

	def save_change( self, event ):
		event.Skip()

	def apply_press( self, event ):
		event.Skip()

	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogHandleSplit
###########################################################################

class MyDialogHandleSplit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"手动切割", pos = wx.DefaultPosition, size = wx.Size( 982,569 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_view_img = wx.StaticBitmap( self.m_scrolledWindow3, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer48.Add( self.m_bitmap_view_img, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer48 )
		self.m_scrolledWindow3.Layout()
		bSizer48.Fit( self.m_scrolledWindow3 )
		bSizer43.Add( self.m_scrolledWindow3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline42 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer43.Add( self.m_staticline42, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		bSizer45.SetMinSize( wx.Size( 300,-1 ) )
		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"左下角水平坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer46.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl_left = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_textCtrl_left.SetMinSize( wx.Size( 0,-1 ) )

		bSizer46.Add( self.m_textCtrl_left, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"左下角竖直坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer46.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl_botton = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer46.Add( self.m_textCtrl_botton, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"切割宽度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer46.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl_wieth = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer46.Add( self.m_textCtrl_wieth, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"切割高度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer46.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl_height = wx.TextCtrl( self, wx.ID_ANY, u"124", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		bSizer46.Add( self.m_textCtrl_height, 0, wx.ALL, 5 )


		bSizer47.Add( bSizer46, 0, wx.EXPAND, 5 )

		self.m_staticline44 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer47.Add( self.m_staticline44, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		bSizer501 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton13 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton13.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		bSizer501.Add( self.m_bpButton13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton14 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton14.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		bSizer501.Add( self.m_bpButton14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_bpButton15 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton15.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer501.Add( self.m_bpButton15, 0, wx.ALL, 5 )


		bSizer49.Add( bSizer501, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		bSizer49.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer47.Add( bSizer49, 1, wx.EXPAND, 5 )


		bSizer45.Add( bSizer47, 1, wx.EXPAND, 5 )

		self.m_staticline43 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer45.Add( self.m_staticline43, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap_region = wx.StaticBitmap( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_bitmap_region, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer43.Add( bSizer45, 0, wx.EXPAND, 5 )


		bSizer42.Add( bSizer43, 1, wx.EXPAND, 5 )

		self.m_staticline48 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline48, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"Crayonkun可是公共肉便器呢", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_END )
		self.m_staticText_info.Wrap( -1 )

		bSizer50.Add( self.m_staticText_info, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_gauge_val = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_val.SetValue( 0 )
		bSizer50.Add( self.m_gauge_val, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline46 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer50.Add( self.m_staticline46, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"步长", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer50.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox_stepChoices = [ u"1", u"25", u"500" ]
		self.m_comboBox_step = wx.ComboBox( self, wx.ID_ANY, u"124", wx.DefaultPosition, wx.DefaultSize, m_comboBox_stepChoices, wx.CB_DROPDOWN )
		self.m_comboBox_step.SetSelection( 1 )
		self.m_comboBox_step.SetMinSize( wx.Size( 100,-1 ) )
		self.m_comboBox_step.SetMaxSize( wx.Size( 100,-1 ) )

		bSizer50.Add( self.m_comboBox_step, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer42.Add( bSizer50, 0, wx.EXPAND, 5 )

		self.m_staticline49 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline49, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer_save = wx.StdDialogButtonSizer()
		self.m_sdbSizer_saveSave = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer_save.AddButton( self.m_sdbSizer_saveSave )
		m_sdbSizer_save.Realize();

		bSizer42.Add( m_sdbSizer_save, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer42 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl_left.Bind( wx.EVT_MOUSEWHEEL, self.wheel_x )
		self.m_textCtrl_left.Bind( wx.EVT_TEXT, self.enter_x )
		self.m_textCtrl_botton.Bind( wx.EVT_MOUSEWHEEL, self.wheel_y )
		self.m_textCtrl_botton.Bind( wx.EVT_TEXT, self.enter_y )
		self.m_textCtrl_wieth.Bind( wx.EVT_MOUSEWHEEL, self.wheel_w )
		self.m_textCtrl_wieth.Bind( wx.EVT_TEXT, self.enter_width )
		self.m_textCtrl_height.Bind( wx.EVT_MOUSEWHEEL, self.wheel_h )
		self.m_textCtrl_height.Bind( wx.EVT_TEXT, self.enter_height )
		self.m_bpButton13.Bind( wx.EVT_BUTTON, self.add_region )
		self.m_bpButton14.Bind( wx.EVT_BUTTON, self.del_region )
		self.m_bpButton15.Bind( wx.EVT_BUTTON, self.save )
		self.m_listBox4.Bind( wx.EVT_LISTBOX, self.select_region )
		self.m_bitmap_region.Bind( wx.EVT_LEFT_DCLICK, self.view_in_main )
		self.m_bitmap_region.Bind( wx.EVT_MOUSEWHEEL, self.wheel_region )
		self.m_comboBox_step.Bind( wx.EVT_MOUSEWHEEL, self.step_wheel )
		self.m_comboBox_step.Bind( wx.EVT_TEXT, self.step_len )
		self.m_sdbSizer_saveSave.Bind( wx.EVT_BUTTON, self.save_exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def wheel_x( self, event ):
		event.Skip()

	def enter_x( self, event ):
		event.Skip()

	def wheel_y( self, event ):
		event.Skip()

	def enter_y( self, event ):
		event.Skip()

	def wheel_w( self, event ):
		event.Skip()

	def enter_width( self, event ):
		event.Skip()

	def wheel_h( self, event ):
		event.Skip()

	def enter_height( self, event ):
		event.Skip()

	def add_region( self, event ):
		event.Skip()

	def del_region( self, event ):
		event.Skip()

	def save( self, event ):
		event.Skip()

	def select_region( self, event ):
		event.Skip()

	def view_in_main( self, event ):
		event.Skip()

	def wheel_region( self, event ):
		event.Skip()

	def step_wheel( self, event ):
		event.Skip()

	def step_len( self, event ):
		event.Skip()

	def save_exit( self, event ):
		event.Skip()


