import time

from numpy import average
from Motor import *
import RPi.GPIO as GPIO
from servo import *
from PCA9685 import PCA9685
class Ultrasonic:
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)

        self.pwm_S=Servo()


    def send_trigger_pulse(self):
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def wait_for_echo(self,value,timeout):
        count = timeout
        while GPIO.input(self.echo_pin) != value and count>0:
            count = count-1
     
    def get_distance(self):
        distance_cm = []
        for i in range(3):
            self.send_trigger_pulse()
            self.wait_for_echo(True,10000)
            start = time.time()
            self.wait_for_echo(False,10000)
            finish = time.time()
            pulse_len = finish-start
            distance_cm.append(pulse_len/0.000058)
        #print("distance array:", distance_cm)
        return int(average(distance_cm))

    def get_angleDistance(self, angles):
        distancesSigned = []
        distances = []
        for i in angles:
            #set the sonor 
            self.pwm_S.setServoPwm('0', (90 + i))
            time.sleep(0.2)
            #Get diastance
            distance = self.get_distance()
            if i < 0:
                distancesSigned.append(-distance)
            elif i > 0:
                distancesSigned.append(distance)
            print(i, 90+i, distance)
            distances.append(distance)

        #report values
        result = (distances, distancesSigned)
        return(result)

    def init_sonar(self):
        print("Init Sonar System")
        #self.pwm_S.setServoPwm('1', 120)
        self.pwm_S.setServoPwm('0', 120)
        time.sleep(1)
        #self.pwm_S.setServoPwm('1', 105)
        self.pwm_S.setServoPwm('0', 60)
        time.sleep(1)
        self.pwm_S.setServoPwm('0', 90)
        #self.pwm_S.setServoPwm('1', 120)
        time.sleep(1)
        self.pwm_S.setServoPwm('1', 90)



       
#     def run_motor(self,L,M,R):
#         if (L < 30 and M < 30 and R <30) or M < 30 :
#             self.PWM.setMotorModel(-1450,-1450,-1450,-1450) 
#             time.sleep(0.1)   
#             if L < R:
#                 self.PWM.setMotorModel(1450,1450,-1450,-1450)
#             else :
#                 self.PWM.setMotorModel(-1450,-1450,1450,1450)
#         elif L < 30 and M < 30:
#             PWM.setMotorModel(1500,1500,-1500,-1500)
#         elif R < 30 and M < 30:
#             PWM.setMotorModel(-1500,-1500,1500,1500)
#         elif L < 20 :
#             PWM.setMotorModel(2000,2000,-500,-500)
#             if L < 10 :
#                 PWM.setMotorModel(1500,1500,-1000,-1000)
#         elif R < 20 :
#             PWM.setMotorModel(-500,-500,2000,2000)
#             if R < 10 :
#                 PWM.setMotorModel(-1500,-1500,1500,1500)
#         else :
#             self.PWM.setMotorModel(600,600,600,600)
                
#     def run(self):
#         self.PWM=Motor()
#         #self.pwm_S=Servo()
#         for i in range(30,151,60):
#                 self.pwm_S.setServoPwm('0',i)
#                 time.sleep(0.2)
#                 if i==30:
#                     L = self.get_distance()
#                 elif i==90:
#                     M = self.get_distance()
#                 else:
#                     R = self.get_distance()
#         while True:
#             for i in range(90,30,-60):
#                 self.pwm_S.setServoPwm('0',i)
#                 time.sleep(0.2)
#                 if i==30:
#                     L = self.get_distance()
#                 elif i==90:
#                     M = self.get_distance()
#                 else:
#                     R = self.get_distance()
#                 self.run_motor(L,M,R)
#             for i in range(30,151,60):
#                 self.pwm_S.setServoPwm('0',i)
#                 time.sleep(0.2)
#                 if i==30:
#                     L = self.get_distance()
#                 elif i==90:
#                     M = self.get_distance()
#                 else:
#                     R = self.get_distance()
#                 self.run_motor(L,M,R)
        
            
        
# ultrasonic=Ultrasonic()              
# # Main program logic follows:
# if __name__ == '__main__':
#     print ('Program is starting ... ')
#     try:
#         ultrasonic.run()
#     except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
#         PWM.setMotorModel(0,0,0,0)
#         ultrasonic.pwm_S.setServoPwm('0',90)

