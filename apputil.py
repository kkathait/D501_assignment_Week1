

# add code below ...
import string
def palindrome(word):
    new_word = ""
    word = word.lower()
    word = word.translate(str.maketrans("", "", string.punctuation))

    for char in word:
        if char.isalnum():
            new_word += char
        
    return new_word == new_word[::-1]



print(palindrome("racecar"))
print(palindrome("Nurses Run"))
print(palindrome("Sit on a potato pan, Otis."))



def parentheses(case1):
    count = 0

    for char in case1:
        if char == "(" :
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False

    return count == 0


print(parentheses("((blah)()()())"))
print(parentheses("(((())blee))"))
print(parentheses("(()hello((())()))"))
print(parentheses("((((((())"))
print(parentheses("()))"))