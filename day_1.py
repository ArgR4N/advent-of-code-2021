import unittest

def day_1(data):
    inc = 0
    prev = data[0]
    for index in range(len(data)):
        if(data[index] > prev):
            inc += 1
        prev = data[index]
    print(inc)
    return inc

def day_1_part_2(data):
    inc = 0
    for index in range(len(data)):
        if(index < len(data) - 3):
            a = data[index] + data[index + 1] + data[index + 2]
            b = data[index + 1] + data[index + 2] + data[index + 3]
            if(b > a):
                inc += 1
    print(inc)
    return inc

class TestDay1(unittest.TestCase):
    def test_day_1(self):
        data =(
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
        )
        self.assertEqual(
            day_1(data),
        7)
        self.assertEqual(
            day_1_part_2(data),
        5)

    def test_final_day_1(self):
        f = open("day_1.txt", "r")
        data = [
            int(elm)
            for elm in f.read().splitlines()
        ]
        f.close()
        self.assertTrue(
            day_1(data)
        )
        self.assertTrue(
            day_1_part_2(data)
        )



if __name__ == '__main__':
    unittest.main()