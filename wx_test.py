"""[summary]

    Arguments:
        wx {[type]} -- [description]
"""

import wx


class MyApp(wx.Frame):      # pylint: disable=too-many-ancestors
    """[summary]

    Arguments:
        wx {[type]} -- [description]
    """

    def __init__(self, parent, id):                # pylint: disable=W0622

        wx.Frame.__init__(self, parent, id,
                          "My firstg GUI app", size=(300, 200))
        my_panel = wx.Panel(self)
        my_button = wx.Button(my_panel, label='exit',
                              pos=(130, 10), size=(60, 20))
        self.Bind(wx.EVT_BUTTON, self.close_button, my_button)
        self.Bind(wx.EVT_CLOSE, self.close_window)
        status_bar = self.CreateStatusBar()     # pylint: disable=unused-variable
        menu_bar = wx.MenuBar()
        first_menu = wx.Menu()
        second_menu = wx.Menu()
        first_menu.Append(wx.NewId(), "New Window", "This is a new window")
        first_menu.Append(wx.NewId(), "Open...", "This will open a new window")
        menu_bar.Append(first_menu, "File")
        menu_bar.Append(second_menu, "Edit")

        self.SetMenuBar(menu_bar)

    def close_button(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """


        self.Close(True)

    def close_window(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """

        self.Destroy()


MY_APP = wx.App()
FRAME = MyApp(parent=None, id=-1)
FRAME.Show()
MY_APP.MainLoop()
