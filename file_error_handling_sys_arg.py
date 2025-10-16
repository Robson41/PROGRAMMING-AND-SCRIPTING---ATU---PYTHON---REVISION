'''New Question:
Task:
Write a program that reads a text file and outputs the number of times the letter “a” appears in the file.
Requirements:
The program should take the filename from a command-line argument.
Document any assumptions you make (e.g., file encoding, case-sensitivity).
Handle errors gracefully, including:
No filename provided
File does not exist
File is not a .txt file
Bonus (optional):
Make the program case-insensitive, so it counts both “a” and “A”.'''
# ---------------------------------------------------------------
# Import the 'sys' module so we can read command-line arguments.
# This lets the program receive input when it's launched from the terminal.
# Example usage: python3 file_error_handling_2.py Text.txt
# In this case:
#   sys.argv[0] -> 'file_error_handling_2.py'  (the script name)
#   sys.argv[1] -> 'Text.txt'                  (the filename you typed)
# ---------------------------------------------------------------
import sys

# ---------------------------------------------------------------
# STEP 1: Check if the user provided a filename
# ---------------------------------------------------------------
# When you run the script, the arguments you type are stored in a list called sys.argv.
# The first item (sys.argv[0]) is always the script name.
# If there’s no second item (sys.argv[1]), it means the user didn’t give a filename.
# len(sys.argv) tells us how many total items are in that list.
if len(sys.argv) < 2:
    print("Error: No filename provided.")
    print("Usage: python3 file_error_handling_2.py <filename>")
    quit()  # Stop the program early since we cannot proceed without a file

# ---------------------------------------------------------------
# STEP 2: Store the filename entered by the user
# ---------------------------------------------------------------
filename = sys.argv[1]  # This captures whatever the user typed after the script name

# ---------------------------------------------------------------
# STEP 3: Check if the file is a text file
# ---------------------------------------------------------------
# The assignment requires that we only accept files ending in '.txt'
# We use the .endswith() method to check the last characters in the filename.
# If it’s not a .txt file, we print an error and exit.
# Check if the filename provided by the user does NOT end with '.txt'
# 'filename.lower()' ensures we ignore case differences, e.g., 'Text.TXT' becomes 'text.txt'
# '.endswith('.txt')' returns True if the string ends with '.txt', False otherwise
# The 'not' keyword reverses the boolean value of the condition
# So if the file does NOT end with '.txt', the condition becomes True and the code inside runs
if not filename.lower().endswith('.txt'):
    # This line runs ONLY if the filename is NOT a .txt file
    # Example: 'document.pdf' → endswith('.txt') is False → not False = True → this block executes
    print("Error: File is not a .txt file. Please provide a valid filename")
    
    # Stop the program because continuing with a non-.txt file would cause errors later
    quit()  


'''if not filename.lower().endswith('.txt'):
    print("Error: File is not a .txt file. Please provide a valid text file.")
    quit()  # Stop the program because the file type is invalid'''

# ---------------------------------------------------------------
# STEP 4: Try to open and read the file
# ---------------------------------------------------------------
# The 'try' block attempts the risky operation (opening a file).
# If something goes wrong (like the file not existing), it jumps to one of the 'except' blocks below.
try:
    # 'with open(filename, 'r') as file:' means:
    # - Open the file in "read" mode ('r').
    # - Assign it the name 'file' so we can use it in this block.
    # - Python automatically closes the file after this block finishes.
    with open(filename, 'r') as file:
        text = file.read()  # Read the entire contents of the file into one string variable

    # ---------------------------------------------------------------
    # STEP 5: Count the number of 'a' and 'A' characters
    # ---------------------------------------------------------------
    count = 0  # Start a counter at zero

    # Go through each character in the text, one by one
    for char in text:
        # Check if the current character is 'a' or 'A'
        # This makes the program case-insensitive without using .lower()
        if char == 'a' or char == 'A':
            count += 1  # Add 1 each time we find either version of 'a'

    # ---------------------------------------------------------------
    # STEP 6: Display the result
    # ---------------------------------------------------------------
    print(f"There are {count} occurrences of the letter 'a' or 'A'.")

    lower_a = 0  # Counter for lowercase 'a'
    upper_A = 0  # Counter for uppercase 'A'
    for char in text:
        # Compare each character individually.
        if char == 'a':
            lower_a += 1  # Increment lowercase count
        elif char == 'A':
            upper_A += 1  # Increment uppercase count
    # ---------------------------------------------------------------
    # STEP 6: Display the results
    # ---------------------------------------------------------------
    print(f"There are {lower_a} occurrences of lowercase 'a'.")
    print(f"There are {upper_A} occurrences of uppercase 'A'.")

# ---------------------------------------------------------------
# STEP 7: Handle errors gracefully
# ---------------------------------------------------------------
# This 'except' block runs if the file wasn’t found at the location given.
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the name and try again.")

# This 'except' block catches any other unexpected errors (e.g., permission issues, encoding errors).
except Exception as e:
    print(f"An unexpected error occurred: {e}")
