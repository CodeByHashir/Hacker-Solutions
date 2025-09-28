# Multi-Level Inheritance - HackerRank Solution

## Problem Overview
This problem demonstrates multi-level inheritance where a class inherits from another class that itself inherits from a base class, creating a hierarchy of inheritance.

## Step-by-Step Explanation

### Input → Processing → Output

**Input:**
- Data for creating vehicles at different inheritance levels

**Processing:**
1. **Base Class**: Create Vehicle class with basic properties
2. **First Level**: Create Car class inheriting from Vehicle
3. **Second Level**: Create SportsCar class inheriting from Car
4. **Method Overriding**: Override methods at each level
5. **Constructor Chaining**: Call parent constructors at each level
6. **Specialized Methods**: Add methods specific to each level

**Output:**
- Display information and behavior for each inheritance level

## Key Python Concepts Used
- **Multi-Level Inheritance**: Classes inheriting from other derived classes
- **Inheritance Hierarchy**: Vehicle → Car → SportsCar
- **Method Overriding**: Redefining methods at each level
- **Constructor Chaining**: Multiple super() calls
- **Specialized Behavior**: Level-specific methods and attributes

## Learning Points
- Multi-level inheritance creates class hierarchies
- Each level can add new attributes and methods
- Methods can be overridden at any level
- super() calls the immediate parent class
- Inheritance hierarchy should represent "is-a" relationships
- Higher levels inherit from all lower levels
