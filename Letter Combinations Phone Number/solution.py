def minTasksToCancelForNoConflict(digits):
    
# -----------------------------------
  
        
    telephone = {
        "2": 'abc',
        "3": 'def',
        "4": 'ghi',
        "5": 'jkl',
        "6": 'mno',
        "7": 'pqrs',
        "8": 'tuv',
        "9": 'wxyz',
        "0": '0',
        "1": '1'
    }
    
    combinations = []
    
    def backtracking(index, char):
        if index == len(digits): # confirmacao pra quando salvar
            combinations.append(char)
            return
        for c in telephone[digits[index]]:
            backtracking(index + 1, char + c)
            
    backtracking(0,"")
    return combinations
            
# -----------------------------------

if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))
