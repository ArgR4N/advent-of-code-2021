import unittest

def day_6(data):
    print(data)
    i = 0
    while(i < 80):
        for index in range(len(data)):
            if(data[index] == 0):
                data.append(8)
                data[index] = 6
            else:
                data[index] -= 1
        i += 1
    return len(data)

def day_6_part_2(data):
    print(data)
    state = data
    data = {}
    for i in range(0, 9):
        data[i] = 0
    for fish in state:
        data[fish] += 1

    for i in range(256):
        zeroes = data[0]
        data[0] = 0
        for index in range(1, len(data)):
            data[index - 1] += data[index]
            data[index] = 0
        data[6] += zeroes
        data[8] += zeroes
    total = 0
    for i in range(len(data)):
        total += data[i] 
    print(total)
    return total


class testDay6(unittest.TestCase):
    def test_day_6(self):
        data=[3,4,3,1,2]
        self.assertEqual(
            day_6(data),
           5934 
        )
        data=[3,4,3,1,2]
        self.assertEqual(
            day_6_part_2(data),
            26984457539
        )
    def test_day_6_final(self):
        data = [1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]
        self.assertTrue(
            day_6_part_2(data)
        )

if __name__ == '__main__':
    unittest.main()