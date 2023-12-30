from Armstrong import is_armstrong

def generate_armstrong_numbers(lower_limit, upper_limit):
    armstrong_numbers = []
    for num in range(lower_limit, upper_limit + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

lower_limit =int(input("ENTER THE LOWER LIMIT:"))
upper_limit =int(input("ENTER THE UPPER LIMIT:"))
result = generate_armstrong_numbers(lower_limit, upper_limit)
print(f"Armstrong numbers between {lower_limit} and {upper_limit}:")
print(result)

