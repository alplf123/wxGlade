#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade "faked test version"
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyMenuBar.__init__
        wx.MenuBar.__init__(self, *args, **kwds)
        wxglade_tmp_menu = wx.Menu()
        self.Append(wxglade_tmp_menu, "File")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyMenuBar.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyMenuBar.__do_layout
        pass
        # end wxGlade

# end of class MyMenuBar

class MyToolBar(wx.ToolBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyToolBar.__init__
        wx.ToolBar.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyToolBar.__set_properties
        self.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyToolBar.__do_layout
        pass
        # end wxGlade

# end of class MyToolBar

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "placeholder - every design\nneeds a toplevel window", style=wx.ALIGN_CENTER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.label_1, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((200, 200))
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
