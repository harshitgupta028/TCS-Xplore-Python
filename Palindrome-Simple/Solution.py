# palindrome

def check_palindrome(lis):
    palin_lis = []
    for i in lis:
        if i == i[::-1]:
            palin_lis.append(i)
    return palin_lis

lis = []
for i in range(int(input())):
    lis.append(input())

for _ in check_palindrome(lis):
    print(_)
