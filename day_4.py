import unittest

def day_4(data):
    print(data)

class TestDay4(unittest.TestCase):
    def test_day_3(self):

        self.assertEqual(
           day_4(data),
        4512)

if __name__ == '__main__':
    unittest.main()