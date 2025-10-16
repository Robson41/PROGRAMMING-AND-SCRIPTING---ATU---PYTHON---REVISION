'''Question:
Write a Python program that asks the user for their age and prints whether they are eligible to vote.
A person can vote if they are 18 or older.
Use a Boolean expression to determine eligibility.
Example Output:
Enter your age: 20
Eligible to vote: True
Enter your age: 16
Eligible to vote: False
'''

age = int(input('Please provide your age: '))

if age > 18:
    print('You are old enough to vote')
else:
    print('You are too young to vote')