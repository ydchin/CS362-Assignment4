import unittest
import cube

class testCubeVol(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.cubeVol(3), 27)
    def test2(self):
        with self.assertRaises(Exception):
            cube.cubeVol(-2)
    def test3(self):
        with self.assertRaises(TypeError):
            cube.cubeVol("hi")

if __name__ == '__main__':
    unittest.main(verbosity=2)