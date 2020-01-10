#Python 3
import math

class Vector():
    def __init__(self, *coordinates):
        #Define vector
        self.coordinates = coordinates
        
    def get_vector(self):
       # return '{}'.format(self.coordinates) 
       return self.coordinates

    def plus (self, other): 
        #1.1. Add vectors
        new_coordinates = [x+y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)

    def minus (self, other): 
        #1.1. Substract vectors
        new_coordinates = [x-y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)

    def times_scalar(self,c):
        #1.1. Scalar multiplication
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(*new_coordinates)   
    
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
    
    def parallel_component(self, basis):
        #1.5. Calculate projection of a vector on another one
        u = basis.normalize()
        weight = self.dot(u) 
        return u.times_scalar(weight) 
    
    def orthogonal_component(self, other):
        #1.5. Calculate the orthogonal component of a vector on another 
        projection = self.parallel_component(other)
        return self.minus(projection)

    

v = Vector(3.009, -6.172, 3.692, -2.51)
w = Vector(6.404, -9.144, 2.759, 8.718)
c = 2
print("Vector: ", v.get_vector())
print ("Plus: ", v.plus(w).get_vector())
print ("Minus: ", v.minus(w).get_vector())
print ("Times scalar:", v.times_scalar(c).get_vector())
print ('Magnitude', w.magnitude())
print("Normalize: ", w.normalize().get_vector())
print ('Dot product: ', v.dot(w))
print ('Angle (radian): ', v.angle(w))
print ('Angle (degrees): ', v.angle(w, in_degrees=True))
print ('Is parallel: ', v.is_parallel_to(w))
print ('Is orthogonal: ', v.is_orthogonal_to(w))
print ("Parallel component: ", v.parallel_component(w).get_vector())
print ("Orthogonal component: ", v.orthogonal_component(w).get_vector())