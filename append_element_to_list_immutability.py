'''Append an extra element to a list'''
queue = [1, 2, 3]

appended_queue = queue.append(4)

print(appended_queue)

name = 'Bob'
New_name = 'Alice'

New_name = name

print(New_name)


'''Lists (mutable): Python can safely modify the original object in place, so there’s no need to create a new list when you do something like .append(). That’s why queue.append(4) changes the list itself and returns None.
Strings (immutable): You cannot change the existing string — it’s locked in memory. So when you “change” a string (like New_name = name), Python has no choice but to create a new string object and make your variable point to it.
✅ In short:
Mutable → can change in place, no new object needed.
Immutable → must create a new object to reflect a change.
It’s all about whether Python can safely reuse the existing object.
'''


