from sikuli.Sikuli import *
import unittest

class HomeWarningBrowserVersion(unittest.TestCase):

    def setUp(self):
        App.open("Firefox")
#    def tearDown(self):
#       App.close("Firefox")
    def test_home_warning_browser(self):
        click("barre_recherche_ff16.png")
        paste("http://localhost:3000//")
        type(Key.ENTER)
        wait(4)
        assert exists("brower_warning.png")

suite = unittest.TestLoader().loadTestsFromTestCase(HomeWarningBrowserVersion)
unittest.TextTestRunner(verbosity=2).run(suite)
