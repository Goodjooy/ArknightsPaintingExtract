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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Azur Lane Paintng Extract", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 512,288 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetMinSize( wx.Size( 325,-1 ) )
		self.m_panel1.SetMaxSize( wx.Size( 325,-1 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_filterChoices = [ u"全部", u"仅小人贴图集", u"仅NPC", u"仅敌人贴图集", u"仅干员初始立绘", u"仅干员精英化立绘", u"仅皮肤立绘" ]
		self.m_choice_filter = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_filterChoices, 0 )
		self.m_choice_filter.SetSelection( 0 )
		bSizer8.Add( self.m_choice_filter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		bSizer8.Add( self.m_searchCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

		self.m_treeCtrl_info = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer3.Add( self.m_treeCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_work = wx.Button( self.m_panel1, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_work, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_change = wx.Button( self.m_panel1, wx.ID_ANY, u"选择对应文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_change, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_setting = wx.Button( self.m_panel1, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_setting, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )

		self.m_gauge_state = wx.Gauge( self.m_panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_state.SetValue( 0 )
		bSizer4.Add( self.m_gauge_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer6.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer12 )
		self.m_scrolledWindow2.Layout()
		bSizer12.Fit( self.m_scrolledWindow2 )
		bSizer6.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


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
		self.m_choice_filter.Bind( wx.EVT_CHOICE, self.filter_work )
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.cancel_work )
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_work )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.search )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.search_work )
		self.m_treeCtrl_info.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_info_select )
		self.m_button_work.Bind( wx.EVT_BUTTON, self.work )
		self.m_button_change.Bind( wx.EVT_BUTTON, self.choice_file )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def resize( self, event ):
		event.Skip()

	def filter_work( self, event ):
		event.Skip()

	def cancel_work( self, event ):
		event.Skip()

	def search_work( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()


	def on_info_select( self, event ):
		event.Skip()

	def work( self, event ):
		event.Skip()

	def choice_file( self, event ):
		event.Skip()

	def setting( self, event ):
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

		self.m_colourPicker_view_color = wx.ColourPickerCtrl( self.m_panel3, wx.ID_ANY, wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_SHOW_LABEL )
		bSizer12.Add( self.m_colourPicker_view_color, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


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

	def apply_press( self, event ):
		event.Skip()

	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
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


