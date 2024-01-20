# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# pseudocode

# ask user to input a word
random_word = input ("Kindly input a word:")

# print the word 
print ("You enter the word", random_word)
print("Here are all even index letters")

# determine the length of the word
word_length = len(random_word)

# only present even index number
for i in range (0, word_length,2):
# print all even index character
    print (random_word[i])