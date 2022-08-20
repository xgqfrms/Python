

def letter_count(text, letter):
    #your code goes here
    total = 0
    for c in text:
        if(c == letter):
            total += 1
        else:
            continue
    return total

text = input()
letter = input()

print(letter_count(text, letter))




def search(word, text):
  if(word.find(text) > -1):
    return "Word found"
  else:
    return "Word not found"

text = input()
word = input()
print(search(text, word))


"""
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
"""
