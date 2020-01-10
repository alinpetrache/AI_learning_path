#Python 3
import math

class Vector():
    def __init__(self, *coordinates):
        #Define vector
        self.coordinates = coordinates

    def __str_(self):
        return '{}'.format(self.coordinates)

    def plus (self, other): 
        #1.1. Add vectors
        new_coordinates = [x+y for x,y in zip(self.coordinates, other.coordinates)]
        #new_coordinates = ['%.3f' % n for n in new_coordinates]
        return Vector(new_coordinates)
    
    def times_scalar(self,c):
        #1.1. Scalar multiplication
        return Vector((c*x for x in self.coordinates))    
    
    def magnitude(self):
        #1.2. Calculate the length of the vector
        coordinates_squared = (x**2 for x in self.coordinates)
        return math.sqrt(sum(coordinates_squared))

    def normalize(self):
        #1.2. Get the unity vector
        try:
            magnitude = self.magnitude()
            return Vector(self.times_scalar(1./magnitude))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot (self, other):
        #1.3. Calculate Dot Product 
        return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])
         
    def angle(self, other, in_degrees=False):
        #1.3. Calculate the Angle between vectors
            dot = self.dot(other)
            magnitude_v1 = self.magnitude()
            magnitude_v2 = other.magnitude()
            if (magnitude_v1 != 0) and (magnitude_v2 != 0):
                res = dot/(magnitude_v1*magnitude_v2)
            else:
                raise Exception('Can''t divide by zero')
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
    
    def projection(self, basis):
        #1.5. Calculate projection of a vector on another one
        u = basis.normalize()
        weight = self.dot(basis) 
        return u
        


v = Vector(3.039, 1.879)
w = Vector(0.825, 2.036)
c = 2
print("Vector: ", v)
print ("Plus: ", v.plus(w))
print ("Times scalar:", v.times_scalar(c))
print ('Magnitude', w.magnitude())
print("Normalize: ", w.normalize())
print ('Dot product: ', v.dot(w))
print ('Angle (radian): ', v.angle(w))
print ('Angle (degrees): ', v.angle(w, in_degrees=True))
print ('Is parallel: ', v.is_parallel_to(w))
print ('Is orthogonal: ', v.is_orthogonal_to(w))
print ("Projection: ", v.projection(w))








