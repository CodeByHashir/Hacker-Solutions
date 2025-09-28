class Student:
    """Student class to demonstrate struct-like behavior in Python"""
    
    def __init__(self, name, age, grade):
        """Initialize student with name, age, and grade"""
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        """String representation of student"""
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"
    
    def __repr__(self):
        """Detailed representation of student"""
        return f"Student('{self.name}', {self.age}, '{self.grade}')"


class Point:
    """Point class to represent 2D coordinates"""
    
    def __init__(self, x, y):
        """Initialize point with x and y coordinates"""
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """Calculate distance from origin (0,0)"""
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to(self, other):
        """Calculate distance to another point"""
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self):
        """String representation of point"""
        return f"Point({self.x}, {self.y})"


def main():
    """Main function to demonstrate struct-like classes"""
    # Create student objects
    student1 = Student("Alice", 20, "A")
    student2 = Student("Bob", 19, "B")
    
    print("Students:")
    print(student1)
    print(student2)
    
    # Create point objects
    point1 = Point(3, 4)
    point2 = Point(0, 0)
    point3 = Point(6, 8)
    
    print("\nPoints:")
    print(f"Point1: {point1}")
    print(f"Point2: {point2}")
    print(f"Point3: {point3}")
    
    # Calculate distances
    print(f"\nDistance from origin to Point1: {point1.distance_from_origin():.2f}")
    print(f"Distance from Point1 to Point3: {point1.distance_to(point3):.2f}")


if __name__ == "__main__":
    main()
