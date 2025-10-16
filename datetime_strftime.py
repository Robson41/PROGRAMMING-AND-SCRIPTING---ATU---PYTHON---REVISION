'''Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)'''
'''
weekday.py

This program outputs whether today is a weekday or not.

Python concepts covered:
1. Importing modules (`from datetime import datetime`) to use built-in functionality.
2. Working with datetime objects (`datetime.today()`).
3. Using methods on objects (`.strftime()`) to extract specific information.
4. Format codes in strftime, e.g., "%A" gives the full weekday name.
5. Conditional statements (if/else) to make decisions based on program logic.
6. String formatting with f-strings for clear output.

Key Python principle:
- Extracting and transforming data from objects.
- Conditional logic to branch program behavior.
'''

from datetime import datetime  # Import the datetime module to work with dates and times

# Get the current date and time as a datetime object
today = datetime.today()  
# 'today' is a datetime object representing the exact current date and time
# Example: 2025-10-09 14:30:45.123456

# Extract the full name of the weekday from the datetime object
full_name = today.strftime('%A')  
# '%A' is a strftime format code that converts the datetime object into the full weekday name
# Example: if today is Thursday, full_name will be 'Thursday'
# Other codes: '%a' -> abbreviated weekday, '%d' -> day of month, '%Y' -> year

# Define the weekdays (Monday to Friday)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Check if today is a weekday
if full_name in weekdays:
    # Conditional logic: if today's name is in the weekdays list, print it's a weekday
    print(f"{full_name} is a weekday")
else:
    # Else, today must be Saturday or Sunday
    print(f"{full_name} is not a weekday")

'''
Summary of flow:
1. datetime.today() -> creates a datetime object with current date/time.
2. .strftime('%A') -> extracts the full weekday name from the datetime object.
3. if full_name in weekdays -> checks if today is Monday to Friday.
4. print() -> outputs the result using f-string formatting.

Python principles reinforced:
- Module usage (datetime)
- Object methods (.strftime)
- Format codes for dates and times
- Conditional statements
- String formatting and output
'''




    



