from sikuli.Sikuli import *
import unittest


class TestBasicScenario(unittest.TestCase):

    def setUp(self):
        App.open("Google Chrome")
    def test_01_open_clara(self):
        click("barre_de_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        wait(4)
        assert exists("1527080917841.png")
        
        


