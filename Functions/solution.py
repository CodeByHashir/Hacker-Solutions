def is_leap(year):
    """Check if a year is a leap year"""
    # Leap year conditions:
    # 1. Divisible by 400, OR
    # 2. Divisible by 4 but not by 100
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    
    return fib_sequence


def main():
    """Main function to demonstrate various functions"""
    # Test leap year function
    year = int(input("Enter a year: "))
    if is_leap(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
    # Test factorial function
    num = int(input("Enter a number for factorial: "))
    print(f"Factorial of {num} is {factorial(num)}")
    
    # Test Fibonacci function
    terms = int(input("Enter number of Fibonacci terms: "))
    fib_seq = fibonacci(terms)
    print(f"Fibonacci sequence: {fib_seq}")


if __name__ == "__main__":
    main()
