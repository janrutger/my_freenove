



class Brain:
    def __init__(self):
        self.maxDistance = 60


    def manual(self, distance):
        if distance < 30:
            return((0,0,0,0))
        else:
            power = round(((self.maxDistance - distance)/self.maxDistance)*100)
            return((power,power,power,power))