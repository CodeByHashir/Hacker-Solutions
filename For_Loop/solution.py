def print_squares(n):
    """Print squares of numbers from 0 to n-1"""
    for i in range(n):
        print(i * i)


def print_even_squares(n):
    """Print squares of even numbers from 0 to n-1"""
    for i in range(0, n, 2):  # Step by 2 for even numbers
        print(i * i)


def print_pattern(n):
    """Print a pattern using nested loops"""
    for i in range(1, n + 1):
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # New line after each row


def main():
    """Main function to demonstrate for loops"""
    n = int(input())
    
    print("Squares from 0 to n-1:")
    print_squares(n)
    
    print("\nSquares of even numbers:")
    print_even_squares(n)
    
    print("\nPattern:")
    print_pattern(n)


if __name__ == "__main__":
    main()
