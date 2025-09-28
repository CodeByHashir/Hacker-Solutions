# Inheritance Introduction - HackerRank Solution

## Problem Overview
This problem demonstrates inheritance in object-oriented programming, showing how child classes can inherit properties and methods from parent classes.

## Step-by-Step Explanation

### Input → Processing → Output

**Input:**
- Data for creating different types of animals

**Processing:**
1. **Base Class**: Create Animal class with common properties
2. **Child Classes**: Create Dog and Cat classes inheriting from Animal
3. **Method Overriding**: Override methods in child classes
4. **Super() Function**: Call parent class methods from child classes
5. **Polymorphism**: Use same interface for different animal types

**Output:**
- Display information and sounds for different animals

## Key Python Concepts Used
- **Inheritance**: Child classes inheriting from parent classes
- **Method Overriding**: Redefining methods in child classes
- **Super() Function**: Accessing parent class methods
- **Polymorphism**: Same interface for different object types
- **Constructor Chaining**: Calling parent constructors

## Learning Points
- Inheritance allows code reuse and organization
- Child classes inherit all parent attributes and methods
- Method overriding provides specialized behavior
- super() function calls parent class methods
- Inheritance creates "is-a" relationships
- Always call super().__init__() in child constructors
