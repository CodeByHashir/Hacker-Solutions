def check_number(n):
    """Check if number is weird or not weird based on conditions"""
    
    # Check if number is odd
    if n % 2 == 1:
        return "Weird"
    
    # Check if number is even and in range 2-5
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    
    # Check if number is even and in range 6-20
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    
    # Check if number is even and greater than 20
    elif n % 2 == 0 and n > 20:
        return "Not Weird"
    
    # Default case (should not reach here)
    else:
        return "Invalid input"


def main():
    """Main function to demonstrate conditional statements"""
    # Read input
    n = int(input())
    
    # Check and display result
    result = check_number(n)
    print(result)


if __name__ == "__main__":
    main()
