# Virtual Function - HackerRank Solution

## Problem Overview
This problem demonstrates object-oriented programming concepts including inheritance, polymorphism, and virtual functions (method overriding in Python).

## Step-by-Step Explanation

### Input → Processing → Output

**Input:**
- First line: Number of objects to create (n)
- For each object:
  - Object type (1 for Professor, 2 for Student)
  - Name and age
  - For Professor: Number of publications
  - For Student: 6 subject marks

**Processing:**
1. **Class Hierarchy**: Create a base `Person` class with virtual methods
2. **Inheritance**: `Professor` and `Student` classes inherit from `Person`
3. **Method Overriding**: Each subclass implements its own `getdata()` and `putdata()` methods
4. **Static Variables**: Use class variables to track unique IDs for each type
5. **Polymorphism**: Store different object types in the same list and call methods uniformly

**Output:**
- For Professor: Name, age, publications, professor ID
- For Student: Name, age, total marks, student ID

## Key Python Concepts Used
- **Inheritance**: Classes inheriting from base class
- **Method Overriding**: Subclasses implementing parent methods
- **Class Variables**: Static-like variables shared across instances
- **Polymorphism**: Same interface for different object types
- **Object-Oriented Design**: Clean separation of concerns

## Learning Points
- Virtual functions in C++ become method overriding in Python
- Class variables act like static variables in other languages
- Python's dynamic typing makes polymorphism more flexible
- Always call `super().__init__()` when inheriting from a class
