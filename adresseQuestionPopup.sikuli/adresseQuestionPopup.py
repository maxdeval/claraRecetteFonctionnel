from sikuli.Sikuli import *
import unittest


class AdresseQuestionPopup(unittest.TestCase):

    def setUp(self):
        App.open("Firefox")
    def tearDown(self):
       App.close("Firefox")
    def test_adresse_question_pop(self):
        click("barre_de_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        wait(4)
        click("1527087746609.png")
        click(Pattern("1527146499559.png").targetOffset(20,3))
        click("1527147045965.png")