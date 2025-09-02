# Python Object-Oriented Programming Examples

This repository contains comprehensive examples demonstrating key Object-Oriented Programming (OOP) concepts in Python. The code covers class creation, inheritance patterns, abstraction, polymorphism, and advanced OOP implementations.

---

📚 **Table of Contents**

- [🚀 Features](#-features)  
- [📋 Code Examples](#-code-examples)  
  - [Class Creation and Object Initialization](#class-creation-and-object-initialization)  
  - [Class Variables](#class-variables)  
  - [Inheritance](#inheritance)  
  - [Abstraction](#abstraction)  
  - [Method Overriding & super()](#method-overriding--super)  
  - [Polymorphism](#polymorphism)  
  - [Aggregation](#aggregation)  
  - [Composition](#composition)  
  - [Nested Classes](#nested-classes)  
  - [Static Methods](#static-methods)  
  - [Class Methods](#class-methods)  
  - [Magic Methods](#magic-methods)  
  - [Property Decorator](#property-decorator)  
- [🏃‍♂️ Getting Started](#-getting-started)  
- [🎯 Concepts Covered](#-concepts-covered)  
- [🖥 Usage / Expected Output](#-usage--expected-output)  
- [🤝 Contributing](#-contributing)  
- [📝 License](#-license)  

---

## 🚀 Features

* **Class Creation & Object Initialization**: Create classes, constructors, and object methods  
* **Instance & Class Variables**: Differentiate between instance and shared class-level attributes  
* **Inheritance**: Demonstrates single, multilevel, and multiple inheritance  
* **Abstraction**: Using abstract base classes with `abc`  
* **Method Overriding & super()**: Extend parent methods while customizing behavior  
* **Polymorphism**: Implement shared interfaces across different classes  
* **Aggregation**: Objects referencing other independent objects  
* **Composition**: Objects composed of dependent sub-objects  
* **Nested Classes**: Classes defined inside other classes  
* **Static Methods**: Utility functions tied to the class, not instances  
* **Class Methods**: Operate on class-level data rather than individual instances  
* **Magic Methods (Dunder Methods)**: Customize object behavior with `__str__`, `__eq__`, `__lt__`, etc.  
* **Property Decorator**: Manage attributes with getters, setters, and deleters  

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

### Class Variables
```python
class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class Dog(Animal):
    def speak(self):
        print("woof")
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

### Method Overriding & `super()`
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
```

### Polymorphism
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings
```

### Aggregation
```python
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
```

### Composition
```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
```

### Nested Classes
```python
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
```

### Static Methods
```python
class Employee:
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
```

### Class Methods
```python
class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}" if cls.count else 0
```

### Magic Methods
```python
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
```

### Property Decorator
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width} inch"

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self._width = value

    @property
    def height(self):
        return f"{self._height} inch"

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self._height = value

    @property
    def area(self):
        return f"{self._width * self._height} square inch"

    @height.deleter
    def height(self):
        del self._height
```

---

## 🏃‍♂️ Getting Started

**Prerequisites:**
* Python 3.x installed  

**Running the Code:**
```bash
git clone [your-repository-url]
cd python-oop-examples
python main.py
```

---

## 🎯 Concepts Covered

| Concept                | Description                               | Example                      |
| ---------------------- | ----------------------------------------- | ---------------------------- |
| Class                  | Define objects with attributes & methods  | `Car`, `Student`             |
| Constructor            | Object initialization                     | `__init__` methods           |
| Instance Variables     | Attributes unique to each object          | `self.name`                  |
| Class Variables        | Shared attributes across instances        | `Student.class_year`         |
| Inheritance            | Parent-child relationships                | `Dog(Animal)`                |
| Multilevel Inheritance | Chain of inheritance                      | `Animal -> Prey -> Rabbit`   |
| Multiple Inheritance   | Inheriting from multiple parents          | `Fish(Prey, Predator)`       |
| Abstraction            | Abstract classes with `abc`               | `Vehicle`                    |
| Method Overriding      | Redefine parent method in child class     | `desc()` in Shapes           |
| super()                | Call parent class methods                 | `super().desc()`             |
| Polymorphism           | Same method across multiple classes       | `area()` in Shapes           |
| Aggregation            | Objects containing independent objects    | `Library & Book`             |
| Composition            | Objects composed of dependent sub-objects | `Car with Engine`            |
| Nested Classes         | Classes inside other classes              | `Company.Employee`           |
| Static Methods         | Class utility methods                     | `Employee.is_valid_position` |
| Class Methods          | Work with class-level data                | `Student.get_count()`        |
| Magic Methods          | Customize object behavior                 | `__str__`, `__eq__`, `__add__`|
| Property Decorator     | Getter, Setter, Deleter as attributes     | `Rectangle.width`            |

---

## 🖥 Usage / Expected Output

Running `main.py` will demonstrate:  
* Car creation & driving  
* Student count and GPA tracking  
* Inheritance with animals  
* Shapes using `super()`  
* Polymorphism with `area()`  
* Library aggregation with books  
* Car composition with Engine & Wheels  
* Nested classes in Company  
* Static and Class methods  
* Magic methods (`book1 + book2`, `keyword in book`)  
* Property decorator (`rectangle.width`, `del rectangle.height`)  

---

## 🤝 Contributing

Contributions are welcome! Feel free to:  
* Add new OOP examples  
* Improve documentation  
* Fix issues or suggest improvements  

---

## 📝 License

This project is open source and available under the MIT License.  

---

📞 **Contact**  
If you have any questions or suggestions, please open an issue in this repository.  

**Happy Learning! 🐍✨**
