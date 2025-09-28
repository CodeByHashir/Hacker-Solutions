class Person:
    """Base class for Person with virtual methods"""
    def __init__(self):
        self.name = ""
        self.age = 0
    
    def getdata(self):
        """Virtual method to get data - to be overridden"""
        pass
    
    def putdata(self):
        """Virtual method to put data - to be overridden"""
        pass


class Professor(Person):
    """Professor class inheriting from Person"""
    cur_id = 1  # Class variable to track professor IDs
    
    def __init__(self):
        super().__init__()
        self.publications = 0
    
    def getdata(self):
        """Get professor data from input"""
        self.name = input()
        self.age = int(input())
        self.publications = int(input())
    
    def putdata(self):
        """Display professor data with current ID"""
        print(f"{self.name} {self.age} {self.publications} {Professor.cur_id}")
        Professor.cur_id += 1


class Student(Person):
    """Student class inheriting from Person"""
    cur_id = 1  # Class variable to track student IDs
    
    def __init__(self):
        super().__init__()
        self.marks = [0] * 6  # Initialize 6 subjects with 0 marks
        self.total_marks = 0
    
    def getdata(self):
        """Get student data from input"""
        self.name = input()
        self.age = int(input())
        self.total_marks = 0
        
        # Read 6 subject marks and calculate total
        for i in range(6):
            self.marks[i] = int(input())
            self.total_marks += self.marks[i]
    
    def putdata(self):
        """Display student data with current ID"""
        print(f"{self.name} {self.age} {self.total_marks} {Student.cur_id}")
        Student.cur_id += 1


def main():
    """Main function to handle the program logic"""
    n = int(input())  # Number of objects to create
    objects = []
    
    # Create objects based on input
    for i in range(n):
        obj_type = int(input())
        
        if obj_type == 1:
            # Create Professor object
            obj = Professor()
        else:
            # Create Student object
            obj = Student()
        
        obj.getdata()  # Get data for the object
        objects.append(obj)
    
    # Display all objects
    for obj in objects:
        obj.putdata()


if __name__ == "__main__":
    main()
