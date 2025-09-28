class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        """Initialize animal with name and age"""
        self.name = name
        self.age = age
    
    def speak(self):
        """Base speak method - to be overridden"""
        return "Some generic animal sound"
    
    def display_info(self):
        """Display animal information"""
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        """Initialize dog with name, age, and breed"""
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        """Override speak method for dog"""
        return "Woof!"
    
    def display_info(self):
        """Override display method to include breed"""
        super().display_info()  # Call parent method
        print(f"Breed: {self.breed}")


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, age, color):
        """Initialize cat with name, age, and color"""
        super().__init__(name, age)  # Call parent constructor
        self.color = color
    
    def speak(self):
        """Override speak method for cat"""
        return "Meow!"
    
    def display_info(self):
        """Override display method to include color"""
        super().display_info()  # Call parent method
        print(f"Color: {self.color}")


def main():
    """Main function to demonstrate inheritance"""
    # Create animal objects
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "Orange")
    
    # Display information
    print("Dog Information:")
    dog.display_info()
    print(f"Sound: {dog.speak()}")
    
    print("\nCat Information:")
    cat.display_info()
    print(f"Sound: {cat.speak()}")


if __name__ == "__main__":
    main()
