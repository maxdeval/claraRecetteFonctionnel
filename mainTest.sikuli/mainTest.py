from sikuli.Sikuli import *
from adresseQuestionPop import *
import unittest


suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicScenario)
unittest.TextTestRunner(verbosity=2).run(suite)

test_adresse_question_pop(self):
