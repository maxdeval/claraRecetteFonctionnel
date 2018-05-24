from sikuli.Sikuli import *
import unittest


class GoToResults(unittest.TestCase):

    def setUp(self):
        App.open("Firefox")
#    def tearDown(self):
#       App.close("Firefox")
    def test_go_to_results(self):
        click("barre_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        wait(4)
        click("je_commence.png")
        click(Pattern("pas_inscrit.png").targetOffset(20,3))
        click("continuer.png")
        click("assurance_chomage.png")
        click("continuer.png")
        click("montant_mois.png")
        paste("300")
        click("continuer.png")
        wait(1)
        paste("16")
        click("continuer.png")
        click("bac_3_licence.png")
        click("continuer.png")
        wait(2)
        click(Pattern("continuer.png").similar(0.81))
        click("aucune_de_ces_situations.png")
        click("continuer.png")
        wait("pouvez_beneficier.png")
        assert exists("pouvez_beneficier.png")


suite = unittest.TestLoader().loadTestsFromTestCase(GoToResults)
unittest.TextTestRunner(verbosity=2).run(suite) 