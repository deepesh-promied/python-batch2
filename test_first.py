import unittest
import first
lst = [[10,15,25],[10,-5,5],[25,25,50]]

class testFirst(unittest.TestCase):
    def test_sum(self):
        for x in lst:
            self.assertEqual(first.sum(x[0],x[1]),x[2])
    def test_product(self):
        self.assertEqual(first.product(5,2),10)
        self.assertEqual(first.product(5,-3),-15)
    def test_product(self):
        self.assertEqual(first.product(5,2),10)

if __name__=='__main__':
    unittest.main()