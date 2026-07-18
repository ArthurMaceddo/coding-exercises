def isPalindrome(s: str) -> bool:
    cleanText = "".join(char for char in s.lower() if char.isalnum())

    palindrome = cleanText[::-1]
    return cleanText == palindrome