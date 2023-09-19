
import builtins

# Displaying documentation of abs() function
print("Documentation of abs() function:")
print(builtins.abs.__doc__)

# Finding the absolute value of -155
number = -155
absolute_value = abs(number)
print("Absolute value of", number, "is", absolute_value)

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Print the third, fourth, and fifth items
print(fruits[-7:-4])
