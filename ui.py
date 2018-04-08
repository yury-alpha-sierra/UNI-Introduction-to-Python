"""[summary]
"""
import re
import wx  # pylint: disable=E0611,W0401


class Ui(wx.Frame):  # pylint: disable=too-many-ancestors
    """[summary]
    """

    def __init__(self, name, parent, id, app):  # pylint: disable=W0622

        self.application = app
        self.delete_or_modify = False

        wx.Frame.__init__(self, parent, id, name, style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX), size=(1000, 600))
        self.Bind(wx.EVT_CLOSE, self.__my_frame_handle_EVT_CLOSE)

        self.my_font = wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'sans-serif')

        self.my_service_panel = wx.Panel(self)
        self.my_admin_panel = wx.Panel(self)
        self.my_info_panel = wx.Panel(self)

        self.my_menu_bar = wx.MenuBar()
        self.my_menu = wx.Menu()

        self.menu_item_exit = self.my_menu.Append(wx.NewId(), "Exit", "Terminate application.")
        self.menu_item_exit.SetFont(self.my_font)
        self.Bind(wx.EVT_MENU, self.__my_frame_handle_EVT_CLOSE, self.menu_item_exit)

        self.my_menu_bar.Append(self.my_menu, "Function Selector")
        self.my_menu_bar.SetFont(self.my_font)
        self.SetMenuBar(self.my_menu_bar)

        self.my_service_panel.Hide()
        self.my_admin_panel.Hide()

        self.my_panel_boxsizer = wx.BoxSizer(wx.VERTICAL)
        self.my_panel_boxsizer.Add(self.my_service_panel, 1, wx.ALL | wx.EXPAND, border=3)
        self.my_panel_boxsizer.Add(self.my_admin_panel, 1, wx.ALL | wx.EXPAND, border=3)
        self.my_panel_boxsizer.Add(self.my_info_panel, 1, wx.ALL | wx.EXPAND, border=3)

        self.__init_admin_panel()
        self.__init_service_panel()
        self.__init_info_panel()

    def __init_info_panel(self):

        self.my_info_boxsizer = wx.BoxSizer(wx.HORIZONTAL)  # | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL
        my_info_text = wx.StaticText(self.my_info_panel, -1, style=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        my_message = 'this is an introductory message\n to finctionality of the postal service\n application'
        my_info_text.SetLabel(my_message)

        self.my_info_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_info_panel.SetBackgroundColour(self.my_info_panel_colour)

        my_info_font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'sans-serif')
        my_info_text.SetFont(my_info_font)

    def __init_admin_panel(self):

        self.menu_item_admin = self.my_menu.Prepend(wx.NewId(), "Admin", "Start admin functions.")
        self.Bind(wx.EVT_MENU, self.__my_menu_handle_Admin_Option, self.menu_item_admin)

        self.my_admin_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_admin_panel.SetBackgroundColour(self.my_admin_panel_colour)

    def __init_service_panel(self):
        """[summary]
        """

        self.menu_item_service = self.my_menu.Prepend(wx.NewId(), "Service", "Start new postal service transaction.")
        self.Bind(wx.EVT_MENU, self.__my_menu_handle_Service_Option, self.menu_item_service)

        self.my_service_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_service_panel.SetBackgroundColour(self.my_service_panel_colour)

        self.my_status_bar = self.CreateStatusBar(4)  # pylint: disable=unused-variable
        self.my_status_bar.SetStatusWidths([200, 300, 200, 100])

        self.my_weight_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_weight_label = wx.StaticText(self.my_service_panel, id=wx.ID_ANY, label="  Enter item weight:")
        self.my_weight_label.SetFont(self.my_font)
        self.my_weight_boxsizer.Add(self.my_weight_label, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, border=15)
        self.my_weight_boxsizer.AddSpacer(20)
        self.my_weight_entry = wx.TextCtrl(self.my_service_panel, size=(85, 30))
        self.my_weight_entry.SetFont(self.my_font)
        self.my_weight_entry.SetMaxLength(7)
        self.my_weight_entry.Bind(wx.EVT_CHAR, self.__my_weight_entry_handle_EVT_CHAR)
        self.my_weight_entry.Bind(wx.EVT_TEXT, self.__weight_entry_handle_EVT_CHOICE)
        self.my_weight_boxsizer.Add(self.my_weight_entry, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        self.my_weigh_unit_selector = wx.RadioBox(self.my_service_panel, id=wx.ID_ANY, choices=["Kg", "gr"], majorDimension=2, style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)
        self.my_weight_boxsizer.AddSpacer(15)
        self.my_weigh_unit_selector.SetFont(self.my_font)
        self.my_weigh_unit_selector.Bind(wx.EVT_RADIOBOX, self.__my_weigh_unit_selector_handle_EVT_RADIOBOX)

        self.my_weigh_unit_selector.SetSelection(1)
        self.my_weight_boxsizer.Add(self.my_weigh_unit_selector, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

        self.my_country_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_country_label = wx.StaticText(self.my_service_panel, id=wx.ID_ANY, label="  Select destination country: ")
        self.my_country_label.SetFont(self.my_font)
        self.my_country_boxsizer.Add(self.my_country_label, 0, border=30)
        self.my_country_choice = wx.Choice(self.my_service_panel, id=wx.ID_ANY, size=wx.DefaultSize, choices=list(self.application.country_and_zone_data.keys()), style=0)
        self.my_country_choice.SetFont(self.my_font)
        self.my_country_choice.Bind(wx.EVT_CHOICE, self.__country_choice_handle_EVT_CHOICE)
        self.my_country_boxsizer.Add(self.my_country_choice, 0, border=3)

        self.my_item_list_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_item_list = wx.ListCtrl(self.my_service_panel, style=wx.LC_REPORT, id=wx.ID_ANY, pos=wx.DefaultPosition, size=[900, 200])
        self.my_item_list.AppendColumn('method', width=230)
        self.my_item_list.AppendColumn('price', width=100)
        self.my_item_list.SetFont(self.my_font)
        self.my_item_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.__my_item_list_handle_EVT_LIST_ITEM_ACTIVATED)
        self.my_item_list_boxsizer.Add(self.my_item_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.my_buttons_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_next_button = wx.Button(self.my_service_panel, label='print receipt and get ready for next customer')
        self.my_next_button.SetFont(self.my_font)
        self.my_next_button.Bind(wx.EVT_BUTTON, self.__my_next_button_handle_EVT_BUTTON)
        self.my_buttons_boxsizer.Add(self.my_next_button, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        self.my_busket_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_busket_item_list = wx.ListCtrl(self.my_service_panel, style=wx.LC_REPORT | wx.LC_VRULES, id=wx.ID_ANY, pos=wx.DefaultPosition, size=[900, 150])
        self.my_busket_item_list.AppendColumn('item no', width=60)
        self.my_busket_item_list.AppendColumn('type', width=70)
        self.my_busket_item_list.AppendColumn('method', width=90)
        self.my_busket_item_list.AppendColumn('weight', width=70)
        self.my_busket_item_list.AppendColumn('destination', width=350)
        self.my_busket_item_list.AppendColumn('quantity', width=80)
        self.my_busket_item_list.AppendColumn('cost', width=80)
        self.my_busket_item_list.AppendColumn('each', width=100)
        self.my_busket_item_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.__my_busket_item_list_handle_EVT_LIST_ITEM_ACTIVATED)
        self.my_busket_boxsizer.Add(self.my_busket_item_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        self.my_service_boxsizer = wx.BoxSizer(wx.VERTICAL)
        self.my_service_boxsizer.Add(self.my_weight_boxsizer, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, border=3)
        self.my_service_boxsizer.Add(self.my_country_boxsizer, 1, wx.ALIGN_BOTTOM | wx.ALL| wx.EXPAND, border=3)
        self.my_service_boxsizer.Add(self.my_item_list_boxsizer, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, border=3)
        self.my_service_boxsizer.Add(self.my_busket_item_list, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, border=3)
        self.my_service_boxsizer.Add(self.my_buttons_boxsizer, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, border=3)

        self.SetSizer(self.my_panel_boxsizer)
        self.Layout()

        self.my_service_panel.SetSizer(self.my_service_boxsizer)
        self.my_service_panel.Layout()
        self.my_weight_entry.SetFocus()

    def __getKey(self, item):
        return int(item[0])

    def __prettyfy_list(self, line):

        # if self.my_weigh_unit_selector.GetSelection() == 0:
        #     suffix = 'Kg'
        # else:
        #     suffix = 'gr'
        suffix = 'Kg'

        item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = line
        new_line = [str(item_no), my_type, my_method, '{0:.2f} {1}'.format(my_weight, suffix), my_country, quantity, '${0:.2f}'.format(cost), '${0:.2f}'.format(my_price)]
        return new_line

    def __recalculate_and_update_service_price_options_display(self):

        self.application.current_country = self.my_country_choice.GetString(self.my_country_choice.GetSelection())
        self.application.current_weight = self.my_weight_entry.GetValue()
        if self.application.current_country and self.application.current_weight:
            self.my_item_list.DeleteAllItems()
            if not((self.application.current_weight == '') or (self.application.current_country == '')):
                if self.my_weigh_unit_selector.GetSelection() == 0:
                    divisor = 1
                else:
                    divisor = 1000
                self.application.current_weight = float(self.application.current_weight) / float(divisor)

                if self.application.available_serice_price_options:
                    self.application.available_serice_price_options.clear()
                self.application.available_serice_price_options = self.application.get_available_serice_price_options()
                for each_item in self.application.available_serice_price_options:
                    self.my_item_list.Append(each_item)

            # if self.application.available_serice_price_options:
            #     self.application.available_serice_price_options.clear()
            # self.application.available_serice_price_options = self.application.get_available_serice_price_options()
            # for each_item in self.application.available_serice_price_options:
            #     self.my_item_list.Append(each_item)

           
    def __blank_all_service_fields(self):
        """[summary]
        """

        self.my_weight_entry.SetValue("") #blank the selection in preparation for a new user
        self.my_country_choice.SetSelection(-1)
        self.my_weigh_unit_selector.SetSelection(1)
        self.my_item_list.DeleteAllItems()
        self.my_busket_item_list.DeleteAllItems()
        self.application.initialise_volatile()
        self.my_weight_entry.SetFocus()

    def __my_frame_handle_EVT_CLOSE(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.Destroy()

    def __my_menu_handle_Service_Option(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.SetTitle("Postal Service")
        self.my_info_panel.Hide()
        self.my_admin_panel.Hide()
        self.my_service_panel.Show()

        self.Layout()

    def __my_menu_handle_Admin_Option(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.SetTitle("Admin Service")
        self.my_info_panel.Hide()
        self.my_service_panel.Hide()
        self.my_admin_panel.Show()

        self.Layout()

    def __weight_entry_handle_EVT_CHOICE(self, event):  # pylint: disable=W0613

        self.__recalculate_and_update_service_price_options_display()

    def __my_weight_entry_handle_EVT_CHAR(self, event):  # pylint: disable=W0613
        """[summary]
        """
        keycode = event.GetKeyCode()
        if keycode < 255:  # valid ASCII
            # Valid alphanumeric character + backspace, left and right arrow
            if chr(keycode).isdigit() or keycode == 8 or keycode == 314 or keycode == 316 or keycode == 46:
                event.Skip()

    def __my_next_button_handle_EVT_BUTTON(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.__blank_all_service_fields()

    def __country_choice_handle_EVT_CHOICE(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.__recalculate_and_update_service_price_options_display()

    def __my_weigh_unit_selector_handle_EVT_RADIOBOX(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.__recalculate_and_update_service_price_options_display()

    def __my_item_list_handle_EVT_LIST_ITEM_ACTIVATED(self, event):  # pylint: disable=W0613
        """[summary]
        """

        index = self.my_item_list.GetFirstSelected()
        item_no = len(self.application.invoice) + 1

        my_type_str, my_price = self.application.available_serice_price_options[index]
        my_type_split = my_type_str.split(' ')
        my_method = my_type_split[0].upper()
        my_type = my_type_split[1]

        my_weight = self.application.current_weight

        quantity = 1
        cost = float(quantity * my_price)

        self.my_item_list.DeleteAllItems()
        self.my_busket_item_list.DeleteAllItems()

        # The very first item formed here in case the next if fails
        to_basket = [item_no, my_type, my_method, my_weight, self.application.current_country, quantity, cost, my_price]

        if self.application.invoice:
            for each_item in reversed(self.application.invoice):
                if (each_item[1] == my_type) and (each_item[2] == my_method) and (each_item[3] == my_weight) and (each_item[4] == self.application.current_country):
                    quantity = each_item[5] + 1
                    cost = my_price * quantity
                    item_no = each_item[0]
                    self.application.invoice.remove(each_item)
            to_basket = [item_no, my_type, my_method, my_weight, self.application.current_country, quantity, cost, my_price]

        self.application.invoice.append(to_basket)

        self.application.invoice = sorted(self.application.invoice, key=self.__getKey)

        for each_line in self.application.invoice:
            self.my_busket_item_list.Append(self.__prettyfy_list(each_line))

        self.application.invoice = sorted(self.application.invoice, key=self.__getKey)

        total_cost = 0
        total_items = 0

        for row in range(self.my_busket_item_list.GetItemCount()):
            number_pattern = re.compile(r'\d.{1,5}')
            number_matches = re.findall(number_pattern, self.my_busket_item_list.GetItem(row, 6).GetText())
        ### TODO: find a way of selectig colum number from text name of the column                                      # pylint: disable=W0511
            total_items += int(self.my_busket_item_list.GetItem(row, 5).GetText())
            total_cost += float(''.join(number_matches))

        self.my_status_bar.SetStatusText('Sale number: {}'.format(self.application.get_next_sales_number()))
        self.my_status_bar.SetStatusText('Total: ${0:.2f}'.format(total_cost), 3)
        self.my_status_bar.SetStatusText('Items: {0}'.format(total_items), 2)
        self.my_weight_entry.SetValue('')
        if not self.delete_or_modify:
            self.my_country_choice.SetSelection(-1)


    def __my_busket_item_list_handle_EVT_LIST_ITEM_ACTIVATED(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.delete_or_modify = True
        index = self.my_busket_item_list.GetFirstSelected()

        item_no, my_type, my_method, my_weight, self.application.current_country, quantity, cost, my_price = self.application.invoice[index]

        self.my_country_choice.SetSelection(self.my_country_choice.FindString(self.application.current_country))

        self.my_busket_item_list.DeleteAllItems()
        for each_line in self.application.invoice:
            self.my_busket_item_list.Append(self.__prettyfy_list(each_line))

        self.my_weight_entry.SetValue('')
        self.my_weigh_unit_selector.SetSelection(0)
        self.my_weight_entry.WriteText(str('{0:.2f}'.format(my_weight)))

        self.delete_or_modify = False
