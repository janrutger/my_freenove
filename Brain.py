



class Brain:
    def __init__(self):
        self.maxDistance = 60
        self.minDistance = 30

    def manual(self, distance):
        print("gemeten afstand:", distance)
        if distance < self.minDistance:
            return((0,0,0,0), True)
        else: 
            distance = distance - self.minDistance       
            if distance > self.maxDistance:
                distance = self.maxDistance
                
            print("berekende afstand:", distance)
            power = round((distance / self.maxDistance)*100)
            return((power,power,power,power), False)