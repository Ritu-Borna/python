class animal:
    def bark(self):
        print("Animal make different sounds.")

class dog(animal):
    def bark(self):
        print("Dog barks.")

a=animal()
d=dog()
a.bark()
d.bark()      