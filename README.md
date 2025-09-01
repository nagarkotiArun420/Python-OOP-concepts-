# Python Object-Oriented Programming Examples

This repository contains comprehensive examples demonstrating key Object-Oriented Programming (OOP) concepts in Python. The code covers class creation, inheritance patterns, abstraction, polymorphism, and advanced OOP implementations.

---

📚 **Table of Contents**

* Features
* Code Examples
* Getting Started
* Concepts Covered
* Usage
* Contributing
* License

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

**Key Features:**

* Constructor method (`__init__`)
* Instance variables
* Object methods
* Object creation and method calling

---

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

**Key Features:**

* Class variables vs instance variables
* Automatic counting of objects
* Shared attributes across all instances

---

### Inheritance

**Single Inheritance Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class Dog(Animal):
    def speak(self):
        print("woof")
```

**Multilevel and Multiple Inheritance:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Prey(Animal):
    def flee(self):
        print("The animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("The animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass
```

**Key Features:**

* Parent-child relationship
* Grandparent → Parent → Child hierarchy
* Multiple inheritance and method resolution order (MRO)

---

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

class Car(Vehicle):
    def go(self):
        print("you drive the car")
    def stop(self):
        print("You stop the car")
```

**Key Features:**

* Abstract base class (`ABC`)
* Enforced implementation of abstract methods in subclasses

---

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

**Key Features:**

* Method overriding
* Using `super()` to reuse parent methods

---

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

**Key Features:**

* Common interface (`area()`)
* Different implementations across subclasses

---

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

**Key Features:**

* Objects (Books) exist independently of the Library
* Library contains references to Book objects

---

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

**Key Features:**

* Car cannot exist without its Engine and Wheels
* Strong lifecycle dependency

---

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

**Key Features:**

* Class defined inside another class
* Useful for logically grouping related functionality

---

### Static Methods

```python
class Employee:
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
```

**Key Features:**

* Utility methods tied to the class itself
* No access to `self` or `cls`

---

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

**Key Features:**

* Operates on class-level data
* Can be used to compute aggregates like student count and average GPA

---

## 🏃‍♂️ Getting Started

**Prerequisites:**

* Python 3.x installed
* Basic understanding of programming concepts

**Running the Code:**

```bash
git clone [your-repository-url]
cd python-oop-examples
python main.py
```

**Expected Output:**

* Car object creation and method execution
* Student class variable tracking
* Inheritance examples with Animal hierarchy
* Shapes with `super()` and overridden methods
* Polymorphism with shared `area()` method
* Aggregation (Library & Books)
* Composition (Car with Engine & Wheels)
* Nested Class (Company & Employees)
* Static Method validation
* Class Method for student statistics

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

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

* Add new OOP examples
* Improve documentation
* Fix bugs or issues
* Suggest new features or concepts

---

## 📝 License

This project is open source and available under the MIT License.

---

📞 **Contact**
If you have any questions or suggestions, please open an issue in this repository.

**Happy Learning! 🐍✨**
