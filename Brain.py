



class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def manual(self, distance):
        print("gemeten afstand:", distance)
        if distance < self.minDistance:
            return((0,0,0,0), True)
        else:           
            if (distance - self.minDistance) > self.maxDistance:
                distance = self.maxDistance + self.minDistance
                print("berekende afstand:", distance)

        power = round(((distance - self.minDistance) / self.maxDistance)*100)
        return((power,power,power,power), False)