import unittest
import hotel2
from unittest.mock import patch
import sys

class test_capture_stdout(unittest.TestCase):
    def test1(self):
        testargs = ["rooms2.json"]
        with patch.object(sys, 'argv', testargs):
            setup = get_setup_file()
            assert setup == "rooms2.jons"


if __name__ == '__main__':
    unittest.main()