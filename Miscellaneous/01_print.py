
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:  # Condition (a): Number must be divisible by five
        if num > 150:  # Condition (b): Skip if number is greater than 150
            continue
        elif num > 500:  # Condition (c): Stop loop if number is greater than 500
            break
        else:
            print(num) 
