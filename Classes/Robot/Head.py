# EV3
from ev3dev2.motor import MediumMotor
from ev3dev2.sensor.lego import ColorSensor

# Local resources
import Config
from Classes.Robot.Ev3Motor import Ev3Motor

# Python
import logging as Logging
from time import sleep as Sleep

class Head(Ev3Motor):
    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort, SensorPort):
        Logging.basicConfig(level = Logging.getLevelName(Config.LOGGING_LEVEL))

        Logging.info('Init head motor')
        super().__init__(Motor = MediumMotor(address = MotorPort))

        Logging.info('Init color sensor')
        self.__Sensor = ColorSensor(address = SensorPort)
        self.__Sensor.mode = self.__Sensor.MODE_COL_REFLECT

    #
    # InitPosition
    # Move the elephant trunk to the initial position
    def InitPosition(self):
        Logging.info('Moving head to initial position')
        self.Speed = -400
        self.StopAction = 'brake'
        
        self.RunForever()

        # Set position to 0
        self.WaitUntilStalled()
        self.MotorReset()

    #
    # MoveDown
    # Move the elephant head down
    def MoveDown(self, Wait):
        Logging.info('Moving head down')
        self.Position = 0
        self.Speed = 400
        self.StopAction = 'brake'
        
        self.RunToAbsolutePosition()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # MoveUp
    # Move the elephant head up
    def MoveUp(self, Wait):
        Logging.info('Moving head up')

        self.Position = 700
        self.Speed = 400
        self.StopAction = 'brake'
        
        self.RunToAbsolutePosition()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # Stop
    # Stop moving
    def Stop(self):
        Logging.info('Stop moving')
        self.MotorOff()