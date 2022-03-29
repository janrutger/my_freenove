from numpy import average as avg



class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def avgDistances(self, distances):
        leftDistances  = []
        rightDistances = []
        for d in distances:  #only signed values (delta angle != 0)
            if d < 0:
                if abs(d) < self.maxDistance + self.minDistance:
                    leftDistances.append(abs(d))
                else:
                    leftDistances.append(self.maxDistance + self.minDistance)
            else:
                if d < self.maxDistance + self.minDistance:
                    rightDistances.append(d)
                else:
                    rightDistances.append(self.maxDistance + self.minDistance)

        print("berekende afstanden:", (leftDistances), (rightDistances))
        return(avg(leftDistances), avg(rightDistances))



    def drive(self, distances):
        print("gemeten afstand:", distances)
        if min(distances[0]) < self.minDistance: #all vallues unsigned
            return((0,0,0,0), True)
        else:
            leftDistances, rightDistances = self.avgDistances(distances[1])

            leftPower  = round(((avg(rightDistances) - self.minDistance) / self.maxDistance)*100)
            rightPower = round(((avg(leftDistances)  - self.minDistance) / self.maxDistance)*100)
                           
            print("power percentage:", (leftPower,leftPower,rightPower,rightPower))
            return((leftPower,leftPower,rightPower,rightPower), False)