class Cricket_Player:
    def __init__(self,playerName,playedCountry,playerAge,playerCountry):
        self.playerName = playerName
        self.playedCountry = playedCountry
        self.playerAge = playerAge
        self.playerCountry = playerCountry

class Solution:
    def __init__(self,objLis):
        self.playerList = objLis

    def countPlayers(self, countryName):
        count = 0
        for obj in self.playerList:
            if obj.playerCountry.lower() == countryName.lower():
                count = count + 1
        return count

    def getPlayerPlayedForMaxCountry(self):
        max = 0
        name = ""
        for obj in self.playerList:
            tempMax = len(obj.playedCountry)
            tempName =  obj.playerName
            if tempMax > max:
                max = tempMax
                name = tempName
        return name

objLis = []
for _ in range(int(input())):
    playerName = input()
    playedCountry = []
    for i in range(int(input())):
        temp = input()
        playedCountry.append(temp)
    playerAge = int(input())
    playerCountry = input()
    objLis.append(Cricket_Player(playerName,playedCountry,playerAge,playerCountry))

obj = Solution(objLis)
countryName = input()
res_1 = obj.countPlayers(countryName)
res_2 = obj.getPlayerPlayedForMaxCountry()
print(res_1)
print(res_2)

# 3
# virat
# 5
# aus
# nze
# eng
# wi
# pak
# 35
# ind
# raina
# 3
# aus
# pak
# nze
# 34
# ind
# gayle
# 3
# aus
# ind
# pak
# 42
# wi
# ind
