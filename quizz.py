def filter_even_numbers(numbers):
     # Initialize an empty list to store even numbers
    even_numbers = []

    # Loop through each number in the input list
    for numbers in numbers:
        # Check if the number is even
        if even_numbers % 2 == 0:
            # If it is, append it to the even_numbers list
            even_numbers.append(numbers)
    
    # Return the list of even numbers
    return even_numbers