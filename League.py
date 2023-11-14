import Game
import Player

def sortByNet(p):
    return p.pointsO

def playPreseason(pList):
    for p1 in pList:
        for p2 in pList:
            if p1 != p2:
                Game.playPossesion(p1,p2)
    i = 1
    for p in sorted(pList,reverse=True,key=sortByNet):
        print(f"{str(i).ljust(3)} {p.name.ljust(20)} {round((p.pointsO) / p.poss * 100, 1)} {round(p.koWins / (p.koWins + p.koLosses) * 100, 1)} {round(p.pointsO / p.playO * 100, 1)} {round(p.pointsD / p.playD * 100, 1)}",end=" ")
        for s in p.skills:
            print(str(round(s)).ljust(3),end="")
        print()
        i+=1



pList = []

for i in range(250):
    pList.append(Player.Player())

playPreseason(pList)



