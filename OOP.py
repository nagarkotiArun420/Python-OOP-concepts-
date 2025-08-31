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