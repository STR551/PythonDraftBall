import math
import random

class Game():

    def __init__(self,team1,team2,poss):
        self.team1 = team1
        self.team2 = team2
        self.scoreTo = poss


    def playGame(self):
        for player1 in self.team1:
            for player2 in self.team2:
                if player1 != player2:
                    for player in range(self.scoreTo):
                        self.playPossesion(player1,player2)
                        self.playPossesion(player2,player1)





    def playPossesion(self,p1,p2):
        offenseHasBall = True
        p1.offPoss += 1
        p2.defPoss += 1
        while offenseHasBall:

            #determine if locked
            
            s1 = p1.skills[2]
            s2 = p2.skills[5]

            keepBall  = 1-1/(1+math.exp((p1.skills[2]-p2.skills[5]+16.48)/15))
            if random.random() > keepBall:
                p1.tovs +=1
                p2.locks += 1
                return
            
            s1 = p1.skills[0]
            s2 = p2.skills[3]


            p1.shots += 1
            p2.shotsAllowed += 1
            makeShot  = 1-1/(1+math.exp((p1.skills[0]-p2.skills[3])/30))
            if random.random() > makeShot:
                p1.points += 1
                p2.pointsAllowed += 1
                return
            
            s1 = p1.skills[1]
            s2 = p2.skills[4]
            offReb  = 1-1/(1+math.exp((p1.skills[1]-p2.skills[4]-42.37)/50))
            if random.random() > offReb:
                p2.drebs += 1
                return
                
            
            p1.orebs += 1




            
            
            


