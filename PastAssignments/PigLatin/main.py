#Luke Murdock, Pig Latin Converter

userWord = input("What word do you want in pig latin?: ")

def converter(word):
    endWord = word[0] + "ay"
    startWord = word[1:]
    return startWord + endWord 

print(converter(userWord))