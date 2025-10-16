'''Write a program that reads in a text file and outputs the number of e's it contains. 
Think about what is being asked here, and document any assumptions you are making.
The program should take the filename from an argument on the command line. 
Need to research how to do this. 
Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.'''

import re

try:
    with open ('text.txt', 'r') as file:
        letters = file.read()

    contains_e = re.findall('[e]', letters)
    print(contains_e)

except FileNotFoundError:
    print('The file Text.txt was not found.')
    quit()

except PermissionError:
    print('You dont have permission to read the file')
    quit()
 
except UnicodeEncodeError:
    print('That is not a text file')
    quit()

except Exception as e:
    print(f'An unexpected error occurred {e}')


num = 0
for e in contains_e:
    if e == 'e':
        num = num +1

print(f' There are {num} instances of the letter e in the text.txt file')


