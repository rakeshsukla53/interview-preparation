# what is interface

Interface are those classes which is kind of a template which tells you exactly what your classes must have 

for example lets take a class `Shape`

    class Shape(object):
    
        def area(self):
        
        def perimeter(self):
        
Every `Shape` class must have `area` and `perimeter` as two properties 

We will never directly use the `Shape Class` 

# python provides an module to define the class as abstract 

    from abc import ABCMeta, abstractmethod
    
Abstract methods must be overridden
 
 
# define the methods as `Abstract` 

    class Shape(object):
    
            __metaclass__ = ABCMeta
            
            @abstractmethod
            def area(self):
            
            @abstractmethod
            def perimeter(self):

Without overridding these abstract classes you cannot use the `Shape` class here

# Now inheriting `Rectangle` class 


       class Rectangle(Shape):
       
            def __init__(self, width, length):
                self.width = width
                self.length = length
                
                super(Rectangle, self).__init__()
    
                # we must override the abstract method here     
             
            def area(self):
                
                return self.width * self.length
                
            def perimeter(self):
            
                return 2 * (self.width + self.length)
       
       