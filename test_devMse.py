from unittest import TestCase
import unittest
import numpy as np
from devMse import devMse

class TestDevMse(unittest.TestCase):
    def test_devMse(self):
        x = np.random.rand(6, 1)
        y = np.random.rand(6,1)
        res = devMse(x, y)
        self.assertIsNone(res, 'Successfully Tested.')

if __name__ == '__main__':
    unittest.main()
