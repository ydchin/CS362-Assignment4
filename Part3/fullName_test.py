import unittest
import fullName

class fullNameTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fullName.fullName("Dylan", "Chin"), "Dylan Chin")
    def test2(self):
        with self.assertRaises(TypeError):
            fullName.fullName(1,"Chin")
    def test3(self):
        with self.assertRaises(Exception):
            fullName.fullName("Dylan", "")
            
if __name__ == '__main__':
    unittest.main(verbosity=2)