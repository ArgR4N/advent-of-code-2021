from typing import final
import unittest
from unittest import result

def day_8(data):
    data = [elm.split(' | ')[1] for elm in data]
    result = 0
    for elem in data:
        for e in elem.split(' '):
            if(len(e) == 2):
                result += 1
            elif(len(e) == 3):
                result += 1
            
            elif(len(e) == 4):
                result += 1

            elif(len(e) == 7):
                result += 1
    return result

def day_8_part_2(data):

    def getCommons(a, b):
        commons = 0
        for letter in a:
            if letter in b:
                commons += 1
        return commons
    result = 0
    for case in data:
        sign, output = case.split(' | ')

        #sort letters of each word
        sign = [''.join(sorted(n))
            for n in sign.split(' ')]
        output = [''.join(sorted(n))
            for n in output.split(' ')]

        sign.sort(key = len)

        #get 1, 7, 4, 8
        code = {sign[0]:1, sign[1]:7, sign[2]:4, sign[9]:8}
        fives = [n for n in sign[3:6]]
        sixes = [n for n in sign[6:9]]
        #get 2
        for index in range(len(fives)):
            if(getCommons(fives[index], sign[2]) == 2):
                code[fives[index]] = 2
                del(fives[index])
                break
        #get 3
        for index in range(len(fives)):
            if(getCommons(fives[index], sign[0]) == 2):
                code[fives[index]] = 3
                del(fives[index])
                break
        #get 9
        for index in range(len(sixes)):
            if(getCommons(sixes[index], sign[2]) == 4):
                code[sixes[index]] = 9
                del(sixes[index])
                break
        #get 5
        code[fives[0]] = 5
        #get 0
        for index in range(len(sixes)):
            if(getCommons(sixes[index], fives[0]) == 4):
                code[sixes[index]] = 0
                del(sixes[index])
                break
        #get 6
        code[sixes[0]] = 6
        final_case_number = ''
        for number in output:
            final_case_number += str(code[number])
        result += int(final_case_number)
    print(result)
    return result

class TestDay8(unittest.TestCase):
    def test_day_8(self):
        data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
            ]
        self.assertEqual(
            day_8(data),
            26
        )
        self.assertEqual(
            day_8_part_2(data),
            61229
        )
    def test_day_8_final(self):
        f = open("day_8.txt", "r")
        data = [elm for elm in f.read().splitlines()]
        f.close()
        self.assertTrue(
            day_8(data)
        )
        self.assertTrue(
            day_8_part_2(data)
        )
if __name__ == '__main__':
    unittest.main()