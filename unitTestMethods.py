#assertEqual(a,b)

#assertNotEqual(a,b) # Values Not Equal

#assertTrue(a)  Returns True

#assertFalse(a) Returns False

#assertIsNone(x) Returns no object
#assertIsNotNone(x) Returns an object

#assertIn(a,b) b--> List / tuple 
#assertNotIn(a,b) b--> List / tuple 

#assertIsInstance(a,b) --> To check if the return value is an object of the specifiec class
#assertNotIsInstance(a,b) --> To check if the return value is NOT an object of the specifiec class

import TestFunctions
import unittest
class TestFunction(unittest.TestCase):
    def test_getrandom(self):
        self.assertNotEqual(TestFunctions.getRandom(),-1)
        self.assertIn(TestFunctions.getRandom(),list(range(1,11)))
    def test_checkpercentage(self):
        self.assertTrue(TestFunctions.checkPercentage(50))
        self.assertFalse(TestFunctions.checkPercentage(500))
        self.assertTrue(TestFunctions.checkPercentage(50))
    
    def test_checkobject(self):
        self.assertIsNone(TestFunctions.checkObject())

    def test_checkStudent(self):
        self.assertIsInstance(TestFunctions.returnStudent(),TestFunctions.Student)
        

if __name__=='__main__':
    unittest.main()
        

