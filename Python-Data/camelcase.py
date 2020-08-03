input = raw_input("Enter a string \n").lower() #Getting a string from user and making it to lower case
words = input.split(' ') #Splitting the string into words
capitalized = [] #initializing a list to store each word after making first letter capital
for word in words:
    final_words = word[0].upper() + word[1:] #Converting first letter to upper case and appending it with remaining letters
    capitalized.append(final_words) #Appending all words into capitalized list
output = ' '.join(capitalized) #At last joining each word togather to make a string
print output #Priting the final output
