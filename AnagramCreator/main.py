#Luke Murdock, Anagram Creator

import random

name = input("What is your name?: ")
userNum = int(input("How many anagrams do you want?: "))

num = 1
while num <= userNum:
  letters = list(name.lower())  
  random.shuffle(letters)
  anagram = "".join(letters).title()
  print(anagram)
  num += 1
