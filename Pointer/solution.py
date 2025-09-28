def pointer_concepts():
    """Demonstrate pointer-like concepts in Python"""
    
    # Python doesn't have explicit pointers, but we can demonstrate similar concepts
    
    # 1. References (similar to pointers)
    a = [1, 2, 3]
    b = a  # b references the same object as a
    print(f"Original a: {a}")
    print(f"b = a: {b}")
    
    # Modifying through one reference affects the other
    b[0] = 99
    print(f"After b[0] = 99, a: {a}")
    print(f"After b[0] = 99, b: {b}")
    
    # 2. Function parameters (pass by reference for mutable objects)
    def modify_list(lst):
        """Modify a list (mutable object)"""
        lst.append(4)
        lst[0] = 100
    
    numbers = [1, 2, 3]
    print(f"Before function call: {numbers}")
    modify_list(numbers)
    print(f"After function call: {numbers}")
    
    # 3. Immutable objects (pass by value)
    def modify_number(num):
        """Modify a number (immutable object)"""
        num += 10
        return num
    
    x = 5
    print(f"Before function call: x = {x}")
    result = modify_number(x)
    print(f"After function call: x = {x}, result = {result}")
    
    # 4. Using id() to see object identity (like memory addresses)
    print(f"ID of a: {id(a)}")
    print(f"ID of b: {id(b)}")
    print(f"a is b: {a is b}")  # Check if they reference the same object


def swap_values(a, b):
    """Demonstrate swapping values (Python style)"""
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a  # Python's elegant swapping
    print(f"After swap: a = {a}, b = {b}")
    return a, b


def main():
    """Main function to demonstrate pointer-like concepts"""
    print("=== Pointer-like Concepts in Python ===")
    pointer_concepts()
    
    print("\n=== Swapping Values ===")
    x, y = 10, 20
    x, y = swap_values(x, y)
    
    print(f"Final values: x = {x}, y = {y}")


if __name__ == "__main__":
    main()
