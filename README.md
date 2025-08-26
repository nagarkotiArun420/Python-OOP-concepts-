Python Object-Oriented Programming Examples
This repository contains comprehensive examples demonstrating key Object-Oriented Programming (OOP) concepts in Python. The code covers class creation, inheritance patterns, and practical implementations.
📚 Table of Contents

Features
Code Examples
Getting Started
Concepts Covered
Usage
Contributing

🚀 Features

Class Creation & Object Initialization: Learn how to create classes and initialize objects with constructors
Instance & Class Variables: Understand the difference between instance and class-level attributes
Single Inheritance: Explore parent-child class relationships
Multilevel Inheritance: Implement grandparent-parent-child hierarchies
Multiple Inheritance: Demonstrate classes inheriting from multiple parents

📋 Code Examples
1. Class Creation and Object Initialization
pythonclass Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
Key Features:

Constructor method (__init__)
Instance variables
Object methods (drive, stop)
Object creation and method calling

2. Class Variables
pythonclass Student:
    class_year = 2024  # Class variable
    num_students = 0   # Class variable shared by all instances
Key Features:

Class variables vs instance variables
Automatic student counting
Shared data across all instances

3. Single Inheritance
pythonclass Animal:  # Parent class
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class Dog(Animal):  # Child class
    def speak(self):
        print("woof")
Key Features:

Parent-child relationship
Method inheritance
Method overriding capabilities

4. Multilevel & Multiple Inheritance
python# Multilevel: Animal -> Prey/Predator -> Rabbit/Hawk
class Animal:        # Grandparent
class Prey(Animal):  # Parent
class Rabbit(Prey):  # Child

# Multiple: Fish inherits from both Prey and Predator
class Fish(Prey, Predator):
    pass
Key Features:

Grandparent-parent-child hierarchy
Multiple inheritance patterns
Method resolution order

🏃‍♂️ Getting Started
Prerequisites

Python 3.x installed on your system
Basic understanding of programming concepts

Running the Code

Clone this repository:

bashgit clone [your-repository-url]
cd python-oop-examples

Run the Python file:

bashpython main.py
Expected Output
The script will demonstrate:

Car object creation and method execution
Student class variable tracking
Animal inheritance hierarchy with different behaviors
Multilevel inheritance examples

🎯 Concepts Covered
ConceptDescriptionExample ClassClass CreationDefining classes with attributes and methodsCarConstructorObject initialization with __init__ methodAll classesInstance VariablesAttributes unique to each objectself.name, self.modelClass VariablesAttributes shared across all instancesStudent.class_yearMethod DefinitionFunctions within classesdrive(), speak()Single InheritanceClass inheriting from one parentDog(Animal)Multilevel InheritanceChain of inheritanceAnimal -> Prey -> RabbitMultiple InheritanceInheriting from multiple parentsFish(Prey, Predator)
💡 Usage Examples
Creating and Using Objects
python# Create car objects
car1 = Car("Mustang", 2023, "Red", False)
car2 = Car("Ferrari", 2024, "Blue", True)

# Use object methods
car1.drive()  # Output: "You drive the car"
print(vars(car1))  # Display object attributes
Working with Inheritance
python# Create animals with inherited behaviors
dog = Dog("Scooby")
dog.eat()    # Inherited from Animal
dog.speak()  # Dog-specific method

# Multiple inheritance example
fish = Fish("Nemo")
fish.flee()  # From Prey parent
fish.hunt()  # From Predator parent
🔧 Customization
Feel free to extend these examples by:

Adding new methods to existing classes
Creating additional inheritance hierarchies
Implementing method overriding
Adding property decorators
Exploring advanced OOP concepts like polymorphism

🤝 Contributing
Contributions are welcome! Please feel free to:

Add new OOP examples
Improve existing code documentation
Fix any bugs or issues
Suggest new features or concepts to cover

📝 License
This project is open source and available under the MIT License.
📞 Contact
If you have any questions or suggestions, please feel free to reach out or open an issue in this repository.

Happy Learning! 🐍✨
