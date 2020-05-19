import unittest
import StudentClass

test_cases = [('Divyansh',10,20,30,60),('Saransh',10,25,35),('Anvi',25,35,45,105)]
class TestStudent(unittest.TestCase):
    def test_getTotal(self):
        for x in test_cases:
            a,*b,c = x
            s1 = StudentClass.Student(a,*b)
            self.assertEqual(s1.getTotal(),c)

class TestSection(unittest.TestCase):
    pass

if __name__=='__main__':
    unittest.main()