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
