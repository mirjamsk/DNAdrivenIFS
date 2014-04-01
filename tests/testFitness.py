'''
Created on 31. 3. 2014.

@author: Monsieur
'''
import unittest
import math
from Fitness import Fitness

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testEuclideanDistance(self):
        p1 = (10,3)
        p2 = (8,6)
        
        self.assertEqual(Fitness.getFitnessValue(p1,p2), math.sqrt(13),
                         "test EuclideanDistance is: %f, but should be %f" %(Fitness.getFitnessValue(p1,p2), math.sqrt(13)))
        
    def testManhattanDistance(self):
        p1 = (10,3)
        p2 = (8,6)
        Fitness.setDistanceFunction("manhattan")
        self.assertEqual(Fitness.getFitnessValue(p1,p2),5,
                         "test ManhattanDistance is: %f, but should be %f" %(Fitness.getFitnessValue(p1,p2), 5))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()