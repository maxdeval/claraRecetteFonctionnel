from sikuli.Sikuli import *
from clara import *
import unittest


suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicScenario)
unittest.TextTestRunner(verbosity=2).run(suite)

test_01_open_clara(self)

