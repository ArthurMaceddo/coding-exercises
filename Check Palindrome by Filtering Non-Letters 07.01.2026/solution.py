def isAlphabeticPalindrome(code):
    
    phrase = ''.join(char for char in code.lower() if char.isalpha())
    palindrome = phrase[::-1]
    
    if palindrome == phrase:
        return True
        
    if palindrome != phrase:
        return False
    

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))