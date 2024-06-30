import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for the length and number of passwords
    try:
        length = int(input("Enter the desired password length: "))
        number = int(input("Enter the number of passwords to generate: "))
        
        if length <= 0 or number <= 0:
            print("Please enter positive integers for both length and number.")
            return
        
        print("\nGenerated Passwords:")
        for i in range(number):
            print(f"Password {i + 1}: {generate_password(length)}")
    
    except ValueError:
        print("Invalid input! Please enter integer values for length and number.")

if __name__ == "__main__":
    main()
