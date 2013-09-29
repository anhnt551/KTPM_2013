'''
Created on Sep 23, 2013

@author: AnhLum
'''
import unittest
import math
import decimal
from triangle import detect_triangle

class Test(unittest.TestCase):
    def testIsNumbera(self):
        self.assertEqual(detect_triangle("1",2 ,3), "Exception")
    def testIsNumberb(self):
        self.assertEqual(detect_triangle(10.9,"1",3), "Exception")
    def testIsNumberc(self):
        self.assertEqual(detect_triangle(3,4,"1"), "Exception")
    def testIsNumberab(self):
        self.assertEqual(detect_triangle("xy","-1", 4.2), "Exception")
    def testIsNumberbc(self):
        self.assertEqual(detect_triangle(4,"1","abc"), "Exception")
    def testIsNumberac(self):
        self.assertEqual(detect_triangle("-2.4",4,"1"), "Exception")
    def testIsNumberAll(self):
        self.assertEqual(detect_triangle("1","2","anh"), "Exception")
    def testNumberRangea1(self):
        self.assertEqual(detect_triangle(-1,2,2), "Exception")
    def testNumberRangea2(self):
        self.assertEqual(detect_triangle(2**33,2,2), "Exception")
    def testNumberRangea3(self):
        self.assertEqual(detect_triangle(0,2,2), "Exception")
    def testNumberRangeb1(self):
        self.assertEqual(detect_triangle(2**33,-2,2), "Exception")
    def testNumberRangeb2(self):
        self.assertEqual(detect_triangle(2**33,0,2), "Exception")
    def testNumberRangeb3(self):
        self.assertEqual(detect_triangle(2**33,2**33,2), "Exception")
    def testNumberRangec1(self):
        self.assertEqual(detect_triangle(2**33,3,2**33), "Exception")
    def testNumberRangec2(self):
        self.assertEqual(detect_triangle(2**33,7,0), "Exception")
    def testNumberRangec3(self):
        self.assertEqual(detect_triangle(2**33,2,-10.4), "Exception")
    def testNumberRangeAll(self):
        self.assertEqual(detect_triangle(2**33,0,-10.4), "Exception")
    def testIsBalance1(self):
        self.assertEqual(detect_triangle(1,2,2), "triangle is balance")
    def testIsBalance2(self):
        self.assertEqual(detect_triangle(1,2.5,2.5), "triangle is balance")
    def testIsBalance3(self):
        self.assertEqual(detect_triangle(0.1,0.1,0.05), "triangle is balance")
    def testIsSquareAndBalance(self):
        self.assertEqual(detect_triangle(2,2,2*math.sqrt(2)), 'triangle is square and balance')
    def testIsNormal1(self):
        self.assertEqual(detect_triangle(1.1,2.2,3.2), 'triangle is normal')
    def testIsNormal2(self):
        self.assertEqual(detect_triangle(2.4,2**32-1, 2**31-1-1), 'triangle is normal')
    def testIsTriangleMaximum(self):
        self.assertEqual(detect_triangle(1,1,2**31-1), "Not triangle")
    def testIsTriangle(self):
        self.assertEqual(detect_triangle(2,3,10), 'Not triangle')
    def testIsRegular1(self):
        self.assertEqual(detect_triangle(2.0,2.0,2), "triangle is regular")
    def testIsRegular2(self):
        self.assertEqual(detect_triangle(2**31-1,2**31-1,2**31-1), "triangle is regular")
    

if __name__ == "__main__":
    unittest.main()