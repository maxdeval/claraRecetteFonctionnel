from sikuli.Sikuli import *
from adresseQuestionPopup import *
import unittest


suite = unittest.TestLoader().loadTestsFromTestCase(AdresseQuestionPopup)
unittest.TextTestRunner(verbosity=2).run(suite)

test_adresse_question_popup(self)
