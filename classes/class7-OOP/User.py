class User:
    """
        This is the parent User class
    """
    def __init__(self, name, department):
        if not name or not department:
            raise ValueError("Missing attribute")
        self.name = name
        self.department = department
        """
            This method initilizes the the attributes of the User class.
            It also performs a check if the 'name' or 'department' attribute is missing.
        """
        
    ...

class Student(User):
    """
        This Student class inherits from the User class
    """
    def __init__(self, name, age, department, courses=[]):
        super().__init__(name, department)
        self.age = age
        self.courses = courses
        """
            The 'init' method has its own specific parameters, it also inherits parameters from the parent User class.
        """

    ... 

class Teacher(User):
    def __init__(self, name, depatment, course, address):
        super().__init__(name, depatment)
        self.address = address
        self.course = course
    
    ...

student  = Student("Albert", 22, "Physics", ["PHY101", "ELE112", "MOT167"])
teacher = Teacher("Professor Tanus", "English", "ENG 229", "12 Cambridge Lane, NY")