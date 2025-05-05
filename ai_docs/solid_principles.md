# SOLID Principles in Python

This document outlines the SOLID principles of object-oriented design and programming, with specific examples in Python. These principles are fundamental to writing maintainable, scalable, and robust code.

## 1. Single Responsibility Principle (SRP)

**A class should have only one reason to change, meaning it should have only one job or responsibility.**

### Example:
```python
# Bad: Class handling both user data and file operations
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_file(self):
        with open('users.txt', 'a') as f:
            f.write(f"{self.name},{self.email}\n")

# Good: Separate responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save_to_file(self, user):
        with open('users.txt', 'a') as f:
            f.write(f"{user.name},{user.email}\n")
```

## 2. Open/Closed Principle (OCP)

**Software entities should be open for extension but closed for modification.**

### Example:
```python
# Bad: Modifying existing class for new shapes
class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius

# Good: Using abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
```

## 3. Liskov Substitution Principle (LSP)

**Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.**

### Example:
```python
# Bad: Square inheriting from Rectangle violates LSP
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Good: Using composition or separate classes
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
```

## 4. Interface Segregation Principle (ISP)

**Clients should not be forced to depend on methods they do not use.**

### Example:
```python
# Bad: Single interface with many methods
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass

# Good: Segregated interfaces
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Sleepable:
    def sleep(self):
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")
```

## 5. Dependency Inversion Principle (DIP)

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

### Example:
```python
# Bad: High-level module depends on low-level module
class LightBulb:
    def turn_on(self):
        print("Light bulb turned on")
    
    def turn_off(self):
        print("Light bulb turned off")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()
    
    def operate(self):
        self.bulb.turn_on()

# Good: Both depend on abstraction
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb turned on")
    
    def turn_off(self):
        print("Light bulb turned off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
    
    def operate(self):
        self.device.turn_on()
```

## Best Practices for This Project

When contributing to this project, please adhere to these principles by:

1. Creating focused, single-purpose classes and functions
2. Using abstractions and interfaces to make code extensible
3. Ensuring subclasses can be used in place of their parent classes
4. Breaking down large interfaces into smaller, more specific ones
5. Depending on abstractions rather than concrete implementations

Remember that while these principles are important, they should be applied judiciously and not at the expense of code clarity or practicality. 