import unittest
from io import StringIO
from unittest.mock import patch
from print_square import print_square

class PrintSquareTestCase(unittest.TestCase):
    def test_print_square(self):
        size = 5
        expected_output = "#####\n#####\n#####\n#####\n#####\n"

        with patch("sys.stdout", new=StringIO()) as fake_output:
            print_square(size)
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
