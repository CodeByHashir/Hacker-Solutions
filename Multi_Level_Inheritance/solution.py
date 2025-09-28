class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, brand, model, year):
        """Initialize vehicle with brand, model, and year"""
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        """Start the vehicle engine"""
        return f"{self.brand} {self.model} engine started"
    
    def display_info(self):
        """Display vehicle information"""
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, doors):
        """Initialize car with additional doors attribute"""
        super().__init__(brand, model, year)
        self.doors = doors
    
    def start_engine(self):
        """Override start_engine for car"""
        return f"Car {self.brand} {self.model} engine started with {self.doors} doors"
    
    def display_info(self):
        """Override display_info to include doors"""
        super().display_info()
        print(f"Doors: {self.doors}")


class SportsCar(Car):
    """SportsCar class inheriting from Car (multi-level inheritance)"""
    
    def __init__(self, brand, model, year, doors, top_speed):
        """Initialize sports car with additional top_speed attribute"""
        super().__init__(brand, model, year, doors)
        self.top_speed = top_speed
    
    def start_engine(self):
        """Override start_engine for sports car"""
        return f"Sports car {self.brand} {self.model} engine started with {self.doors} doors, top speed: {self.top_speed} mph"
    
    def display_info(self):
        """Override display_info to include top speed"""
        super().display_info()
        print(f"Top Speed: {self.top_speed} mph")
    
    def race_mode(self):
        """Sports car specific method"""
        return f"Race mode activated for {self.brand} {self.model}"


def main():
    """Main function to demonstrate multi-level inheritance"""
    # Create objects at different inheritance levels
    vehicle = Vehicle("Toyota", "Camry", 2020)
    car = Car("Honda", "Civic", 2021, 4)
    sports_car = SportsCar("Ferrari", "488", 2022, 2, 205)
    
    # Display information for each object
    print("Vehicle:")
    vehicle.display_info()
    print(f"Engine: {vehicle.start_engine()}")
    
    print("\nCar:")
    car.display_info()
    print(f"Engine: {car.start_engine()}")
    
    print("\nSports Car:")
    sports_car.display_info()
    print(f"Engine: {sports_car.start_engine()}")
    print(f"Special: {sports_car.race_mode()}")


if __name__ == "__main__":
    main()
