import unittest
import task2


class TestTask1(unittest.TestCase):

    def test_list_int(self):
        """
        Test that function returns proper values
        """
        self.assertEqual(task2.square_list(5), [0, 1, 4, 9, 16])
        """
        Test that reaction to negative input is valid
        """
        self.assertRaises(ValueError, task2.square_list, -4)


if __name__ == '__main__':
    unittest.main()
