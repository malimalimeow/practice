class Pet:
    def __init__(self,name,type,age):
        self.name=name
        self.age=age
        self.type=type
    
    def speak(self):
        if self.type=="dog":
            print(f"woof!I am {self.name},{self.age} years old.") 
        
        if self.type=="cat":
            print(f"Meow!I am {self.name},{self.age} years old.") 
            
class PetShelter:
    def __init__(self):
        self.pets=[]
        
    def add_pet(self,pet):
        self.pets.append(pet) 
    
    def all_speak(self) :
        if not self.pets:
            print("pet is not registered!")    
            return 
        for pet in self.pets:
            pet.speak()


dog = Pet("Buddy", "dog", 3)
cat = Pet("Mimi", "cat", 2)

# 建立收容所
shelter = PetShelter()

# 加入寵物
shelter.add_pet(dog)
shelter.add_pet(cat)

# 所有寵物講嘢
shelter.all_speak()
