import unittest

def day_2(data):
    depth = 0
    horiz = 0
    for elem in data:
        move, q = elem.split(' ')
        q = int(q)
        if(move == 'forward'):
            horiz += q
        if(move == 'up'):
            depth -= q
        if(move == 'down'):
            depth += q
    return depth * horiz

def day_2_part_2(data):
    depth = 0
    horiz = 0
    aim = 0
    for elem in data:
        move, q = elem.split(' ')
        q = int(q)
        if(move == 'forward'):
            horiz += q
            depth += aim * q
        if(move == 'up'):
            aim -= q
        if(move == 'down'):
            aim += q
    print(depth * horiz)
    return depth * horiz


class TestDay2(unittest.TestCase):
    def test_day_2(self):
        data =(
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        )
        self.assertEqual(
            day_2(data),
        150)
        self.assertEqual(
            day_2_part_2(data),
        900)

    def test_final_day_2(self):
        f = open("day_2.txt", "r")
        data = f.read().splitlines()
        f.close()
        self.assertTrue(
            day_2(data)
        )
        self.assertTrue(
            day_2_part_2(data)
        )

if __name__ == '__main__':
    unittest.main()