#Freenover stuff
from Motor import *
from Ultrasonic import *
from ADC import *

#system stuff
from numpy import average as avg
import time

#My stuff
import Brain as b


class Auto:
    def __init__(self):
        self.motor = Motor()
        self.sonar = Ultrasonic()
        self.adc   = Adc()
        self.brain = b.Brain()

        self.maxSpeed = 800
        self.minSpeed = 300


        print("------- STARTING -------")
        self.sonar.init_sonar()
        self.battery()
        answer = input("Turn motor on (yes):")
        if answer == "yes":
            self.motorEnable = True
        else:
            self.motorEnable = False
        

        
    #def init_sonar(self):
    #    self.sonar.init_sonar()

    def battery(self):
        battery=self.adc.recvADC(2)*3
        print ("Battery :",battery)

    def drive(self, power):
        speed = []
        for i in power:
            _speed = round((i/100)*self.maxSpeed)
            if abs(_speed) < self.minSpeed * 1.3:
                _speed = 0
            speed.append(int(_speed))
        print("calculated speed:", speed)

        if self.motorEnable:
            #print(self.motorEnable)
            self.motor.setMotorModel(speed[0], speed[1], speed[2],speed[3])
        return(speed)

        
    def halt(self):
        print("------- HALTING -------")
        self.motor.setMotorModel(0,0,0,0)
        self.sonar.init_sonar()
        

    def run(self):
        stopped = False
        while True:
            if not stopped:
                print("------- NEXT RUN -------")
                distances = self.sonar.get_angleDistance((-30,0,30))
                power, stopped = self.brain.drive(distances)
                speed = self.drive(power)
                if not stopped and avg(speed) == 0:
                    time.sleep(0.5)
                    distances = self.sonar.get_angleDistance((-60, -30, 0, 30, 60))
                    power, timer = self.brain.turn(distances)
                    _ = self.drive(power)
                    time.sleep(timer)
                    self.motor.setMotorModel(0,0,0,0)
                    #stopped = True

            else:
                self.halt()
                answer = input("Restart the car (yes):")
                if answer == "yes":
                    stopped = False
               



auto = Auto()
if __name__ == '__main__':
    print ('Auto is starting up ... ')
    try:
        auto.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("Auto halted now ...")
        auto.halt()