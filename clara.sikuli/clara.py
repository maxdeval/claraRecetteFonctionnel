from sikuli.Sikuli import *
import unittest


class TestBasicScenario(unittest.TestCase):

    def setUp(self):
        App.open("Google Chrome")

    def tearDown(self):
        App.close("Google Chrome")
        
    def test_01_open_clara(self):
        click("barre_de_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        assert exists(Pattern("acceuil.png").targetOffset(-26,100))
    def test_02_start_form(self):
        click(Pattern("acceuil.png").targetOffset(-32,106))
        assert exists(Pattern("inscription_questions.png").targetOffset(-23,-18))

