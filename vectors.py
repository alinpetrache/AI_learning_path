import numpy as np
import math

class Vector():
    def __init__(self, *coordinates):
        #Define vector
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('Nu exista coordonate!')
        except TypeError:
            raise TypeError('Coordonatele trebuie sa fie iterabile!')

    def plus (self, other): 
        #1.1. Add two vectors
        new_coordinates = [x+y for x,y in zip(self.coordinates, other.coordinates)]
        new_coordinates = ['%.3f' % n for n in new_coordinates]
        return Vector(new_coordinates)
    
    def times_scalar(self,c):
        #1.1. Scalar multiplication
        return (tuple(c*x for x in self.coordinates))
            
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)  

    '''
    def __eq__ (self, other):
        return self.coordinates == other.coordinates
    '''

    def magnitude(self):
        #1.2. Calculate the length of the vector
        coordinates_squared = (x**2 for x in self.coordinates)
        return math.sqrt(sum(coordinates_squared))
    
    def normalize(self):
        #1.2. Get the unity vector
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Eroare: nu pot imparti la 0')

    def dot (self, other):
        #1.3. Calculate Dot Product 
        return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])
       
    def angle(self, other, in_degrees=False):
        #1.3. Calculate the Angle between vectors
        dot = self.dot(other)
        magnitude_v1 = self.magnitude()
        magnitude_v2 = other.magnitude()
        res = dot/(magnitude_v1*magnitude_v2)
        angle_in_redians = math.acos(res)        
        if in_degrees:
            degrees_per_radian = 180. / math.pi
            return angle_in_redians * degrees_per_radian
        else: 
            return angle_in_redians

    def is_zero(self, tolerance = 1e-10):
        #1.4. Check if the vector length is zero
        return self.magnitude() < tolerance

    def is_parallel_to(self, other):
        #1.4. Verify parallelism
        return (self.is_zero() or other.is_zero() or self.angle(other) == 0 or self.angle(other) == math.pi)
    
    def is_orthogonal_to(self, other, tolerance=1e-10):
        ##1.4. Verify orthogonality
        return abs(self.dot(other)) < tolerance
        

'''
v = Vector(8.218,-9.341)
w = Vector(-1.129,2.111)
print (v.plus(w))

v = Vector(7.35,0.221,5.188)
w = Vector(2.751,8.259,3.985)
print ('Magnitude', '{:.3f}'.format(v.magnitude()))
'''
v = Vector(-7.579,-7.88)
w = Vector(22.737,23.64)
print ('First!')
print ('Is parallel: ', v.is_parallel_to(w))
print ('Is orthogonal: ', v.is_orthogonal_to(w))

v = Vector(5.581,-2.221)
print ('Normalize: ', v.normalize())
'''
v = Vector(-5.955,-4.904,-1.874)
w = Vector(-4.496,-8.755,7.103)
print ('Dot product: ', v.dot(w))


v = Vector(3.183,-7.627)
w = Vector(-2.668,5.319)
print ('Angle (radian): ', v.angle(w))

v = Vector(7.35, 0.221, 5.188)
w = Vector(2.751, 8.259, 3.985)
print ('Angle (degrees): ', v.angle(w, in_degrees=True))


v = Vector(7.35, 0.221, 5.188)
w = Vector(2.751, 8.259, 3.985)
print ('Angle (degrees): ', v.angle(w, in_degrees=True))
'''







