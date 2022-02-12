# 4
# 101
# Kadamb
# 500
# Portrait
# 102
# Suman
# 3000
# Portrait
# 103
# Suman
# 3000
# Modern
# 104
# Kadamb
# 3000
# portrait
# landscape

# 5
# 101
# Raman
# 50000
# Portrait
# 102
# Kamaal
# 30000
# Portrait
# 103
# Raman
# 25600
# Modern
# 104
# Preeti
# 31000
# landscape
# 105
# Sumiran
# 50000
# modern
# modern


class Painting:
    def __init__(self, paintingId, painterName, paintingPrice, paintingType):
        self.paintingId = paintingId
        self.painterName = painterName
        self.paintingPrice = paintingPrice
        self.paintingType = paintingType

class Showroom:
    def __init__(self, paintingObj):
        self.paintingList = paintingObj

    def getTotalPaintingPrice(self, type):
        su = 0
        isFound = False
        for obj in self.paintingList:
            if obj.paintingType.lower() == type.lower():
                su = su + obj.paintingPrice
                isFound = True
        if isFound:
            return su
        else:
            return "No painting found"

    def getPainterWithMaxCountOfPaintings(self):
        dic = {}
        for obj in self.paintingList:
            if obj.painterName not in dic:
                dic[obj.painterName] = 1
            else:
                dic[obj.painterName] = dic[obj.painterName] + 1

        dic1 = dict(sorted(dic.items(), key = lambda item:item[1], reverse=True))
        print(dic1)
        lis = []
        for k,v in dic1.items():
            if len(lis) == 0:
                lis.append(k)
                temp = v
            else:
                if temp == v:
                    lis.append(k)
                else:
                    break
        lis.sort()
        return lis[0]


paintingObj = []
for i in range(int(input())):
    paintingId = int(input())
    painterName = input()
    paintingPrice = int(input())
    paintingType = input()
    paintingObj.append(Painting(paintingId,painterName,paintingPrice,paintingType))

obj = Showroom(paintingObj)
type = input()
totalPrice = obj.getTotalPaintingPrice(type)
painter = obj.getPainterWithMaxCountOfPaintings()
# painter.sort()
print(totalPrice)
print(painter)
