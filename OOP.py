# Class creation and object initialization

class Car:
    def __init__(self,model,year,colour,for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

car1 = Car("Mustang",2023,"Red",False)
car2 = Car("Ferrari", 2024, "Blue" , True)

print(vars(car1))
car1.drive()
print(vars(car2))
car2.stop()


# CLASS VARIABLES

class Student:

    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students +=1
        

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward",55)
student4 = Student("Sandy",27)


print(f"My graduating class of {Student.class_year} has {Student.num_students}")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

#INHERITANCE
#Multiple inheritance - inherit from more than one parent

class Animal: # Class name
    def __init__(self, name): # constructor
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("woof")
        

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("chi chi")
        
dog = Dog("Scooby")
cat = Cat("Meow")
Mouse = Mouse("chi chi")

print(dog.name)
print(dog.is_alive)
cat.eat()
dog.sleep()




# multilevel inheritance - granparent inheritance

# Grand parent
class Animal:

    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f" {self.name} is eating")
    def sleep(self):
        print(f" {self.name} is sleeping")

# Parent
class Prey(Animal):
    def flee(self):
        print(f"The animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"The animal is hunting")

# Children
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.eat()

# Abstraction

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

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("You stop the motocycle")


class Boat(Vehicle):

    def go(self):
        print("you sail the boat")

    def stop(self):
        print("You stop the boat")

boat = Boat()
boat.go()
boat.stop()

# Super - allows to extend the fuctionality of a inherited method also lets us inherit the functions



class Shape:
    def __init__ (self, color, is_filled):
        self. color = color
        self. is_filled = is_filled

    def desc(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class Circle(Shape):
    def __init__ (self, color, is_filled,radius):
        super().__init__(color, is_filled ) # Use super to add speical attribute
        self.radius = radius

    def desc(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}") #overrding method
        super().desc() # Use super to also use parents functions in addition

class Square(Shape):
    def __init__ (self, color, is_filled,width):
        super().__init__(color,is_filled) 
        self.width = width

    def desc(self):
        print(f"It is a circle with an area of {3.14 * self.width * self.width}") #overrding method
        super().desc() # Use super to also use parents functions in addition


class Triangle(Shape):
    def __init__ (self, color, is_filled,height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

    def desc(self):
        print(f"It is a circle with an area of {3.14 * self.width * self.height / 2}") #overrding method
        super().desc() # Use super to also use parents functions in addition


circle = Circle("red",True,radius=5)
square = Square("blue",False, width = 9)
triangle = Triangle("Black",True, height = 10, width = 5)

print(circle.color)
print(circle.is_filled)
print(f"THe circle is {circle.radius}")
circle.desc()
print ('\n')

print(square.color)
print(square.is_filled)
print(f"THe square is {square.width}")
square.desc()
print ('\n')

print(triangle.color)
print(triangle.is_filled)
print(f"THe triangle is {triangle.height}")
triangle.desc()




# polymorphism

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__ (self,radius):
        self.radius = radius

    def area(self):
        return 3.14* self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self. base = base
        self. height = height

    def area(self):
        return self.base* self.height * 0.5

class Pizza(Circle):
    def __init__(self, toppings , radius):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza('pepporoni', 15)]

for shape in shapes:
    print(shape.area())
    
    

# Aggregation = Represents a relationship where one object (the whole) contains references to one or 
# more INDEPENDENT obects (the parts)

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

library = Library("NYP library")

book1 = Book("Harry porter","Haru puttar")
book2 = Book("Magic emperor","Zhuo fan")
book3 = Book("TBATE","Arthur")   

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print (library.name)

for book in library.list_books():
    print(book)
    

# Composition = cannot exist without the parent class

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
        self.wheels = [ Wheel (wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horsepower}(hp) {self.wheels[0].size}in"

car1 = Car("Ford","Mustang", 500, 18)
car2 = Car("Chevrolet","Corvette",679,19)
print(car1.display_car())


# Nested class =  Class inside a class

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
            

    def __init__ (self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee (self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employee(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Hello world")
company2 = Company("Bye world")
company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob","Cook")
company1.add_employee("squidward","ship")

company2.add_employee("Rem", "Assitant")
company2.add_employee("John","Cook")
company2.add_employee("jane","ship")

for employee in company1.list_employee():
    print(employee)

for employee in company2.list_employee():
    print(employee)
    

# Static method in python are those methods that belong to class instead of object


class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position =position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier","Cook", "Janitor"]
        return position in valid_position


employee1  = Employee("Eugene","Manager")
employee2  = Employee("Squidward","Cashier")
employee3  = Employee("Spongebob","Cook")


print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())



        
# class Methods  = Allow operations related to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    # instance method cuase here it has self as a parameter
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
         return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f" Average gps: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy",4.0)

print(Student.get_count())
print(Student.get_average_gpa())


# Magic method  = Dunder methods (double underscore) __ini__, __str__, __eq__,
#                 They are authomatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other): #less than 
        return self.num_pages < other.num_pages

    def __gt__(self, otherr): # greater than
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword): # Search for a key word 
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title

        elif key == "author":
            return self.author

        elif key == "num_pages":
            return self.num_pages
        else: 
            return f"Key{key} was not found"
        
        

book1 = Book("The hobbit",'J.R.R', 310)
book2 = Book("SL","jinwoo",120)
book3 = Book("TBATE hello","jinwoo",344)

print(book3['num_pages'])


# @Property = Decorator is used to define a method as a property (it can be accessed like an)
# attribute) So instead of calling rectangle.width(), you can just do rectangle.width.
# Benefits = Add additional logic when read, write, or delete attributes
# Gives you getter, setter, deleter method

class Rectangle:
    def __init__ (self, width, height):
        self._width = width
        self._height = height
        
    @property # property decorater lets us to use method as attribute instead of calling rectangle.width(), you can just do rectangle.width.
    def width(self):
        return f"{self._width} inch"
        
    @property
    def height(self):
         return f"{self._height} inch"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")


    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(6,6)

rectangle.width = 6
rectangle.height = 7

del rectangle.width
del rectangle.height

