# -*- coding: utf-8 -*-
import sys
import unittest
from tests.QA_364_tests import BusinessCreationTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(BusinessCreationTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
