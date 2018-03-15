import wx


class MyApp(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,
                          "My firstg GUI app", size=(300, 200))


app = wx.PySimpleApp()
frame = MyApp(parent=None, id=-1)
frame.Show()
app.MainLoop()
