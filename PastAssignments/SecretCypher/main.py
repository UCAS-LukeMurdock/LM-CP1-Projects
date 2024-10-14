#Luke Murdock, Secret Cypher

usersWord = input("What word do you want cyphered?: ")
userShift = int(input("How many times do you want it shifted? (Negative numbers unshift): "))
secret = ""

def cypher(word,secret):
    for a in word:

        num = ord(a)
        num += userShift
        secret += chr(num)

    return secret

print(usersWord)
print(cypher(usersWord,secret))