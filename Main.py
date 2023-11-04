import Player
import Game
import League

t1 = []
t2 = []

for i in range(5):
    t1.append(Player.Player())
    t2.append(Player.Player())


Game.Game(t1,t2,50).playGame()



def sortByNet(p):
    return p.points-p.pointsAllowed

#for p in sorted(t1,reverse=True,key=sortByNet):
#    print(f"{p.name}, {round(p.points/p.offPoss*100,1)}, {round(p.points/(p.shots)*100,1)}, {round(p.orebs/(p.shots-p.points)*100,1)}, {round(p.tovs/p.offPoss*100,1)}, {round(p.pointsAllowed/p.defPoss*100,1)}, {round(p.pointsAllowed/(p.shotsAllowed)*100,1)}, {round(p.drebs/(p.shotsAllowed-p.pointsAllowed)*100,1)}, {round(p.locks/p.defPoss*100,1)}")




# t1 = sorted(t1,reverse=True,key=sortByNet)[:20]


# for p in t1:
#     p.clear()    



# Game.Game(t1,t1,10).playGame()


# for p in sorted(t1,reverse=True,key=sortByNet):
#     print(f"{p.name}, {round(p.points/p.offPoss*100,1)}, {round(p.points/(p.shots)*100,1)}, {round(p.orebs/(p.shots-p.points)*100,1)}, {round(p.tovs/p.offPoss*100,1)}, {round(p.pointsAllowed/p.defPoss*100,1)}, {round(p.pointsAllowed/(p.shotsAllowed)*100,1)}, {round(p.drebs/(p.shotsAllowed-p.pointsAllowed)*100,1)}, {round(p.locks/p.defPoss*100,1)}")




    
