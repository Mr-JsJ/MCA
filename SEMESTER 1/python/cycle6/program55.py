try:
    number = float(input("Enter a number: "))
    if number >= 0:
        print(f"The entered number is: {number}")
    else:
        raise ValueError("Number is negative")
except ValueError as e:
    print(f"Error: {e}. Please enter a positive number or zero.")
