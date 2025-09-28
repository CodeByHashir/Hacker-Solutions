class Rectangle:
    """Rectangle class to calculate area and perimeter"""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width"""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of rectangle"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate and return the perimeter of rectangle"""
        return 2 * (self.length + self.width)
    
    def display(self):
        """Display rectangle information"""
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


def main():
    """Main function to demonstrate Rectangle class"""
    # Read input
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    
    # Create rectangle object
    rectangle = Rectangle(length, width)
    
    # Display rectangle information
    rectangle.display()


if __name__ == "__main__":
    main()
