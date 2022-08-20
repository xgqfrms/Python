
file = open("/usercode/files/books.txt", "r")

#your code goes here
lines = file.readlines() 

# print(lines)
# ['Harry Potter\n', 'The Hunger Games\n', 'Pride and Prejudice\n', 'Gone with the Wind']

for line in lines:
    # print(line.slice(0, 1) + len(line))
    # AttributeError: 'str' object has no attribute 'slice'
    print(line[0] + str(len(line.replace("\n", ""))))

file.close()
