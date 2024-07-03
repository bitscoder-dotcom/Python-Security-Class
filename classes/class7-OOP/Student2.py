class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"Welcome  {self.name} from {self.house}."
    
    @classmethod
    def get(cls):
        name = input("Whats the name:  ") 
        house = input("Where are you from: ")
        return cls(name, house)
    

def main():
    student =  Student.get()
    print(student)


if __name__ == "__main__":
    main()