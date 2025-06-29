type 1(default constractor):
class Car:
    def __init__(self):#dunder method,constructor
        self.brand=""
        self.model=""

car1=Car()
car1.brand="Toyota"
car1.model="Corolla"
print(car1.brand)
print(car1.model)   
car2=Car()
car2.brand="Honda"
car2.model="Civic"
print(car2.brand, car2.model)   


# type 2(parameterized constractor):
class Car:
    def __init__(self,brand,model):#dunder method,constructor
        self.brand=brand
        self.model=model

car1=Car("Toyota","Corolla") 
print(car1.brand)
print(car1.model)
car2=Car("Honda","Civic")
print(car2.brand, car2.model)  

# type 3(default value constractor):
class Car:
    def __init__(self,brand="honda",model="civic"):#dunder method,constructor
        self.brand=brand
        self.model=model

car1=Car() 
print(car1.brand)
print(car1.model)
car2=Car()
print(car2.brand, car2)     

class Car:
    def __init__(self,brand="honda",model="civic"):#dunder method,constructor
        self.brand=brand
        self.model=model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1=Car() 
car2=Car("toyota","corolla")
car1.display()
car2.display()

class Car:
    def __init__(self, brand="Toyota", model="Corolla"):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Honda", "Civic")
car2 = Car()
car1.display()
car2.display()

class School:
    school_name = "ABC High School"  # Class variabl
    
    def __init__(self,name):
        self.student_name =name  # Instance variable
        
sc1= School("rahim")
sc2= School("karim")
sc1.school_name = "ostad school"
print(sc1.school_name) 
print(sc1.student_name) # Accessing class variable
print(sc2.school_name,sc2.student_name)  # Accessing instance variable

class Employee:
    company_name="ostad company"
    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

emp1=Employee("rahim", "developer")
emp2=Employee("karim","manager")
emp2.company_name="abs company" # Changing class variable for emp2
print(emp1.company_name)  # Accessing class variable
print(emp1.name, emp1.position)  # Accessing instance variable  
print(emp2.company_name)
print(emp2.name,emp2.position) # Accessing instance variable 

class person:   #parent class
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(person):   #child class
    pass
std1=Student("Rahim", 20)
std2=Student("Karim", 22)
std1.display()
std2.display()
