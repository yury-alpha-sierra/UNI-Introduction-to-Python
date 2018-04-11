# import wx
# import wx.lib.mixins.listctrl as listmix

# # musicdata = {
# # 0 : ("Bad English", "The Price Of Love", "Rock"),
# # 1 : ("DNA featuring Suzanne Vega", "Tom's Diner", "Rock"),
# # 2 : ("George Michael", "Praying For Time", "Rock"),
# # 3 : ("Gloria Estefan", "Here We Are", "Rock"),
# # 4 : ("Linda Ronstadt", "Don't Know Much", "Rock"),
# # 5 : ("Michael Bolton", "How Am I Supposed To Live Without You", "Blues"),
# # 6 : ("Paul Young", "Oh Girl", "Rock"),
# # }

# musicdata = [
# ["Bad English", "The Price Of Love", "Rock"],
# ["DNA featuring Suzanne Vega", "Tom's Diner", "Rock"],
# ["George Michael", "Praying For Time", "Rock"],
# ["Gloria Estefan", "Here We Are", "Rock"],
# ["Linda Ronstadt", "Don't Know Much", "Rock"],
# ["Michael Bolton", "How Am I Supposed To Live Without You", "Blues"],
# ["Paul Young", "Oh Girl", "Rock"],
# ]

# ########################################################################
# class TestListCtrl(wx.ListCtrl):

#     #----------------------------------------------------------------------
#     def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition,
#                  size=wx.DefaultSize, style=0):
#         wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

# ########################################################################
# class TestListCtrlPanel(wx.Panel, listmix.ColumnSorterMixin):

#     #----------------------------------------------------------------------
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

#         self.list_ctrl = TestListCtrl(self, size=(-1,100),
#                          style=wx.LC_REPORT
#                          |wx.BORDER_SUNKEN
#                          |wx.LC_SORT_ASCENDING
#                          )
#         self.list_ctrl.InsertColumn(0, "Artist")
#         self.list_ctrl.InsertColumn(1, "Title", wx.LIST_FORMAT_RIGHT)
#         self.list_ctrl.InsertColumn(2, "Genre")

#         # items = musicdata.items()
#         index = 0
#         for data in musicdata:                                                    # for key, data in musicdata:
#             self.list_ctrl.InsertItem(index, data[0])
#             self.list_ctrl.SetItem(index, 1, data[1])
#             self.list_ctrl.SetItem(index, 2, data[2])

#             # self.list_ctrl.SetItemData(index, key)
#             index += 1

#         # Now that the list exists we can init the other base class,
#         # see wx/lib/mixins/listctrl.py
#         self.itemDataMap = musicdata
#         listmix.ColumnSorterMixin.__init__(self, 3)
#         self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list_ctrl)

#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
#         self.SetSizer(sizer)

#     #----------------------------------------------------------------------
#     # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
#     def GetListCtrl(self):
#         return self.list_ctrl

#     #----------------------------------------------------------------------
#     def OnColClick(self, event):
#         print("column clicked")
#         event.Skip()

# ########################################################################
# class MyForm(wx.Frame):

#     #----------------------------------------------------------------------
#     def __init__(self):
#         wx.Frame.__init__(self, None, wx.ID_ANY, "List Control Tutorial")

#         # Add a panel so it looks the correct on all platforms
#         panel = TestListCtrlPanel(self)

# #----------------------------------------------------------------------
# # Run the program
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyForm()
#     frame.Show()
#     app.MainLoop()



# m = 0.
# print(isinstance(m, float))




# import re
# key_list = ('Up to 500g','Up to 1kg','Up to 1.5kg','Up to 2kg','Up to 3kg','Up to 5kg','Up to 10kg','Up to 15kg','Up to 20kg')
# weight_number_pattern = re.compile(r'\d{1,3}[.]?(\d{1,2})?')                 #r'\d{1,3}')
# weigh_unit_pattern = re.compile(r'kg')                                       # \d{1,3}(kg)')
# j = 0
# while j < len(key_list):
#     number_matches = re.findall(weight_number_pattern, key_list[j])
#     unit_matches = re.findall(weigh_unit_pattern, key_list[j])
#     j += 1



# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r'(\d+[\.]?\d?)'

test_str = ("'Up to 500g'\n"
	"Up to 1kg\n"
	"'Up to 1.5kg'\n"
	"Up to 2kg\n"
	"Up to 3kg\n"
	"Up to 5kg\n"
	"Up to 10kg\n"
	"Up to 15kg\n"
	"Up to 20kg\n"
	"From 30kg to 56kg")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))