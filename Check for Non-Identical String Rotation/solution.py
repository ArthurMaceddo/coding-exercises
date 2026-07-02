def isNonTrivialRotation(s1, s2):
    if len(s1) != len(s2):
        return 0
    if s1 == s2:
        return 0 
        
    s3 = s1 + s1
    
    result = s3.find(s2)
    
    if result == -1:
        return 0
    else:
        return True
 
    

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
