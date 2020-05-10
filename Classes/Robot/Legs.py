# EV3
from ev3dev2.motor import LargeMotor

# Local resources
from Classes.Robot.Ev3Motor import Ev3Motor
import Config

# Python import
import logging as Logging

class Legs(Ev3Motor):
    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort):
        Logging.basicConfig(level = Logging.getLevelName(Config.LOGGING_LEVEL))

        Logging.info('Init legs motor')
        super().__init__(Motor = LargeMotor(address = MotorPort))

    #
    # MoveForward
    # Make the elephant moving forward
    def MoveForward(self, Wait = True):
        Logging.info('Moving forward')
        self.Speed = -800
        self.StopAction = 'brake'
        
        self.RunForever()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # Stop
    # Stop moving
    def Stop(self):
        Logging.info('Stop moving')
        self.MotorOff()