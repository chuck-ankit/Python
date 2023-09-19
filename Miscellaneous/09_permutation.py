def get_permutations(string):
    # Base case: If the string is empty or has only one character, return the string itself as a single permutation
    if len(string) <= 1:
        return [string]

    # List to store permutations
    permutations = []

    # Iterate through each character in the string
    for i in range(len(string)):
        # Extract the current character
        current_char = string[i]

        # Generate all permutations of the remaining characters
        remaining_chars = string[:i] + string[i + 1:]
        sub_permutations = get_permutations(remaining_chars)

        # Append the current character to each permutation of the remaining characters
        for sub_permutation in sub_permutations:
            permutations.append(current_char + sub_permutation)

    # Return the list of permutations
    return permutations


# Test the get_permutations function
string = "abc"
permutations = get_permutations(string)
print(permutations)
