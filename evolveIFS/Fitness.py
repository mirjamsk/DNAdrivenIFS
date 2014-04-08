import math

class Fitness():
    #p = 3
    @staticmethod
    def euclideanDistance( point1, point2):
        return  (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 
    
    @staticmethod
    def manhattanDistance( point1, point2):
        return abs( point1[0]-point2[0]) + math.fabs(point1[1]-point2[1])
    
    @staticmethod
    def minkowskiDistance( point1, point2, p = 3):
        return  (point1[0]-point2[0])**p + (point1[1]-point2[1])**p
    
    @staticmethod
    def minMax(cls, m1, m2, fp1, fp2):
        medianEuclidean = cls.euclideanDistance(m1, m2)
        mFpEucl1 =cls.euclideanDistance(m1, fp1)
        mFpEucl2 =cls.euclideanDistance(m2, fp2)
        
        return abs(medianEuclidean - (mFpEucl1+ mFpEucl2))
           
   
    