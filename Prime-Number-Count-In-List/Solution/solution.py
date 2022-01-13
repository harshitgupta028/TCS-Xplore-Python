# Prime Number Count

lis = []
count = 0
n = int(input())
for _ in range(n):
    lis.append(int(input()))

for i in range(0, n):
    if lis[i] != 1:
        for j in range(2, lis[i]):
            if lis[i] % j == 0:
                break
        else:
            count = count + 1

print(count)
