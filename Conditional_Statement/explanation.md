# Conditional Statement - HackerRank Solution

## Problem Overview
This problem demonstrates conditional statements and logical operators in Python to determine if a number is "Weird" or "Not Weird" based on specific conditions.

## Step-by-Step Explanation

### Input → Processing → Output

**Input:**
- A single integer n

**Processing:**
1. **Check if odd**: If n is odd, return "Weird"
2. **Check even ranges**: If n is even, check different ranges:
   - 2-5: "Not Weird"
   - 6-20: "Weird" 
   - >20: "Not Weird"

**Output:**
- "Weird" or "Not Weird" based on the conditions

## Key Python Concepts Used
- **Conditional Statements**: if, elif, else
- **Logical Operators**: and, or, not
- **Comparison Operators**: ==, !=, <, >, <=, >=
- **Modulo Operator**: % for checking even/odd
- **Function Definition**: Creating reusable code blocks

## Learning Points
- Use if-elif-else for multiple conditions
- Modulo operator (%) returns remainder
- Logical operators combine conditions
- Always handle edge cases and default scenarios
- Functions make code reusable and testable
