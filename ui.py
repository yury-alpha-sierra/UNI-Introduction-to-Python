"""[summary]
"""
import wx  # pylint: disable=E0611,W0401


class Ui(wx.Frame):      # pylint: disable=too-many-ancestors
    """[summary]

    """

    def __init__(self, name, parent, id, app):  # pylint: disable=W0622

        self.current_country = ""
        self.application = app

        wx.Frame.__init__(self, parent, id, name, size=(1000, 550))

        self.Bind(wx.EVT_CLOSE, self.close_window)

        self.my_panel = wx.Panel(self)

        self.status_bar = self.CreateStatusBar(
            4)     # pylint: disable=unused-variable
        self.status_bar.SetStatusWidths([100, 300, 200, 100])

        self.menu_bar = wx.MenuBar()
        self.my_menu = wx.Menu()

        self.my_menu.Append(
            wx.NewId(),
            "Service", "This will start new postal service transaction.")
        self.my_menu.Append(
            wx.NewId(),
            "Admin", "This will start admin functions.")

        self.menu_bar.Append(self.my_menu, "Function")

        self.my_weight_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.weight_label = wx.StaticText(
            self.my_panel, id=wx.ID_ANY,
            label="  Enter item weight:                ")
        self.my_weight_boxsizer.Add(
            self.weight_label, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL,
            border=15)
        self.weight_entry = wx.TextCtrl(self.my_panel)
        self.weight_entry.SetMaxLength(5)
        self.weight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)

        self.my_weight_boxsizer.Add(
            self.weight_entry, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        self.my_weigh_unit_selector = wx.RadioBox(
            self.my_panel, id=wx.ID_ANY, choices=["Kg", "gr"],
            majorDimension=2, style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)
        self.my_weigh_unit_selector.SetSelection(1)
        self.my_weight_boxsizer.Add(
            self.my_weigh_unit_selector, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

        self.my_country_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.country_label = wx.StaticText(
            self.my_panel, id=wx.ID_ANY, label="  Select destination country: ")
        self.my_country_boxsizer.Add(self.country_label, 0, border=30)
        self.country_choice = wx.Choice(
            self.my_panel, id=wx.ID_ANY, size=wx.DefaultSize,
            choices=list(self.application.country_and_zone_data.keys()),
            style=0)
        self.my_country_boxsizer.Add(self.country_choice, 0, border=3)

        self.my_item_list_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_item_list = wx.ListCtrl(
            self.my_panel, style=wx.LC_REPORT, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=[900, 200])
        self.my_item_list.AppendColumn('method', width=200)
        self.my_item_list.AppendColumn('price', width=100)

        self.my_item_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.double_click)

        self.my_item_list_boxsizer.Add(
            self.my_item_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.my_next_button = wx.Button(
            self.my_panel, label='next >>', pos=(430, 280))
        self.Bind(wx.EVT_BUTTON, self.next_button, self.my_next_button)

        self.my_add_button = wx.Button(
            self.my_panel, label='get options')
        self.Bind(wx.EVT_BUTTON, self.add_button, self.my_add_button)

        self.my_buttons_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_buttons_boxsizer.Add(
            self.my_add_button, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.my_buttons_boxsizer.Add(
            self.my_next_button, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.my_busket_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_busket_item_list = wx.ListCtrl(
            self.my_panel, style=wx.LC_REPORT, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=[900, 150])
        self.my_busket_item_list.AppendColumn('item no', width=80)
        self.my_busket_item_list.AppendColumn('type', width=100)
        self.my_busket_item_list.AppendColumn('method', width=100)
        self.my_busket_item_list.AppendColumn('weight', width=100)
        self.my_busket_item_list.AppendColumn('destination', width=250)
        self.my_busket_item_list.AppendColumn('quantity', width=100)
        self.my_busket_item_list.AppendColumn('cost', width=100)
        self.my_busket_item_list.AppendColumn('each', width=100)

        self.my_busket_boxsizer.Add(
            self.my_busket_item_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.my_user_input_boxsizer = wx.BoxSizer(wx.VERTICAL)
        self.my_user_input_boxsizer.Add(
            self.my_weight_boxsizer, 0, wx.ALIGN_TOP, border=3)
        self.my_user_input_boxsizer.Add(
            self.my_country_boxsizer, 0, wx.ALIGN_BOTTOM, border=3)
        self.my_user_input_boxsizer.Add(
            self.my_item_list_boxsizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, border=3)
        self.my_user_input_boxsizer.Add(
            self.my_busket_item_list, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, border=3)
        self.my_user_input_boxsizer.Add(
            self.my_buttons_boxsizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, border=3)

        self.my_panel.SetSizer(self.my_user_input_boxsizer)

        self.SetMenuBar(self.menu_bar)

    def double_click(self, event):  # pylint: disable=W0613
        """[summary]
        """
        index = self.my_item_list.GetFirstSelected()
        item_no = len(self.application.invoice) + 1
        to_basket = [str(item_no),'type','method','weight','destination','quantity','cost','each']
        # self.application.available_serice_price_options[index]
        self.application.invoice.append(to_basket)
        # print(self.application.invoice)
        self.my_item_list.DeleteAllItems()
        # print('item {0}, {1}'.format(l[0], l[1]))
        self.my_busket_item_list.DeleteAllItems()
        for each_item in self.application.invoice:
            self.my_busket_item_list.Append(each_item)

    def handle_keypress(self, event):
        """[summary]
        """
        keycode = event.GetKeyCode()
        if keycode < 255:  # valid ASCII
            # Valid alphanumeric character + backspace, left and right arrow
            if chr(keycode).isdigit() or keycode == 8 or keycode == 37 or keycode == 39:
                event.Skip()

    def next_button(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.my_panel.Hide()

    def add_button(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.current_country = self.country_choice.GetString(
            self.country_choice.GetSelection())
        self.application.country = self.current_country
        self.current_weight = self.weight_entry.GetValue()

        self.status_bar.SetStatusText(self.current_weight, 0)

        self.status_bar.SetStatusText(self.current_country, 1)
        if self.my_weigh_unit_selector.GetSelection() == 0:
            self.status_bar.SetStatusText('Kg', 2)
            multiplier = 1000
        else:
            self.status_bar.SetStatusText('gr', 2)
            multiplier = 1

        self.application.weight = float(self.current_weight) * float(multiplier)
        self.my_item_list.DeleteAllItems()
        self.application.available_serice_price_options.clear()
        self.application.available_serice_price_options = self.application.get_available_serice_price_options()
        for each_item in self.application.available_serice_price_options:
            self.my_item_list.Append(each_item)

    def close_window(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.Destroy()
