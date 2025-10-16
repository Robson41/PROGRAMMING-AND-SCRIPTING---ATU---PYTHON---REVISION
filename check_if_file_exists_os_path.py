'''Question:
Write a Python program that:
Checks if a file called "log.txt" exists in the current directory.
If the file does not exist, print "Log file not found" and create the file with the text "Log start\n" inside it.
If the file does exist, print "Log file found" and leave it unchanged.
Hints:
Use os.path.isfile() to check if the file exists.
Use with open(filename, "w") as f: to create and write to the file.'''

import os.path

FILENAME = 'log.txt'

if not os.path.isfile(FILENAME):
    print(f'{FILENAME} file not found')
    with open(FILENAME, 'w') as w:
        file = w.write('Log start\n')
        print(f'{FILENAME} file has now been created with content')
else:
    print(f'{FILENAME} file found')

    
