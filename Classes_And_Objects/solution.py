class Student:
    """Student class to demonstrate basic OOP concepts"""
    
    def __init__(self, name, roll_number):
        """Initialize student with name and roll number"""
        self.name = name
        self.roll_number = roll_number
        self.marks = []
    
    def add_marks(self, subject_marks):
        """Add marks for a subject"""
        self.marks.append(subject_marks)
    
    def get_average(self):
        """Calculate and return average marks"""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self):
        """Determine grade based on average marks"""
        average = self.get_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_info(self):
        """Display student information"""
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Grade: {self.get_grade()}")


def main():
    """Main function to demonstrate Student class"""
    # Create student objects
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")
    
    # Add marks for student1
    student1.add_marks(85)
    student1.add_marks(92)
    student1.add_marks(78)
    
    # Add marks for student2
    student2.add_marks(95)
    student2.add_marks(88)
    student2.add_marks(91)
    
    # Display student information
    print("Student 1:")
    student1.display_info()
    print("\nStudent 2:")
    student2.display_info()


if __name__ == "__main__":
    main()
