from numpy import average as avg



class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def drive(self, distances):
        print("gemeten afstand:", distances)
        if min(distances[1]) < self.minDistance:
            return((0,0,0,0), True)
        else:
            leftDistances  = []
            rightDistances = []
            for d in [distances[0][0], distances[0][2]]:
                if d < 0:
                    if abs(d) < self.maxDistance:
                        leftDistances.append(d)
                    else:
                        leftDistances.append(-self.maxDistance)
                else:
                    if d < self.maxDistance:
                        rightDistances.append(d)
                    else:
                        rightDistances.append(self.maxDistance)
            print("berekende afstanden:", avg(leftDistances), avg(rightDistances))
            

            if avg(leftDistances) + avg(rightDistances) > 0:
                leftPower  =  round((avg(leftDistances) / self.maxDistance)*100)
                leftPower  = abs(leftPower) * 1.0
                rightPower = round((avg(rightDistances) / self.maxDistance)*100)
                rightPower = rightPower * 0.8
            elif avg(leftDistances) + avg(rightDistances) < 0:
                leftPower  =  round((avg(leftDistances) / self.maxDistance)*100)
                leftPower  = abs(leftPower) * 0.8
                rightPower = round((avg(rightDistances) / self.maxDistance)*100)
                rightPower = rightPower * 1.0
            else:
                leftPower  =  round((avg(leftDistances) / self.maxDistance)*100)
                leftPower  = abs(leftPower) * 1.0
                rightPower = round((avg(rightDistances) / self.maxDistance)*100)
                rightPower = rightPower * 1.0
                
            
            return((leftPower,leftPower,rightPower,rightPower), False)