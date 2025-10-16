'''1. Write a program, called collatz.py, 
2. that asks the user to input any positive integer 
3. and outputs the successive values of the following calculation.
    3.1 At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
4.Have the program end if the current value is one.'''

# collatz.py

# Ask the user once for a positive integer
current_num = int(input("Please enter a positive number: "))

# Validate input
if current_num <= 0:
    print("Number must be positive!")
else:
    # Keep applying Collatz rules until number becomes 1
    while current_num != 1:
        print(current_num)  # Print the current number
        if current_num % 2 == 0:  # Even
            current_num = current_num // 2
        else:  # Odd
            current_num = current_num * 3 + 1
    print(current_num)  # Print 1 at the end

