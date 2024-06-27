class Student():
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing parameter 'name'")
        self.name = name
        self.house = house

    def __str__(self):
        return f"Hello {self.name} from {self.house}."
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Lekki", "Ikoyi", "Ikeja", "Banana Island"]:
            raise ValueError("You cannot come to the party")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Whats the name: ") 
    house = input("Where are you from: ")
    return Student(name, house)

if __name__ == "__main__":
    main()