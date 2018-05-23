import unittest
from clara import *

suite = unittest.TestLoader().loadTestsFromTestCase(TestBasicScenario)
unittest.TextTestRunner(verbosity=2).run(suite)

setUp(self)
test_01_open_clara(self)
test_02_start_form(self)
tearDown(self)