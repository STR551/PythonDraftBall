import random

def genTeamList():
    retList = [[],[]]
    nameFile = open("namesList.txt","r")
    for line in nameFile:
        names = line.strip("\n").split(" ")
        retList[0].append(names[0])
        retList[1].append(names[1])

    return retList



   


class Player:
  
    idCounter = 0
    nameList = genTeamList()

    def __init__(self):
        self.id = Player.idCounter+1
        Player.idCounter+=1
        self.name = self.getName()
        self.age = 10
        self.skills = self.getSkills()
        self.potentials = [0]*6


        self.poss = 0
        self.koWins = 0
        self.koLosses = 0


        self.playO = 0
        self.playD = 0


        self.pointsO = 0
        self.pointsD = 0
        self.rebsO = 0
        self.rebsD = 0
        self.tovsO = 0
        self.tovsD = 0
        self.shotsO = 0
        self.shotsD = 0
        self.shotsMissedO = 0
        self.shotsMissedD = 0



    def getName(self):
        f = Player.nameList[0][random.randint(0,len(Player.nameList[0])-1)]
        l = Player.nameList[1][random.randint(0,len(Player.nameList[1])-1)]
        return f+" "+l
    

    def getSkills(self):
        numSkills = 7
        ret = []
        for i in range(numSkills):
            ret.append(random.random()**3*100)

        return ret
    
    def clear(self):
        self.offPoss = 0
        self.points = 0
        self.orebs = 0
        self.tovs = 0
        self.shots = 0
        self.defPoss = 0
        self.pointsAllowed = 0
        self.drebs = 0 
        self.locks = 0
        self.shotsAllowed = 0
