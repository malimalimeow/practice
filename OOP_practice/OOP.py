class Cat:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        
    def speak(self):
        print(f"Meow~I am {self.name},I am {self.age} years old.")
        
Poo=Cat("poo",3)
Poo.speak()