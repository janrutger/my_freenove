#Freenover stuff
from tkinter.messagebox import YES
from Motor import *
from Ultrasonic import *
from ADC import *

#system stuff
import time

#My stuff
import Brain as b


class Auto:
    def __init__(self):
        self.motor = Motor()
        self.sonar = Ultrasonic()
        self.adc   = Adc()

        self.brain = b.Brain()
        self.maxSpeed = 1000
        answer = input("Turn motor on (yes):")
        if answer == "yes":
            self.motorEnable = True
        else:
            self.motorEnable = False

        
    def init_sonar(self):
        self.sonar.init_sonar()

    def battery(self):
        battery=self.adc.recvADC(2)*3
        print (battery)

    def drive(self, power):
        speed = []
        for i in power:
            speed.append(round((i/100)*self.maxSpeed))

        print("calculated speed:", speed)
        if self.motorEnable:
            print(self.motorEnable)
            self.motor.setMotorModel(speed[0], speed[1], speed[2],speed[3])
        
    def halt(self):
        self.motor.setMotorModel(0,0,0,0)
        self.sonar.init_sonar()
        




    def run(self):
        while True:
            self.battery()
            distance = self.sonar.get_distance()
            power = self.brain.manual(distance)
            print("power percentage:", power)
            self.drive(power)

            
            time.sleep(0.002)












auto = Auto()
if __name__ == '__main__':
    print ('Auto is starting up ... ')
    try:
        auto.init_sonar()
        auto.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("Auto halted now ...")
        auto.halt()