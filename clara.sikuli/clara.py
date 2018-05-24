from sikuli.Sikuli import *
import unittest


class TestBasicScenario(unittest.TestCase):

    def setUp(self):
        App.open("Google Chrome")
#    def tearDown(self):
#       App.close("Google Chrome")
    def test_01_open_clara(self):
        click("barre_de_recherche.png")
        paste("https://mae-attempt.herokuapp.com/")
        type(Key.ENTER)
        wait(4)
        assert exists("1527080917841.png")
        
    def test_02_start_clara(self):
#        click("barre_de_recherche.png")
#        paste("https://mae-attempt.herokuapp.com/")
#        type(Key.ENTER)
#        wait(4)
        click("1527087746609.png")
        
        assert exists(Pattern("1527082946751.png").similar(0.50))
    def test_03_pas_inscrit(self):
#        click("barre_de_recherche.png")
#        paste("https://mae-attempt.herokuapp.com/")
#        type(Key.ENTER)
#        wait(4)
#        click("1527087746609.png")
        click(Pattern("1527146499559.png").targetOffset(20,3))
        click("1527147045965.png")
        assert exists("1527146556717.png")
        
         
        


