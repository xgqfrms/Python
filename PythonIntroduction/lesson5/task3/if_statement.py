name = "John"
age = 17

if name == "John" or age == 17:   # check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")

tasks = ['task1', 'task2']    # create new list

if len(tasks) == False:
    print("empty")
# if len(tasks) is False:
# if len(tasks) == False:
# if len(tasks) == 0:
# if len(tasks) is 0:
# if not tasks:
# if bool(tasks):
'''
# For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
# xxx == your list name
Yes: if not xxx:
     if xxx:
No:  if len(xxx):
     if not len(xxx):
'''