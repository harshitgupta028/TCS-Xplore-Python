st = input()
n = int(input())

if len(st) % 2 != 0:
    mid = len(st)//2
else:
    mid = (len(st)//2) - 1

if len(st[mid:mid+n]) == n:
    print(st[mid:mid+n])
else:
    print(st[mid:])
