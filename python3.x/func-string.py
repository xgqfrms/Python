

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
