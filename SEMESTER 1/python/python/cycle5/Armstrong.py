def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    
    if sum_of_digits == number:
        return True
    else:
        return False
