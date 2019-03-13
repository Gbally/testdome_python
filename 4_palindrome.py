def is_palindrome(word):
    reversed = word[::-1]
    if word.lower() == reversed.lower():
        return True
    
print(is_palindrome('Deleveled'))