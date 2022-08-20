txt = input()

#your code goes here

words = txt.split(" ")

# print(words)

maxLen = 0
maxWord = ""

for word in words:
    l = len(word)
    if(l > maxLen):
        maxLen = l
        maxWord = word
print(maxWord)
