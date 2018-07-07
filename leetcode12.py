import unittest

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r_map = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'],['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C'],['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M'],['M', 'MM', 'MMM', ]]
        tmpStr=''
        count = 0
        if num > 4000 :
            return ''
        while True:
            if num > 0 :
                mod_num=num%10
                idx = mod_num -1
                if idx >=0 :
                    tmpStr = r_map[count][idx] + tmpStr
                count += 1
                num /= 10
            else:
                break
        return tmpStr
        
class UT(unittest.TestCase):

    def test_case1(self):
        s = Solution()
        self.assertEqual(s.intToRoman(1), 'I')
        self.assertEqual(s.intToRoman(2), 'II')
        self.assertEqual(s.intToRoman(3), 'III')
        self.assertEqual(s.intToRoman(4), 'IV')
        self.assertEqual(s.intToRoman(5), 'V')
        self.assertEqual(s.intToRoman(6), 'VI')
        self.assertEqual(s.intToRoman(7), 'VII')
        self.assertEqual(s.intToRoman(8), 'VIII')
        self.assertEqual(s.intToRoman(9), 'IX')
        self.assertEqual(s.intToRoman(10), 'X')
        self.assertEqual(s.intToRoman(11), 'XI')
        self.assertEqual(s.intToRoman(20), 'XX')
        self.assertEqual(s.intToRoman(30), 'XXX')
        self.assertEqual(s.intToRoman(40), 'XL')
        self.assertEqual(s.intToRoman(50), 'L')
        self.assertEqual(s.intToRoman(60), 'LX')
        self.assertEqual(s.intToRoman(70), 'LXX')
        self.assertEqual(s.intToRoman(80), 'LXXX')
        self.assertEqual(s.intToRoman(90), 'XC')
        self.assertEqual(s.intToRoman(100), 'C')
        self.assertEqual(s.intToRoman(110), 'CX')
        self.assertEqual(s.intToRoman(111), 'CXI')
        self.assertEqual(s.intToRoman(1111), 'MCXI')
        self.assertEqual(s.intToRoman(100), 'C')
        self.assertEqual(s.intToRoman(200), 'CC')
        self.assertEqual(s.intToRoman(300), 'CCC')
        self.assertEqual(s.intToRoman(400), 'CD')
        self.assertEqual(s.intToRoman(500), 'D')
        self.assertEqual(s.intToRoman(600), 'DC')
        self.assertEqual(s.intToRoman(700), 'DCC')
        self.assertEqual(s.intToRoman(800), 'DCCC')
        self.assertEqual(s.intToRoman(900), 'CM')
        self.assertEqual(s.intToRoman(1000), 'M')
        self.assertEqual(s.intToRoman(1776), 'MDCCLXXVI')
        self.assertEqual(s.intToRoman(1954), 'MCMLIV')
        self.assertEqual(s.intToRoman(1990), 'MCMXC')
        self.assertEqual(s.intToRoman(2014), 'MMXIV')
        self.assertEqual(s.intToRoman(2018), 'MMXVIII')
        self.assertEqual(s.intToRoman(1994), 'MCMXCIV')
        
        
if __name__ == '__main__':
    unittest.main()
