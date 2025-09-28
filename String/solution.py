def string_operations():
    """Demonstrate various string operations"""
    
    # Read input string
    s = input("Enter a string: ")
    
    # Basic string operations
    print(f"Original string: {s}")
    print(f"Length: {len(s)}")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Capitalized: {s.capitalize()}")
    print(f"Title case: {s.title()}")
    
    # String slicing
    print(f"First 3 characters: {s[:3]}")
    print(f"Last 3 characters: {s[-3:]}")
    print(f"Middle characters: {s[1:-1]}")
    
    # String methods
    print(f"Starts with 'Hello': {s.startswith('Hello')}")
    print(f"Ends with 'World': {s.endswith('World')}")
    print(f"Contains 'Python': {'Python' in s}")
    
    # String formatting
    name = "Alice"
    age = 25
    print(f"Formatted string: {name} is {age} years old")
    
    # String joining and splitting
    words = s.split()
    print(f"Words: {words}")
    print(f"Joined with '-': {'-'.join(words)}")


def palindrome_check(s):
    """Check if a string is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    # Check if string equals its reverse
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def main():
    """Main function to demonstrate string operations"""
    string_operations()
    
    # Test palindrome function
    test_string = input("\nEnter a string to check for palindrome: ")
    if palindrome_check(test_string):
        print(f"'{test_string}' is a palindrome")
    else:
        print(f"'{test_string}' is not a palindrome")
    
    # Test vowel counting
    vowel_count = count_vowels(test_string)
    print(f"Number of vowels: {vowel_count}")


if __name__ == "__main__":
    main()
