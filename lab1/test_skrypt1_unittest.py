import unittest
from unittest.mock import patch
import io
import skrypt

class test_capture_stdout(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        skrypt.display(["a","i","8"],False)
        captured_output = mock_stdout.getvalue()
        self.assertIn("a\ni\n8\n", captured_output)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run(self,mock_stdout):
        skrypt.run(["f","b","l","r","l","b"],skrypt.move_descriptions)
        captured_output = mock_stdout.getvalue()
        self.assertIn("Zwierzak idzie do przodu\nZwierzak idzie do tyłu\
\nZwierzak skręca w lewo\nZwierzak skręca w prawo\nZwierzak skręca w lewo\
\nZwierzak idzie do tyłu\n", captured_output)


if __name__ == '__main__':
    unittest.main()