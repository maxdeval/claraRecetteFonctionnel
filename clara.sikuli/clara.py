import unittest

from sikuli.Sikuli import *


class TestBasicScenario(unittest.TestCase):

    def setUp():
        App.open("Google Chrome")

    def tearDown():
        App.close("Google Chrome")

    def test_01_open_clara():
        click("1526994917663.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        assert exists(Pattern("1526995285010.png").targetOffset(-26,100))
    setUp()    
    test_01_open_clara()