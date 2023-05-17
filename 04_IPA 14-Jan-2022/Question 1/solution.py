st1 = input()
st2 = input().lower()
flag = False

for word in st1.split():
    for ch in word:
        if not ch.lower() in st2:
            flag = True
            break
    if flag:
        break

if flag:
    print("Input string is not valid")
    print(st1)
else:
    print("Input string is valid")
    print(st1)

    
    
 """
 
# straight forward approach
n = int(input())
for i in range(0,n):
    a = input()
    b = input()
    c = b.upper() + b.lower() # gathering all the lower case and upper case possibilities of the letters present in the second string
    k = 0

    for j in a:
        if j not in c:
            print("string is invalid")
            print(a)
            break
        k += 1
    if(k == len(a)):
        print("string is valid")
        print(a)
 
 """
