def isAnagram(s, t):
    myDict = {}
    mySecDict = {}

    if len(s) != len(t):
        return False

    for letter in s:
        if letter in myDict:
            myDict[letter] += 1
        else:
            myDict[letter] = 1

    for letter in t:
        if letter in mySecDict:
            mySecDict[letter] += 1
        else:
            mySecDict[letter] = 1

    return myDict == mySecDict