animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # create new list
print(animals)

animals[1:3] = ['cat']
# replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
print(animals)

animals[1:3] = []
# remove 2 items -- 'cat' and 'giraffe' from the list
print(animals)
# print(animals.len())
print(animals.__len__())
animals[:3] = []
print(animals)