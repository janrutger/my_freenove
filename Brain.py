from numpy import average as avg



class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def drive(self, distances):
        print("gemeten afstand:", distances)
        if min(distances[0]) < self.minDistance: #all vallues unsigned
            return((0,0,0,0), True)
        else:
            leftDistances  = []
            rightDistances = []
            for d in distances[1]:  #only signed values (delta angle != 0)
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
            print("berekende afstanden:", avg(leftDistances), avg(rightDistances))

            leftPower  = round(((avg(rightDistances) - self.minDistance) / self.maxDistance)*100)
            rightPower = round(((avg(leftDistances)  - self.minDistance) / self.maxDistance)*100)
            # if avg(leftDistances) + avg(rightDistances) > 0:
            #     leftPower  = (leftPower) * 1.0
            #     rightPower = rightPower * 0.3
            # elif avg(leftDistances) + avg(rightDistances) < 0:
            #     leftPower  = (leftPower) * 0.3
            #     rightPower = rightPower * 1.0
            # else:
            #     leftPower  = (leftPower) * 1.0
            #     rightPower = rightPower * 1.0
                           
            print("power percentage:", (leftPower,leftPower,rightPower,rightPower))
            return((leftPower,leftPower,rightPower,rightPower), False)