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

        self.current_country = ""

        wx.Frame.__init__(self, parent, id,
                          "My firstg GUI app", size=(300, 200))
        my_panel = wx.Panel(self)
        my_button = wx.Button(my_panel, label='exit',
                              pos=(330, 200), size=(60, 20))
        self.Bind(wx.EVT_BUTTON, self.close_button, my_button)
        self.Bind(wx.EVT_CLOSE, self.close_window)
        self.status_bar = self.CreateStatusBar()     # pylint: disable=unused-variable
        self.menu_bar = wx.MenuBar()
        first_menu = wx.Menu()
        # second_menu = wx.Menu()
        first_menu.Append(
            wx.NewId(),
            "Service", "This will start new postal service transaction.")
        first_menu.Append(
            wx.NewId(),
            "Admin", "This will start admin functions.")
        self.menu_bar.Append(first_menu, "Function")
        # self.menu_bar.Append(second_menu, "Edit")
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
        self.country_choice = wx.Choice(
            my_panel, id=wx.ID_ANY, size=wx.DefaultSize, choices=list_choices,
            style=0, pos=(20, 120))  # , validator=DefaultValidator, name=ChoiceNameStr
        self.current_country = self.country_choice.GetString(
            self.country_choice.GetSelection())

        self.my_weight_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.weight_label = wx.StaticText(
            my_panel, id=wx.ID_ANY, label="Enter item weight:")
        self.my_weight_boxsizer.Add(self.weight_label, 0, border=3)
        self.weight_entry = wx.TextCtrl(my_panel)
        self.weight_entry.SetMaxLength(7)
        self.my_weight_boxsizer.Add(self.weight_entry, 0, wx.ALIGN_RIGHT, 5)
        my_panel.SetSizer(self.my_weight_boxsizer)


        self.SetMenuBar(self.menu_bar)

    def close_button(self, event):  # pylint: disable=W0613
        """[summary]

        Arguments:
            event {[type]} -- [description]
        """
        self.current_country = self.country_choice.GetString(
            self.country_choice.GetSelection())
        print(self.current_country)
        print(self.weight_label)
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