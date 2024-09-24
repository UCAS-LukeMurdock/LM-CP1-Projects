# #Luke Murdock, Secret Cypher

# usersWord = input("What word do you want cyphered?: ")

# def cypher(first, k):
#     # k = k
#     secret = (word)
    
#     return secret




# print(cypher(usersWord))


def rotate_list(lst, k):
  """Rotates a list 'lst' by 'k' positions to the right."""
  k = k % len(lst)  # Handle rotations larger than the list length
  if (k > len(lst)) :
    return "sorry. key is greater than length of list"
  
  return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
word = list("Hello")
rotated_list = rotate_list(word, 6)

print(rotate_list())