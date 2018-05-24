from sikuli.Sikuli import *
import unittest


class AdresseQuestionPopup(unittest.TestCase):

    def setUp(self):
        App.open("Firefox")
#    def tearDown(self):
#       App.close("Firefox")
    def test_adresse_question_popup(self):
        click("barre_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        wait(4)
        click("1527087746609.png")
        click(Pattern("1527146499559.png").targetOffset(20,3))
        click("continuer.png")
        click("assurance_chomage.png")
        click("continuer.png")
        click("montant_mois.png")
        paste("300")
        click("continuer.png")
        wait(2)
        paste("16")
        click("continuer.png")
        click("bac_3_licence.png")
        click("continuer.png")
        wait(2)
        assert exists("adresse_question_popup.png")
        
suite = unittest.TestLoader().loadTestsFromTestCase(AdresseQuestionPopup)
unittest.TextTestRunner(verbosity=2).run(suite)        
        