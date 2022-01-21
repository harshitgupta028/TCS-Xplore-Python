# Input:
# 4
# HelloGood Morning
# abcd123Fghy
# India
# Progoto.c

# Output:
# Count Of Valid String = 2
# Count of Invalid String = 2

def isValidString(strLis):
    countValidString = 0
    CountInvalidString = 0
    for str in strLis:
        temp = ""
        for word in str.split():
            temp = temp + word.strip()
        if temp.isalpha():
            countValidString = countValidString + 1
        else:
            CountInvalidString = CountInvalidString + 1
    return [countValidString,CountInvalidString]

strLis = []
for i in range(int(input())):
    strLis.append(input())

valid,Invalid = isValidString(strLis)
print("Count Of Valid String = ",valid)
print("Count of Invalid String =",Invalid)
