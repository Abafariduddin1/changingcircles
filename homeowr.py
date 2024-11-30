class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'Hi, My name is {self.name} and I"m {self.age} years old.')

student1 = Student("Sam", 9)
student1.introduce()
