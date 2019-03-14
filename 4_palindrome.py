"""
Python skill test from:
https://www.testdome.com/questions/python/palindrome/24234?visibility=1&skillId=9

Author:
Anonymous

Score:
100% (3 pass / 0 fail)

Question:
A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. 
Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should 
be ignored, resulting in "deleveled", which is a palindrome since it reads the same 
backward and forward.
"""

######## Start Original script ########

# def is_palindrome(word):
#     return None
    
# print(is_palindrome('Deleveled'))

######## End Original script ########

def is_palindrome(word):
    reversed = word[::-1]
    if word.lower() == reversed.lower():
        return True
    
print(is_palindrome('Deleveled'))