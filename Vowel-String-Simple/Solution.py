# Vowels Strings

def vowelString(lis):
    st = 'aeiou'
    vowel_lis = []
    for str in lis:
        count = 0
        for let in str:
            if let in st:
                count = count + 1
        if count <= 1:
            vowel_lis.append(str)
    return vowel_lis

lis = []
for _ in range(int(input())):
    lis.append(input())

for i in vowelString(lis):
    print(i)
