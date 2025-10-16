'''Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).'''
# list_index_range_min_masking_demo.py
# -----------------------------
# This program reads a 10-character bank account number
# and masks the first 6 characters with 'X', showing only the last 4.
# Extra: it can handle account numbers of any length.
# -----------------------------

# Step 0: Define the masking character
# We want to replace some characters with 'X'.
mask_l = "X"

# Step 1: Read input from the user
# input() always returns a string, even if the user types numbers.
# Example: user enters "1234567890" → input() returns the string "1234567890"
# We then convert this string to a list of characters using list()
# This allows us to manipulate individual characters easily.
# Each element of the list is still a string, not an integer.
acc_num = list(input("Please enter a 10 character account number: "))

# Example after input "1234567890":
# acc_num = ['1','2','3','4','5','6','7','8','9','0']
# Index:     0  1  2  3  4  5  6  7  8  9
# Values:    1  2  3  4  5  6  7  8  9  0

# Step 2: Mask the first 6 digits
# We use a for loop to iterate over the indices of the first 6 elements.
# Syntax: for i in range(n)
# - range(n) generates numbers from 0 to n-1.
#   Example: range(6) → 0,1,2,3,4,5
# - 'i' takes each number from the range one by one. These are the indices.
# - Using acc_num[i] lets us access the element at index i.
# - We assign acc_num[i] = mask_l to replace it with 'X'.

# Important: We use min(6, len(acc_num)) to achieve two things:
# 1. Mask the first 6 digits (per the requirement)
# 2. Add a safety check so that if the account number has fewer than 6 digits,
#    we don’t try to access indices that don’t exist, preventing an IndexError

for i in range(min(6, len(acc_num))):
    # i is the index of the current element to mask
    # acc_num[i] accesses the element at that index
    # mask_l = "X" replaces that element
    acc_num[i] = mask_l

    # Visual representation (example with "1234567890"):
    # Iteration 1: i = 0 → acc_num[0] = 'X'
    # Index:   0 1 2 3 4 5 6 7 8 9
    # Value:   X 2 3 4 5 6 7 8 9 0
    # Iteration 2: i = 1 → acc_num[1] = 'X'
    # Index:   0 1 2 3 4 5 6 7 8 9
    # Value:   X X 3 4 5 6 7 8 9 0
    # Iteration 3: i = 2 → acc_num[2] = 'X'
    # ...
    # After all 6 iterations:
    # Index:   0 1 2 3 4 5 6 7 8 9
    # Value:   X X X X X X 7 8 9 0

# Step 3: Convert the list back to a string
# acc_num is currently a list of strings, e.g. ['X','X','X','X','X','X','7','8','9','0']
# Printing a list directly would show brackets and commas:
# ['X', 'X', 'X', 'X', 'X', 'X', '7', '8', '9', '0']
# We use ''.join(acc_num) to concatenate all elements into a single string.
# - ''.join() is a method that takes an iterable (like a list of strings)
#   and combines the elements into one string, inserting the string before the dot as a "separator".
# - In this case, we use an empty string '' as the separator, meaning nothing is inserted between elements.
# - All elements must be strings; in our code they are strings because input() returns strings.
asked_acc_num = ''.join(acc_num)

# Example after join:
# acc_num = ['X','X','X','X','X','X','7','8','9','0']
# asked_acc_num = "XXXXXX7890"

# Step 4: Print the masked account number
print(asked_acc_num)

# ✅ Output example:
# $ python accounts.py
# Please enter an 10 character account number: 1234567890
# XXXXXX7890

# -----------------------------
# Key points recap:
# 1. input() → always returns a string
# 2. list(string) → splits the string into individual characters
# 3. for i in range(min(6,len(acc_num))):
#    - i takes each index from 0 up to 5 (or fewer if account number shorter)
#    - acc_num[i] = mask_l replaces that element with 'X'
# 4. ''.join(acc_num) → concatenates list elements into a single string
# 5. Using min(6, len(acc_num)) ensures code works for account numbers of any length
# 6. All operations work on strings; no type conversion needed here
# 7. The "heavy lifting" is done by the for loop; join() is formatting
# -----------------------------

# Extra notes / clarifications:
# - If acc_num = list("978"), min(6,3) → 3, loop runs 3 times
#   Result: ['X','X','X'] → join → "XXX"
# - range(n) always generates values 0 to n-1, which we can use as list indices
# - acc_num[i] accesses the element at index i; it **always retrieves or sets the value**, not the index
# - The separator in join() is mandatory; '' just means no characters are inserted between elements
