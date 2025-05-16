from abc import abstractmethod , ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.length= height
        self.width= width

    def area(self):
        return self.length * self.width