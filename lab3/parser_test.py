import unittest
from model import MoveDirection
from controller import OptionsParser

class test_capture_stdout(unittest.TestCase):
    def test1(self):
        self.set = ["f", "f"]
        self.assertEqual(OptionsParser.parse(self.set), 
            [MoveDirection.forward, MoveDirection.forward])

    def test2(self):
        self.assertEqual(OptionsParser.parse(["b", "q", "l", "k", "f", "r"]),
            [MoveDirection.backward, MoveDirection.left, MoveDirection.forward,
            MoveDirection.right])
     

if __name__ == '__main__':
    unittest.main()