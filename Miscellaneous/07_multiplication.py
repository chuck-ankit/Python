# Function to print the multiplication table
def multiplication_table(number):
    for i in range(1, 11):
        product = number * i
        print(number, "x", i, "=", product)

# Get the number from the user
number = int(input("Enter a number: "))

# Print the multiplication table
multiplication_table(number)
