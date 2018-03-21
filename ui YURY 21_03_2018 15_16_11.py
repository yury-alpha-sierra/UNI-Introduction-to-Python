"""[summary]

    Arguments:
        wx {[type]} -- [description]
"""
from wx.core import * # pylint: disable=E0611,W0401


class MyApp(wx.Frame):      # pylint: disable=too-many-ancestors
    """[summary]

    Arguments:
        wx {[type]} -- [description]
    """

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode < 255: # valid ASCII
            if chr(keycode).isdigit(): # Valid alphanumeric character
                event.Skip()


    def __init__(self, parent, id):                # pylint: disable=W0622

        self.current_country = ""

        wx.Frame.__init__(self, parent, id, "My firstg GUI app", size=(500, 300))

        self.my_panel = wx.Panel(self)

        self.my_button = wx.Button(self.my_panel, label='next >>', pos=(330, 200), size=(60, 20))
        self.Bind(wx.EVT_BUTTON, self.next_button, self.my_button)

        self.Bind(wx.EVT_CLOSE, self.close_window)

        self.status_bar = self.CreateStatusBar()     # pylint: disable=unused-variable
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
        self.weight_label = wx.StaticText(self.my_panel, id=wx.ID_ANY, label="Enter item weight:                ")
        self.my_weight_boxsizer.Add(self.weight_label, 0, wx.ALIGN_LEFT, border=3)
        self.weight_entry = wx.TextCtrl(self.my_panel)
        self.weight_entry.SetMaxLength(5)
        self.weight_entry.Bind(wx.EVT_CHAR, self.handle_keypress)

        self.my_weight_boxsizer.Add(self.weight_entry, 0, wx.ALIGN_RIGHT, 20)
        self.my_weigh_unit_selector = wx.RadioBox(self.my_panel, id=wx.ID_ANY, label="select weight unit", choices=["Kg", "gr"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.my_weight_boxsizer.Add(self.my_weigh_unit_selector, 0, wx.ALIGN_RIGHT, 20)
            # validator=DefaultValidator, name=RadioBoxNameStr)

        self.my_country_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.country_label = wx.StaticText(self.my_panel, id=wx.ID_ANY, label="Select destination country: ")
        self.my_country_boxsizer.Add(self.country_label, 0, border=30)
        self.country_choice = wx.Choice(
            self.my_panel, id=wx.ID_ANY, size=wx.DefaultSize, choices=list_choices,
            style=0)  # , validator=DefaultValidator, name=ChoiceNameStr
        self.my_country_boxsizer.Add(self.country_choice, 0, border=3)


        self.my_user_input_boxsizer = wx.BoxSizer(wx.VERTICAL)
        self.my_user_input_boxsizer.Add(self.my_weight_boxsizer, 0, wx.ALIGN_TOP, border=3)
        self.my_user_input_boxsizer.Add(self.my_country_boxsizer, 0, wx.ALIGN_BOTTOM, border=3)
        self.my_panel.SetSizer(self.my_user_input_boxsizer)

        self.SetMenuBar(self.menu_bar)

    def next_button(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """
        self.current_country = self.country_choice.GetString(
            self.country_choice.GetSelection())
        print(self.current_country)
        print(self.weight_entry.GetValue())
        print(self.my_weigh_unit_selector.GetSelection())


    def close_window(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """

        self.Destroy()


MY_APP = wx.App()
FRAME = MyApp(parent=None, id=-1)
FRAME.Centre()
FRAME.Show()
MY_APP.MainLoop()
