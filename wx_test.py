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
                              pos=(330, 200), size=(60, 20))
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
        country_choice = wx.Choice(
            my_panel, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
            choices=list_choices, style=0)  # , validator=DefaultValidator, name=ChoiceNameStr
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
