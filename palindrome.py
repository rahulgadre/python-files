# Asking user to enter a word
word = raw_input ("Enter a word: ")
# Block of code to reverse the string
rev=word[::-1]
# show output on the screen
if (word==rev):
    print("The word is palindrome")
else:
    print("The word is not palindrome")