
class Person:
    """A class to represent a person"""
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def change_name(self):
        self.name = input("Enter new name: ")
    
    def another_name(self, new_name):
        self.name = new_name
    
    def allowed_to_drive(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    # Getters
    def get_name(self):
        return self.name

class Car:
    def __init__(self, model, drive_type, seat_count):
        self.model = model
        self.drive_type = drive_type
        self.seat_count = seat_count

if __name__ =="__main__":
    obj1 = Person("Kwame", 18, 54, 76)
    obj2 = Car("G-Wagon", "All wheel drive", 6)
    #print(obj1.name)
    #print(obj2.model)
    print(f'{obj1.name} is a boy and loves to drive a {obj2.model}')
    print(obj1.allowed_to_drive())
    print(obj1.get_name())
    
