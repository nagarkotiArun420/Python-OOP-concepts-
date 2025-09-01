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

