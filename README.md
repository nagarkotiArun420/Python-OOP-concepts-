# Python Object-Oriented Programming Examples

This repository contains comprehensive examples demonstrating key Object-Oriented Programming (OOP) concepts in Python. The code covers class creation, inheritance patterns, and practical implementations.  

---

## 📚 Table of Contents

- [Features](#-features)  
- [Code Examples](#-code-examples)  
- [Getting Started](#-getting-started)  
- [Concepts Covered](#-concepts-covered)  
- [Usage](#-usage)  
- [Contributing](#-contributing)  
- [License](#-license)  

---

## 🚀 Features

- **Class Creation & Object Initialization**: Learn how to create classes and initialize objects with constructors  
- **Instance & Class Variables**: Understand the difference between instance and class-level attributes  
- **Single Inheritance**: Explore parent-child class relationships  
- **Multilevel Inheritance**: Implement grandparent-parent-child hierarchies  
- **Multiple Inheritance**: Demonstrate classes inheriting from multiple parents  
- **Method Overriding & super()**: Extend parent methods while adding custom behavior  

---

## 📋 Code Examples

### Class Creation and Object Initialization

```python
class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")
```

**Key Features**:  
- Constructor method (`__init__`)  
- Instance variables  
- Object methods  
- Object creation and method calling  

---

### Class Variables

```python
class Student:
    class_year = 2024  # Class variable
    num_students = 0   # Shared across all instances
```

**Key Features**:  
- Class variables vs instance variables  
- Automatic student counting  
- Shared data across all instances  

---

### Single Inheritance

```python
class Animal:  # Parent class
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class Dog(Animal):  # Child class
    def speak(self):
        print("woof")
```

**Key Features**:  
- Parent-child relationship  
- Method inheritance  
- Method overriding capabilities  

---

### Multilevel & Multiple Inheritance

```python
# Multilevel: Animal -> Prey/Predator -> Rabbit/Hawk
class Animal:  # Grandparent class
    pass

class Prey(Animal):
    pass

class Rabbit(Prey):
    pass

# Multiple: Fish inherits from both Prey and Predator
class Fish(Prey, Predator):
    pass
```

**Key Features**:  
- Grandparent-parent-child hierarchy  
- Multiple inheritance patterns  
- Method resolution order  

---

## 🔹 Additional Python OOP Example: Shapes with Inheritance

```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def desc(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def desc(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().desc()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def desc(self):
        print(f"It is a square with an area of {self.width * self.width}")
        super().desc()

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

    def desc(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}")
        super().desc()
```

### Example Usage

```python
circle = Circle("red", True, 5)
square = Square("blue", False, 9)
triangle = Triangle("black", True, 10, 5)

circle.desc()
square.desc()
triangle.desc()
```

### Expected Output

```
It is a circle with an area of 78.5
It is red and filled
It is a square with an area of 81
It is blue and not filled
It is a triangle with an area of 25.0
It is black and filled
```

**Key Concepts Demonstrated**:  
- Inheritance (Circle, Square, Triangle inherit Shape)  
- Method overriding (`desc()`)  
- `super()` usage to call parent methods  
- Child-specific attributes (radius, width, height)  

---

## 🏃‍♂️ Getting Started

**Prerequisites**:  
- Python 3.x installed  
- Basic understanding of programming concepts  

**Running the Code**:

```bash
git clone [your-repository-url]
cd python-oop-examples
python main.py
```

**Expected Output**:  
- Car object creation and method execution  
- Student class variable tracking  
- Animal inheritance hierarchy  
- Shapes inheritance examples with areas  

---

## 🎯 Concepts Covered

| Concept                  | Description                                  | Example                          |
|---------------------------|----------------------------------------------|----------------------------------|
| Class                     | Class creation with attributes and methods  | Car                              |
| Constructor               | Object initialization with `__init__`      | All classes                      |
| Instance Variables        | Attributes unique to each object            | `self.name`, `self.model`        |
| Class Variables           | Shared across instances                      | `Student.class_year`             |
| Method Definition         | Functions within classes                     | `drive()`, `speak()`             |
| Single Inheritance        | Class inheriting from one parent             | `Dog(Animal)`                    |
| Multilevel Inheritance    | Chain of inheritance                          | `Animal -> Prey -> Rabbit`       |
| Multiple Inheritance      | Inheriting from multiple parents             | `Fish(Prey, Predator)`           |
| Method Overriding         | Child class replacing parent method         | `desc()` in shapes               |
| `super()`                 | Call parent methods                           | `super().desc()`                 |

---

## 💡 Usage Examples

### Creating and Using Objects

```python
car1 = Car("Mustang", 2023, "Red", False)
car2 = Car("Ferrari", 2024, "Blue", True)

car1.drive()
print(vars(car1))
```

### Working with Inheritance

```python
dog = Dog("Scooby")
dog.is_alive   # inherited
dog.speak()    # dog-specific

circle = Circle("red", True, 5)
circle.desc()  # overridden + parent functionality
```

---

## 🔧 Customization

Feel free to extend these examples by:  
- Adding new methods to existing classes  
- Creating additional inheritance hierarchies  
- Implementing method overriding  
- Adding property decorators  
- Exploring advanced OOP concepts like polymorphism  

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:  
- Add new OOP examples  
- Improve existing code documentation  
- Fix any bugs or issues  
- Suggest new features or concepts to cover  

---

## 📝 License

This project is open source and available under the **MIT License**.  

---

## 📞 Contact

If you have any questions or suggestions, please open an issue in this repository.  

Happy Learning! 🐍✨
