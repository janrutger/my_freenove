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
            leftDistance, rightDistance = self.avgDistances(distances[1])

            leftPower  = round(((rightDistance - self.minDistance) / self.maxDistance)*100)
            rightPower = round(((leftDistance  - self.minDistance) / self.maxDistance)*100)
                           
            print("power percentage:", (leftPower,leftPower,rightPower,rightPower))
            return((leftPower,leftPower,rightPower,rightPower), False)

    def turn(self, distances):
        print("gemeten afstand:", distances)
        if min(distances[0]) < self.minDistance: #all vallues unsigned
            return((-100, -100, -100, -100), 0.3)
        else:
            avgLeftDistance, avgRightDistance = self.avgDistances(distances[1])
            if avgLeftDistance < avgRightDistance:
                return ((100, 100, -100, -100), 0.5)
            else:
                return((-100, -100, 100, 100), 0.5)
