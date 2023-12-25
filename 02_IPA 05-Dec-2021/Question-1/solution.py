def isPresent(lis,st):
    for i in range(0, len(lis)):
        if lis[i] == st:
            return i
    else:
        return -1

lis = []
for j in range(int(input())):
    lis.append(input())
st = input()

ind = isPresent(lis,st)

if ind == -1:
    print("String not found")
else:
    print("Position of the searched string is: ",ind)


# Input:
# 4
# Hello Good Morning
# abcd123Fghy
# India
# Progoti.c
# India

# Output:
# Position of the searched string is: 2
