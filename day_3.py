import unittest

def day_3(data):
    gamma = [0 for _ in range(len(data[0]))]
    epsilon = [0 for _ in range(len(data[0]))]
    for elm in data:
        for i in range(len(elm)):
            gamma[i] += int(elm[i])
    gamma_int = 0        
    epsilon_int = 0        
    for index in range(len(gamma)):
        if(gamma[index] > len(data) / 2):
            gamma_int += 2 ** ((index - (len(gamma) - 1)) * - 1)
        else:
            epsilon_int += 2 ** ((index - (len(gamma) - 1)) * -1)
    return gamma_int * epsilon_int
            
def day_3_part_2(data):
    data = [data[index] 
    for index in range(len(data))]

    def findOxygen(data):
        index = 0
        newData = data
        while len(newData) > 1:
            one = 0
            zero = 0
            ones = []
            zeroes = []
            for i in range(len(newData)):
                if(newData[i][index] == '0'):
                    zero += 1
                    zeroes.append(newData[i])
                else:
                    one += 1
                    ones.append(newData[i])
            if(zero > one):
                newData = zeroes
            else:
                newData = ones
            index += 1
        return newData[0]

    def findC2O(data):
        index = 0
        newData = data
        while len(newData) > 1:
            one = 0
            zero = 0
            ones = []
            zeroes = []
            for i in range(len(newData)):
                if(newData[i][index] == '0'):
                    zero += 1
                    zeroes.append(newData[i])
                else:
                    one += 1
                    ones.append(newData[i])
            if(one < zero):
                newData = ones
            else:
                newData = zeroes
            index += 1
        return newData[0]

    oxygen = int(findOxygen(data), 2)
    c2o = int(findC2O(data), 2)
    print(oxygen * c2o)


            
class TestDay3(unittest.TestCase):
    def test_day_3(self):
        data =(
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        )
        self.assertEqual(
            day_3(data),
        198)
        self.assertEqual(
            day_3_part_2(data),
        230)

    def test_final_day_3(self):
        f = open("day_3.txt", "r")
        data = f.read().splitlines()
        f.close()

        self.assertTrue(
            day_3(data)
        )
        self.assertTrue(
            day_3_part_2(data)
        )



if __name__ == '__main__':
    unittest.main()