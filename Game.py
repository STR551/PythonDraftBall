import math
import random
import Player

class Game():

    def __init__(self,team1,team2,poss):
        self.team1 = team1
        self.team2 = team2
        self.scoreTo = poss

        def __init__(self,team1):
            self.team1 = team1



    def playGame(self):

        t1score = 0
        t2score = 0

        player1 = self.team1[0]
        player2 = self.team2[0]
        
        while t1score < self.scoreTo and t2score < self.scoreTo:
            result = playPossesion(player1,player2)
            if result == 1:
                t1score +=1
            else:
                t2score += 1

        #print(t1score,t2score)




def playPossesion(p1,p2):
        onOff,onDef = kickoff(p1,p2)
        p1.poss += 1
        p2.poss += 1
        
        
        while True:
            result = singlePlay(onOff,onDef)

            #offense scored
            if result == 1:
                if onOff == p1:
                    #print(p1.name+" scored")
                    return 1
                if onOff == p2:
                    #print(p2.name+" scored")
                    return 2
                
            #offense got ball back
            if result == 2:
                continue

            #defense got ball
            if result == 3:
                temp = onOff
                onOff = onDef
                onDef = temp

                onOff.playO += 1
                onDef.playD += 1
                continue



            #determine if locked
            
            


def kickoff(p1,p2):
    s1 = p1.skills[6]
    s2 = p2.skills[6]

    s1KeepBall  = (s1+10)/(s1+s2+20)
    if random.random() < s1KeepBall:
        p1.playO +=1
        p2.playD += 1
        p1.koWins += 1
        p2.koLosses += 1
        #print(1)
        return p1,p2
    else:
        p1.playD +=1
        p2.playO += 1
        p2.koWins += 1
        p1.koLosses += 1
        #print(2)
        return p2,p1





def singlePlay(p1,p2):
    #print(p1.name+" vs "+p2.name)
    s1 = p1.skills[2]
    s2 = p2.skills[5]

    keepBall  = (p1.skills[2]*5+50)/(p1.skills[2]*5+p2.skills[5]+60)
    if random.random() > keepBall:
        p1.tovsO +=1
        p2.tovsD += 1
        return 3
    


    s1 = p1.skills[0]
    s2 = p2.skills[3]

    p1.shotsO += 1
    p2.shotsD += 1
    makeShot  = (p1.skills[0]+10)/(p1.skills[0]+p2.skills[3]+20)
    if random.random() < makeShot:
        p1.pointsO += 1
        p2.pointsD += 1
        return 1
    

    
    p1.shotsMissedO += 1
    p2.shotsMissedD += 1

    s1 = p1.skills[1]
    s2 = p2.skills[4]
    offReb  = (10+p1.skills[1])/(p1.skills[1]+p2.skills[4]*3+40)
    
    if random.random() > offReb:
        p2.rebsD += 1
        return 3
        
    
    
    p1.rebsO += 1
    #print("OREB")
    return 2




