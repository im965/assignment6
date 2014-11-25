from myexceptions import *
from interval import *
import unittest


#test mergeIntervals
class TestmergeIntervals(unittest.TestCase):
    def setUp(self):
        self.itema = interval("[5,10]")
	self.itemb = interval("(5,10)")
        self.mymerge = mergeIntervals(self.itema,self.itemb)
    def test_interior(self):
        self.assertEqual(self.mymerge.leftreal, self.itema.leftreal)  

#test mergeOverlapping
class TestmergeOverlapping(unittest.TestCase):
    def setUp(self):
        self.itema = interval("[5,10]")
	self.itemb = interval("(7,12)")
	self.itemc = interval("(15,20)")
        self.mymerge = mergeOverlapping([self.itema,self.itemb,self.itemc])
    def test_overlap(self):
        self.assertEqual(len(self.mymerge), 2) 


#test insert
class Testinsert(unittest.TestCase):
    def setUp(self):
        self.itema = interval("[5,10]")
	self.itemb = interval("(7,12)")
	self.itemc = interval("(15,20)")
        self.inserted = insert([self.itema,self.itemc],self.itemc)
    def test_insert(self):
        self.assertEqual(len(self.inserted), 2) 


if __name__ == '__main__':
    unittest.main()
