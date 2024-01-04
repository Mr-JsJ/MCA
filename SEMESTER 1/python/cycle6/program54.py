def validate_name(name):
    return name.isalpha() or ' ' in name

def validate_age(age):
    try:
        age = int(age)
        if age >= 18:
            return True
        else:
            return False
    except ValueError:
        return False

name = input("Enter your name: ")
age = input("Enter your age: ")

if validate_name(name) and validate_age(age):
    print(f"Hello, {name}!")
    print("You are eligible to cast your vote.")
else:
    print("Sorry, you are not eligible to cast your vote.")
