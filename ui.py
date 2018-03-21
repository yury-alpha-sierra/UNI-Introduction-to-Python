"""[summary]

    Arguments:
        wx {[type]} -- [description]
"""
import wx # pylint: disable=E0611,W0401


class Ui(wx.Frame):      # pylint: disable=too-many-ancestors
    """[summary]

    Arguments:
        wx {[type]} -- [description]
    """
    def __init__(self, name, parent, id):                # pylint: disable=W0622

        self.current_country = ""

        wx.Frame.__init__(self, parent, id, name, size=(600, 450))

        self.my_panel = wx.Panel(self)

        self.my_button = wx.Button(self.my_panel, label='next >>', pos=(430, 280), size=(60, 20))
        self.Bind(wx.EVT_BUTTON, self.next_button, self.my_button)

        self.Bind(wx.EVT_CLOSE, self.close_window)

        self.status_bar = self.CreateStatusBar(3)     # pylint: disable=unused-variable
        self.status_bar.SetStatusWidths([100, 300, 200])

        self.menu_bar = wx.MenuBar()
        self.my_menu = wx.Menu()

        self.my_menu.Append(wx.NewId(), "Service", "This will start new postal service transaction.")
        self.my_menu.Append(wx.NewId(), "Admin", "This will start admin functions.")

        self.menu_bar.Append(self.my_menu, "Function")

        list_choices = ['Arab Emirates',
                        'Argentina',
                        'Austria',
                        'Bahrain',
                        'Belgium',
                        'Brazil',
                        'Brunei Darussalam',
                        'Cambodia',
                        'Canada',
                        'Chile',
                        'China',
                        'Cook Islands',
                        'Croatia',
                        'Cyprus',
                        'Czech Republic',
                        'Denmark',
                        'Estonia',
                        'Fiji',
                        'Finland',
                        'France',
                        'French Polynesia',
                        'Germany',
                        'Greece',
                        'Hong Kong',
                        'Hungary',
                        'India',
                        'Indonesia',
                        '"Iran - Islamic Republic Of"',
                        'Ireland',
                        'Israel',
                        'Italy',
                        'Japan',
                        'Kenya',
                        ''"Korea - Republic Of"','
                        'Kuwait',
                        "Lao People's Democratic Republic",
                        '"Macedonia - The Former Yugoslav Republic Of"',
                        'Malaysia',
                        'Malta',
                        'Mauritius',
                        'Mexico',
                        'Myanmar',
                        'Nauru',
                        'Nepal',
                        'Netherlands',
                        'New Caledonia',
                        'New Zealand',
                        'Nigeria',
                        'Norway',
                        'Pakistan',
                        'Papua New Guinea',
                        'Peru',
                        'Philippines',
                        'Poland',
                        'Portugal',
                        'Qatar',
                        'Romania',
                        'Russian Federation',
                        'Samoa',
                        'Saudi Arabia',
                        'Serbia',
                        'Singapore',
                        'Slovenia',
                        'Solomon Islands',
                        'South Africa',
                        'Spain',
                        'Sri Lanka',
                        'Sweden',
                        'Switzerland',
                        '"Taiwan - Province Of China"',
                        'Thailand',
                        'Tonga',
                        'Turkey',
                        'Ukraine',
                        'United Kingdom',
                        'United States',
                        'Vanuatu',
                        'Vietnam']

        self.my_weight_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.weight_label = wx.StaticText(self.my_panel, id=wx.ID_ANY, label="  Enter item weight:                ")
        self.my_weight_boxsizer.Add(self.weight_label, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL , border=15)
        self.weight_entry = wx.TextCtrl(self.my_panel)
        self.weight_entry.SetMaxLength(5)
        self.weight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)

        self.my_weight_boxsizer.Add(self.weight_entry, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        self.my_weigh_unit_selector = wx.RadioBox(self.my_panel, id=wx.ID_ANY, choices=["Kg", "gr"], majorDimension=2, style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)  #, label="select weight unit"
        self.my_weight_boxsizer.Add(self.my_weigh_unit_selector, 0,  wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL , border =10)

        self.my_country_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.country_label = wx.StaticText(self.my_panel, id=wx.ID_ANY, label="  Select destination country: ")
        self.my_country_boxsizer.Add(self.country_label, 0, border=30)
        self.country_choice = wx.Choice(
            self.my_panel, id=wx.ID_ANY, size=wx.DefaultSize, choices=list_choices,
            style=0)  # , validator=DefaultValidator, name=ChoiceNameStr
        self.my_country_boxsizer.Add(self.country_choice, 0, border=3)

        self.my_item_list_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.my_item_list = wx.ListCtrl(
            self.my_panel, id=wx.ID_ANY, pos=wx.DefaultPosition, size=[500, 200],
            style=wx.LC_ICON)
        self.my_item_list_boxsizer.Add(self.my_item_list, 10, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)


        self.my_user_input_boxsizer = wx.BoxSizer(wx.VERTICAL)
        self.my_user_input_boxsizer.Add(self.my_weight_boxsizer, 0, wx.ALIGN_TOP, border=3)
        self.my_user_input_boxsizer.Add(self.my_country_boxsizer, 0, wx.ALIGN_BOTTOM, border=3)
        self.my_user_input_boxsizer.Add(self.my_item_list_boxsizer, 0, wx.ALIGN_BOTTOM, border=3)
        self.my_panel.SetSizer(self.my_user_input_boxsizer)

        self.SetMenuBar(self.menu_bar)

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode < 255: # valid ASCII
            if chr(keycode).isdigit(): # Valid alphanumeric character
                event.Skip()

    def next_button(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """
        self.current_country = self.country_choice.GetString(
            self.country_choice.GetSelection())
        self.status_bar.SetStatusText(self.weight_entry.GetValue(), 0)
        self.status_bar.SetStatusText(self.current_country, 1)
        if self.my_weigh_unit_selector.GetSelection() == 0:
            self.status_bar.SetStatusText('Kg', 2)
        else:
            self.status_bar.SetStatusText('gr', 2)

    def close_window(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """

        self.Destroy()


POSTAGE_SERVICE_UI = wx.App()
FRAME = Ui('Postage Service', parent=None, id=-1)
FRAME.Centre()
FRAME.Show()
POSTAGE_SERVICE_UI.MainLoop()
