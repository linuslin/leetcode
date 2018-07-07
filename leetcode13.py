import unittest

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_map_1 = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        r_map_2 = { 'CM':900, 'XC':90, 'IX':9, 'IV':4, 'XL':40, 'CD':400 }
        count = 0
        while len(s) > 0:
            if len(s) > 1 :
                #print s[-2:]
                if s[-2:] in r_map_2:
                    count += r_map_2[s[-2:]]
                    s = s[:-2]
                    #print 'sub s2' , s, 'len(s2)', len(s)
                    continue
            
            #print s[-1:]
            if s[-1:] in r_map_1:
                count += r_map_1[s[-1:]]
                s = s[:-1]
                #print 'sub s1 ', s , 'len(s1)', len(s)
            #else:
                #print 'config error'
        return count
        
        
        
class UT(unittest.TestCase):

    def test_case2(self):
        s = Solution()
        self.assertEqual(s.romanToInt(''), 0 )
        self.assertEqual(s.romanToInt('I'), 1 )
        self.assertEqual(s.romanToInt('II'), 2)
        self.assertEqual(s.romanToInt('III'), 3)
        self.assertEqual(s.romanToInt('IV'), 4)
        self.assertEqual(s.romanToInt('V'), 5)
        self.assertEqual(s.romanToInt('VI'), 6)
        self.assertEqual(s.romanToInt('VII'), 7)
        self.assertEqual(s.romanToInt('VIII'), 8)
        self.assertEqual(s.romanToInt('IX'), 9)
        self.assertEqual(s.romanToInt('X'), 10)
        self.assertEqual(s.romanToInt('XI'), 11)
        self.assertEqual(s.romanToInt('XX'), 20)
        self.assertEqual(s.romanToInt('XXX'), 30)
        self.assertEqual(s.romanToInt('XL'), 40)
        self.assertEqual(s.romanToInt('L'), 50)
        self.assertEqual(s.romanToInt('LX'), 60)
        self.assertEqual(s.romanToInt('LXX'), 70)
        self.assertEqual(s.romanToInt('LXXX'), 80)
        self.assertEqual(s.romanToInt('XC'), 90)
        self.assertEqual(s.romanToInt('C'), 100)
        self.assertEqual(s.romanToInt('CX'), 110)
        self.assertEqual(s.romanToInt('CXI'), 111)
        self.assertEqual(s.romanToInt('MCXI'), 1111)
        self.assertEqual(s.romanToInt('CC'), 200)
        self.assertEqual(s.romanToInt('CCC'), 300)
        self.assertEqual(s.romanToInt('CD'), 400)
        self.assertEqual(s.romanToInt('D'), 500)
        self.assertEqual(s.romanToInt('DC'), 600)
        self.assertEqual(s.romanToInt('DCC'), 700)
        self.assertEqual(s.romanToInt('DCCC'), 800)
        self.assertEqual(s.romanToInt('CM'), 900)
        self.assertEqual(s.romanToInt('M'), 1000)
        self.assertEqual(s.romanToInt('MDCCLXXVI'), 1776)
        self.assertEqual(s.romanToInt('MCMLIV'), 1954)
        self.assertEqual(s.romanToInt('MCMXC'), 1990)
        self.assertEqual(s.romanToInt('MMXIV'), 2014)
        self.assertEqual(s.romanToInt('MMXVIII'), 2018)
        self.assertEqual(s.romanToInt('MCMXCIV'), 1994)
        
if __name__ == '__main__':
    unittest.main()
