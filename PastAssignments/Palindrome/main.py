#Luke Murdock, Palindrome

word = input("What is your word?:")

if word [::-1] == word:
 answer = "is"
else:
 answer = "is not"

print(word, answer,"a palindrome")