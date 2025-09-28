class Box:
    """Box class to demonstrate operator overloading"""
    
    def __init__(self, length=0, breadth=0, height=0):
        """Initialize box dimensions"""
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def __add__(self, other):
        """Overload + operator to add two boxes"""
        new_length = self.length + other.length
        new_breadth = self.breadth + other.breadth
        new_height = self.height + other.height
        return Box(new_length, new_breadth, new_height)
    
    def __str__(self):
        """String representation of the box"""
        return f"Box({self.length}, {self.breadth}, {self.height})"
    
    def get_volume(self):
        """Calculate and return the volume of the box"""
        return self.length * self.breadth * self.height


def main():
    """Main function to demonstrate Box operations"""
    # Read input for first box
    l1, b1, h1 = map(int, input().split())
    box1 = Box(l1, b1, h1)
    
    # Read input for second box
    l2, b2, h2 = map(int, input().split())
    box2 = Box(l2, b2, h2)
    
    # Add the boxes using overloaded + operator
    box3 = box1 + box2
    
    # Display results
    print(f"Box 1: {box1}")
    print(f"Box 2: {box2}")
    print(f"Box 3 (Box1 + Box2): {box3}")
    print(f"Volume of Box 3: {box3.get_volume()}")


if __name__ == "__main__":
    main()
