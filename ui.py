"""[summary]
"""

import re
import datetime as dt
import numpy  as np
import pandas as pn
import wx  # pylint: disable=E0611,W0401

class Ui(wx.Frame):  # pylint: disable=too-many-ancestors
    """[summary]
    """

    def __init__(self, name, parent, id, app):  # pylint: disable=W0622

        self.out_df = None

        self.application = app
        self.delete_or_modify = False
        self.weight_entry_error = False

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

        self.my_status_bar = self.CreateStatusBar(4)  # pylint: disable=unused-variable
        self.my_status_bar.SetStatusWidths([200, 300, 200, 100])
        self.my_status_bar.SetStatusText('')

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
        my_info_text = wx.StaticText(self.my_info_panel, -1, style=wx.ALIGN_LEFT | wx.EXPAND)
        my_info_font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'sans-serif')
        my_info_text.SetFont(my_info_font)
        my_message = 'Introduction\n'
        my_info_font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, u'sans-serif')
        my_info_text.SetFont(my_info_font)
        my_message = my_message + 'This program was written by Yury Gurevich as a part of submission for Assignment2 project.\n\n'
        my_message = my_message + '\nThis software assists postal workers in task of vending stamps for the following six kinds of international post based on the price guide:\n'
        my_message = my_message + '\n• Economy Letter;'
        my_message = my_message + '\n• Express Letter;'
        my_message = my_message + '\n• Economy Parcel_By Air;'
        my_message = my_message + '\n• Economy Parcel_By Sea;'
        my_message = my_message + '\n• Standard Parcel;'
        my_message = my_message + '\n• Express Parcel.'
        my_message = my_message + '\n\n\nSELECT FUNCTION FROM FUNCTION SELECTION MENU ABOVE.'

        my_info_text.SetLabel(my_message)

        self.my_status_bar.SetStatusText('')

        self.my_info_boxsizer.Add(my_info_text, 1, wx.ALL | wx.EXPAND, border=3)

        self.my_info_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_info_panel.SetBackgroundColour(self.my_info_panel_colour)

        my_info_font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'sans-serif')
        my_info_text.SetFont(my_info_font)

    def __init_admin_panel(self):

        self.menu_item_admin = self.my_menu.Prepend(wx.NewId(), "Admin", "Start admin functions.")
        self.Bind(wx.EVT_MENU, self.__my_menu_handle_Admin_Option, self.menu_item_admin)

        self.my_admin_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_admin_panel.SetBackgroundColour(self.my_admin_panel_colour)

        self.my_admin_options_boxsizer = wx.BoxSizer(wx.VERTICAL)

        my_info_msg = wx.StaticText(self.my_admin_panel, -1, style=wx.ALIGN_LEFT | wx.EXPAND)
        my_info_msg.SetFont(self.my_font)
        my_info_msg.SetLabel('Select function:')
        self.my_admin_options_boxsizer.Add(my_info_msg, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

        admin_choices = \
        ['The gross sales amount of different years', 'The customer flow during a day (number of sales occur at different time (hours) of a day', \
            'The popularity of postage method for letter and parcel (number of purchased stamps with different postage methods)', 'The top 5 most popular destination countries including any postage']

        self.my_admin_function_selector = wx.RadioBox(self.my_admin_panel, id=wx.ID_ANY, choices=admin_choices, majorDimension=0, style=wx.RA_SPECIFY_ROWS | wx.NO_BORDER)
        self.my_admin_function_selector.SetFont(self.my_font)
        self.my_admin_options_boxsizer.Add(self.my_admin_function_selector, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

        self.admin_process_options_button = wx.Button(self.my_admin_panel, label='run selection')
        self.admin_process_options_button.SetFont(self.my_font)
        self.admin_process_options_button.Bind(wx.EVT_BUTTON, self.admin_process_options_button_handle_EVT_BUTTON)
        self.my_admin_options_boxsizer.Add(self.admin_process_options_button, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, border=10)

        self.my_admin_report_list = wx.ListCtrl(self.my_admin_panel, style=wx.LC_REPORT, id=wx.ID_ANY, pos=wx.DefaultPosition, size=[900, 250])

        self.my_admin_report_list.SetFont(self.my_font)
        self.my_admin_report_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.__my_item_list_handle_EVT_LIST_ITEM_ACTIVATED)
        self.my_admin_options_boxsizer.Add(self.my_admin_report_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)


        self.my_status_bar.SetStatusText('')

        self.SetSizer(self.my_admin_options_boxsizer)
        self.Layout()

    def admin_process_options_button_handle_EVT_BUTTON(self, event):     # pylint: disable=W0613

        def process_admin_panel_switch(val):
            return {1: 'gross_sales_amount', 2: 'customer_flow', 3: 'postage_method_popularity', 4: 'top_5'}.get(val, None)

        sel = self.my_admin_function_selector.GetSelection()
        fun = process_admin_panel_switch(sel+1)  #switch is base 1, my_admin_function_selector is base 0, normalising here
        cmd = 'self.' + fun + '()'

        exec(cmd) # pylint: disable=W0122

    def gross_sales_amount(self):

        self.my_admin_report_list.ClearAll()
        self.out_df = pn.pivot_table(self.application.sales_history, index=[(pn.to_datetime(
            self.application.sales_history['date_time'], format='%d/%m/%Y %H:%M').dt.year)], values=['cost'], aggfunc=np.sum)

        self.my_admin_report_list.AppendColumn(self.out_df.index.name, width=230)
        self.my_admin_report_list.AppendColumn(self.out_df.columns.values.tolist()[0], width=150)

        new_line = zip(self.out_df.index.tolist(), self.out_df.values.tolist())
        for each_line in new_line:
            new_ndx, new_val = each_line
            new_val1 = '${0:,.2f}'.format(round(new_val[0], 2))
            self.my_admin_report_list.Append([new_ndx, new_val1])

    def customer_flow(self):

        self.my_admin_report_list.ClearAll()
        self.out_df = pn.pivot_table(self.application.sales_history,
                                    index=[(pn.to_datetime(self.application.sales_history['date_time'], format='%d/%m/%Y %H:%M').dt.hour)],
                                    values=['sale_id'], aggfunc={'quantity':len})
        print(self.out_df)

    def postage_method_popularity(self):

        self.out_df = pn.pivot_table(self.application.sales_history, index=['postage method'], values=['quantity'], aggfunc=np.sum)
        self.my_admin_report_list.ClearAll()
        self.my_admin_report_list.AppendColumn(self.out_df.index.name, width=230)
        self.my_admin_report_list.AppendColumn(self.out_df.columns.values.tolist()[0], width=150)

        new_line = zip(self.out_df.index.tolist(), self.out_df.values.tolist())
        for each_line in new_line:
            new_ndx, new_val = each_line
            new_val1 = '{0:,}'.format(round(new_val[0], 2))
            self.my_admin_report_list.Append([new_ndx, new_val1])

    def top_5(self):

        self.out_df = pn.pivot_table(self.application.sales_history, index=['destination'], values=['quantity', 'cost'], aggfunc=np.sum).head(n=5)
        self.my_admin_report_list.ClearAll()
        self.my_admin_report_list.AppendColumn(self.out_df.index.name, width=230)
        self.my_admin_report_list.AppendColumn(self.out_df.columns.values.tolist()[0], width=150)

        new_line = zip(self.out_df.index.tolist(), self.out_df.values.tolist())
        for each_line in new_line:
            new_ndx, new_val = each_line
            new_val1 = '${0:,.2f}'.format(round(new_val[0], 2))
            self.my_admin_report_list.Append([new_ndx, new_val1])

    def __init_service_panel(self):
        """[summary]
        """

        self.menu_item_service = self.my_menu.Prepend(wx.NewId(), "Service", "Start new postal service transaction.")
        self.Bind(wx.EVT_MENU, self.__my_menu_handle_Service_Option, self.menu_item_service)

        self.my_service_panel_colour = wx.Colour(230, 240, 255, alpha=wx.ALPHA_OPAQUE)
        self.my_service_panel.SetBackgroundColour(self.my_service_panel_colour)

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

        self.my_weigh_unit_selector.SetSelection(0)
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
        self.my_status_bar.SetStatusText('Sale number: {}'.format(self.application.get_next_sales_number()))
        self.my_service_panel.Layout()
        self.my_weight_entry.SetFocus()

    def __getKey(self, item):
        return int(item[0])

    def __prettyfy_list(self, line):

        suffix = 'Kg'

        item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = line

        adj_weight = my_weight/1000
        if adj_weight < 0.01:
            adj_weight = 0.01
        new_line = [str(item_no), my_type, my_method, '{0:.2f} {1}'.format(adj_weight, suffix), my_country, quantity, '${0:.2f}'.format(cost), '${0:.2f}'.format(my_price)]
        return new_line

    def __recalculate_and_update_service_price_options_display(self):

        self.application.current_country = self.my_country_choice.GetString(self.my_country_choice.GetSelection())
        self.application.current_weight = self.my_weight_entry.GetValue()
        try:
            float(self.application.current_weight)
        except ValueError:
            self.my_item_list.DeleteAllItems()
            # self.my_item_list.SetBackgroundColour('yellow')
            return
        if self.application.current_country and self.application.current_weight:
            self.my_item_list.DeleteAllItems()
            if not((self.application.current_weight == '') or (self.application.current_country == '')):
                if self.my_weigh_unit_selector.GetSelection() == 0:
                    multiplier = 1000
                else:
                    multiplier = 1
                self.application.current_weight = float(self.application.current_weight) * float(multiplier)
                if self.application.current_weight < 1:
                    self.weight_entry_error = True
                    return

                if self.application.available_serice_price_options:
                    self.application.available_serice_price_options.clear()

                self.application.available_serice_price_options = self.application.get_available_serice_price_options()
                if self.application.available_serice_price_options:
                    self.my_item_list.DeleteAllItems()
                    # self.my_item_list.SetBackgroundColour('white')
                    for each_item in self.application.available_serice_price_options:
                        self.my_item_list.Append(each_item)
                else:
                    self.my_item_list.DeleteAllItems()
                    # self.my_item_list.SetBackgroundColour('yellow')
                self.Layout()

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
        self.my_status_bar.SetStatusText('Sale number: {}'.format(self.application.get_next_sales_number()))
        self.my_status_bar.SetStatusText('Total: ${0:.2f}'.format(0), 3)
        self.my_status_bar.SetStatusText('Items: {0}'.format(0), 2)

    def __repaint_busket_and_status_bar(self):
        self.application.invoice = sorted(self.application.invoice, key=self.__getKey)

        i = 1
        for each_line in self.application.invoice:
            item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = each_line
            item_no = i
            i += 1
            each_line = item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price
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

    def __process_invoice_finacials(self, f):

        suffix = 'Kg'
        f.write('--------------Invoice---------------\n\n')
        for each_line in self.application.invoice:
            item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = each_line
            adj_weight = my_weight/1000
            if adj_weight < 0.01:
                adj_weight = 0.01

            new_line = '\nItem No: ' + str(item_no) + '  Type: ' + my_type + '  METHOD:  ' + my_method.capitalize() + '    Weight: {0:.2f} {1}'.format(
                adj_weight, suffix) + ' Destination: ' + my_country + ' Quantity: ' + str(quantity) + '    Cost: ${0:.2f}'.format(cost) + ' [${0:.2f}ea]\n'.format(my_price)
            f.write(new_line)
        f.write('\n\n-----------End Invoice---------------')

    def __process_invoice_stamps(self, f):

        f.write('\n\n-----------Purchased Stamps-----------\n')

        for each_line in self.application.invoice:
            f.write('---------------------------------------------------\n')
            item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = each_line  # pylint: disable=W0612
            while quantity > 0:
                adj_weight = my_weight/1000
                if adj_weight < 0.01:
                    adj_weight = 0.01

                new_line = my_method.capitalize() + ' ' +  my_type.capitalize() + '\n' + 'Destination:  ' + my_country.capitalize() + '    Weight: {0:.2f}'.format(adj_weight)
                f.write(new_line)
                f.write('\n---------------------------------------------------\n')
                quantity -= 1

    def __print_invoice(self):

        now = dt.datetime.now()
        file_name = now.strftime('%Y-%m-%d %H-%M-%S')
        file_name = str(file_name) + ' ' + str(self.application.get_next_sales_number()) + ' invoice.txt'
        with open(file_name, 'w') as invoice_file:
            self.__process_invoice_finacials(invoice_file)
            self.__process_invoice_stamps(invoice_file)

    def __create_sales_record(self):

        now = dt.datetime.now()
        file_name = self.application.data_base_directory + self.application.sales_history_file
        with open(file_name, 'a') as invoice_file:  # pylint: disable=W0622
            for each_line in self.application.invoice:
                item_no, my_type, my_method, my_weight, my_country, quantity, cost, my_price = each_line # pylint: disable=W0612
                while quantity > 0:
                    adj_weight = my_weight/1000
                    if adj_weight < 0.01:
                        adj_weight = 0.01
                    new_line = '\n' + str(self.application.get_next_sales_number()) + ',' + now.strftime('%d/%m/%Y %H:%M') + ',' + my_type.lower() + ',' + str('{0:.2f}'.format(
                        adj_weight)) + ',' + my_country.capitalize() + ',' + my_method.capitalize() + ' ' + my_type.capitalize() + ',' + str(1) + ',' + str(my_price)
                    invoice_file.write(new_line)
                    quantity -= 1

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
        self.my_status_bar.SetStatusText('Sale number: {}'.format(self.application.get_next_sales_number()))

        self.Layout()

    def __my_menu_handle_Admin_Option(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.SetTitle("Admin Service")
        self.my_info_panel.Hide()
        self.my_service_panel.Hide()
        self.my_admin_panel.Show()
        self.my_status_bar.SetStatusText('')

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

        if self.application.invoice:
            self.__print_invoice()
            self.__create_sales_record()
        self.application.invoice = None
        self.application.sales_history = None
        self.application.sales_history = self.application.import_sales_history()
        # self.my_item_list.SetBackgroundColour('white')
        self.my_item_list.Layout()
        self.my_status_bar.SetStatusText('Sale number: {}'.format(self.application.get_next_sales_number()))
        self.__blank_all_service_fields()
        self.Layout()

    def __country_choice_handle_EVT_CHOICE(self, event):  # pylint: disable=W0613
        """[summary]
        """
        if not self.weight_entry_error:
            self.__recalculate_and_update_service_price_options_display()
        else:
            event.Skip()

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

        self.__repaint_busket_and_status_bar()

        self.my_weight_entry.SetValue('')
        if not self.delete_or_modify:
            self.my_country_choice.SetSelection(-1)

    def __my_busket_item_list_handle_EVT_LIST_ITEM_ACTIVATED(self, event):  # pylint: disable=W0613
        """[summary]
        """
        self.delete_or_modify = True
        index = self.my_busket_item_list.GetFirstSelected()

        item_no, my_type, my_method, my_weight, self.application.current_country, quantity, cost, my_price = self.application.invoice.pop(index)

        self.my_country_choice.SetSelection(self.my_country_choice.FindString(self.application.current_country))

        if quantity > 1:
            quantity -= 1
            cost -= my_price
            to_basket = [item_no, my_type, my_method, my_weight, self.application.current_country, quantity, cost, my_price]

            self.application.invoice.append(to_basket)

        self.my_busket_item_list.DeleteAllItems()
        self.__repaint_busket_and_status_bar()

        self.my_weight_entry.SetValue('')
        self.my_weigh_unit_selector.SetSelection(0)
        self.my_weight_entry.WriteText(str('{0:.2f}'.format(my_weight/1000)))

        self.delete_or_modify = False
