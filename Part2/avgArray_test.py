import unittest
import avgArray

class avgArrayTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(avgArray.avgElement([5,5,5,5,5]),5)
    def test2(self):
        self.assertEqual(avgArray.avgElement([-5,-5,-5,-5,-5]),-5)
    def test3(self):
        with self.assertRaises(ZeroDivisionError):
            avgArray.avgElement([])
            
if __name__ == '__main__':
    unittest.main(verbosity=2)