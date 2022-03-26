



from turtle import right


class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def drive(self, distances):
        print("gemeten afstand:", distances)
        if min(abs(distances)) < self.minDistance:
            return((0,0,0,0), True)
        else:
            leftDistances  = []
            rightDistances = []
            for d in [distances[0], distances[2]]:
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
                pass
            elif avg(leftDistances) + avg(rightDistances) < 0:
                pass
            else:
                leftPower  =  round((avg(leftDistances) / self.maxDistance)*100)
                rightPower = round((avg(rightDistances) / self.maxDistance)*100)
                
            
            return((leftPower,leftPower,rightPower,rightPower), False)