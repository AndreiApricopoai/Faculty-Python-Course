import math


# Laboratory 5

# Ex1 - Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with area {self.area()} and perimeter {self.perimeter()}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(circle)
print(rectangle)
print(triangle)
print("\n")


# Ex2 - Design a bank account system with a base class Account and subclasses SavingsAccount
# and CheckingAccount. Implement methods for deposit, withdrawal, and interest calculation.
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self):
        return super().__str__() + f", Interest Rate: {self.interest_rate}"


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded")

    def __str__(self):
        return super().__str__() + f", Overdraft Limit: {self.overdraft_limit}"


savings = SavingsAccount('12345', 1000, 0.03)
checking = CheckingAccount('67890', 500, 200)

savings.deposit(500)
savings.add_interest()
print(savings)

checking.deposit(300)
checking.withdraw(1000)
print(checking)
print("\n")


# Ex3 - Create a base class Vehicle with attributes like make, model, and year,
# and then create subclasses for specific types of vehicles like Car, Motorcycle,
# and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_consumption):
        super().__init__(make, model, year)
        self.fuel_consumption = fuel_consumption

    def calculate_mileage(self, distance_traveled):
        return distance_traveled / self.fuel_consumption

    def __str__(self):
        return super().__str__() + f"Fuel Consumption: {self.fuel_consumption}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_consumption, hp):
        super().__init__(make, model, year)
        self.fuel_consumption = fuel_consumption
        self.hp = hp

    def calculate_mileage(self, distance_traveled):
        if self.hp > 100:
            return distance_traveled / (self.fuel_consumption * 1.5)
        else:
            return distance_traveled / self.fuel_consumption

    def __str__(self):
        return super().__str__() + f"Fuel Consumption: {self.fuel_consumption}, HP: {self.hp}"


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, hp):
        super().__init__(make, model, year)
        self.weight = weight
        self.hp = hp

    def calculate_towing_capacity(self):
        return self.weight * self.hp * 2

    def __str__(self):
        return super().__str__() + f"Towing Capacity: {self.calculate_towing_capacity}"


car = Car("Toyota", "Corolla", 2020, 30)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 40, 75)
truck = Truck("Ford", "F-150", 2021, 5000, 300)
print(car)
print("Car Mileage for 300 miles:", car.calculate_mileage(300), "miles per gallon")
print(motorcycle)
print("Motorcycle Mileage for 150 miles:", motorcycle.calculate_mileage(150), "miles per gallon")
print(truck)
print("Truck Towing Capacity:", truck.calculate_towing_capacity(), "lbs")
print("\n")


# Ex4 - Build an employee hierarchy with a base class Employee.
# Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
# Each subclass should have attributes like salary and methods related to their roles.
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}, Employees: {[e.name for e in self.employees]}"


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, specialty):
        super().__init__(name, employee_id, salary)
        self.specialty = specialty

    def work_on_project(self, project_name):
        return f"Engineer {self.name} is working on {project_name}."

    def __str__(self):
        return f"Engineer: {self.name}, Specialty: {self.specialty}"


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target
        self.achieved_sales = 0

    def make_sale(self, amount):
        self.achieved_sales += amount

    def calculate_commission(self):
        return self.achieved_sales * 0.05

    def display_sales_info(self):
        return f"Salesperson: {self.name}, Achieved Sales: {self.achieved_sales}, Commission: {self.calculate_commission()}"


manager = Manager("Alice", "M001", 95000, "Technology")
engineer1 = Engineer("Bob", "E002", 85000, "Software")
engineer2 = Engineer("Carol", "E003", 82000, "Hardware")
salesperson = Salesperson("Dave", "S004", 60000, 150000)

manager.add_employee(engineer1)
manager.add_employee(engineer2)
print(manager)

print(engineer1.work_on_project("AI Development"))

salesperson.make_sale(50000)
salesperson.make_sale(30000)
print(salesperson.display_sales_info())

manager.remove_employee(engineer1)
print(manager, "\n")


# Ex5 - Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish. Add properties and methods to
# represent characteristics unique to each animal group.
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f" {self.name}, Age: {self.age}, Weight: {self.weight}"


class Mammal(Animal):
    def __init__(self, name, age, weight, fur_color):
        super().__init__(name, age, weight)
        self.fur_color = fur_color
        self.warm_blooded = True

    def nurse_young(self):
        return f"{self.name} is nursing its young."

    def __str__(self):
        return f"Mammal: {super().__str__()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, age, weight, wing_span, beak_type):
        super().__init__(name, age, weight)
        self.wing_span = wing_span
        self.beak_type = beak_type

    def fly(self):
        return f"{self.name} is flying."

    def sing(self):
        return f"{self.name} is singing."

    def __str__(self):
        return f"Bird: {super().__str__()}, Wing Span: {self.wing_span}, Beak Type: {self.beak_type}"


class Fish(Animal):
    def __init__(self, name, age, weight, scale_type, water_type):
        super().__init__(name, age, weight)
        self.scale_type = scale_type
        self.water_type = water_type

    def swim(self):
        return f"{self.name} is swimming."

    def dive(self):
        return f"{self.name} is diving."

    def __str__(self):
        return f"Fish: {super().__str__()}, Scale Type: {self.scale_type}, Water Type: {self.water_type}"


lion = Mammal("Leo", 5, 190, "Golden")
parrot = Bird("Polly", 3, 0.5, "1 foot", "Curved")
shark = Fish("Sammy", 8, 300, "Rough", "Saltwater")

print(lion)
print(lion.eat())
print(lion.nurse_young())

print(parrot)
print(parrot.fly())
print(parrot.sing())

print(shark)
print(shark.swim())
print(shark.dive())
print("\n")


# Ex6 - Design a library catalog system with a base class LibraryItem and subclasses
# for different types of items like Book, DVD, and Magazine. Include methods to check
# out, return, and display information about each item.
class LibraryItem:
    def __init__(self, title, creator, item_id):
        self.title = title
        self.creator = creator
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def __str__(self):
        if self.checked_out:
            status = "Checked Out"
        else:
            status = "Available"
        return f"Title: {self.title}, Creator: {self.creator}, Status: {status}"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, isbn, pages):
        super().__init__(title, author, item_id)
        self.isbn = isbn
        self.pages = pages

    def get_number_of_pages(self):
        return self.pages

    def is_isbn_valid(self):
        if len(self.isbn) == 13:
            return True
        else:
            return False

    def __str__(self):
        return f"{super().__str__()}, ISBN: {self.isbn}, Pages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration, genre):
        super().__init__(title, director, item_id)
        self.duration = duration
        self.genre = genre

    def get_duration(self):
        return self.duration

    def is_genre_valid(self):
        if self.genre in ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]:
            return True
        else:
            return False

    def __str__(self):
        return f"{super().__str__()}, Duration: {self.duration}, Genre: {self.genre}"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number, publication_date):
        super().__init__(title, publisher, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def get_issue_number(self):
        return self.issue_number

    def get_publication_date(self):
        return self.publication_date

    def is_published_this_year(self):
        if self.publication_date == 2021:
            return True
        else:
            return False

    def __str__(self):
        return f"{super().__str__()}, Issue: {self.issue_number}, Publication Date: {self.publication_date}"


book = Book("To Kill a Mockingbird", "Harper Lee", "B001", "978-0061120084", 281)
dvd = DVD("The Shawshank Redemption", "Frank Darabont", "D002", "142 minutes", "Drama")
magazine = Magazine("Time", "Time Inc.", "M003", "2021-04", 2021)

print(book.check_out())
print(dvd.check_out())

print(book)
print(dvd)
print(magazine)

print("Book Pages:", book.get_number_of_pages())
print("DVD Duration:", dvd.get_duration())
print("Magazine Publication Date:", magazine.get_publication_date())

print(book.return_item())
print(dvd.return_item())

print(book)
print(dvd)
