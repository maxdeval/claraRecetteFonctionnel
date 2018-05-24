from sikuli.Sikuli import *
import unittest

class LoadingBar(unittest.TestCase):

    def setUp(self):
        App.open("Google Chrome")
#    def tearDown(self):
#       App.close("Google Chrome")
    def test_loading_bar(self):
        click("chrome_bar.png")
        paste("http://localhost:3000/")
        type(Key.ENTER)
        wait(15)
        click("je_commence.png")
        wait(15)
        assert exists("loading.png")
        


suite = unittest.TestLoader().loadTestsFromTestCase(LoadingBar)
unittest.TextTestRunner(verbosity=2).run(suite)