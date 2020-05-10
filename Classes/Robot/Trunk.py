# EV3
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound

# Local resources
import Config
from Classes.Robot.Ev3Motor import Ev3Motor

# Python
import logging as Logging
from time import sleep as Sleep

class Trunk(Ev3Motor):
    __Sensor = None
    __Speaker = None

    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort, SensorPort):
        Logging.basicConfig(level = Logging.getLevelName(Config.LOGGING_LEVEL))

        Logging.info('Init trunk motor')
        super().__init__(Motor = LargeMotor(address = MotorPort))

        Logging.info('Init touch sensor')
        self.__Sensor = TouchSensor(address = SensorPort)
        self.__Sensor.mode = self.__Sensor.MODE_TOUCH

        Logging.info('Init sounds')
        self.__Speaker = Sound()

    #
    # InitPosition
    # Move the elephant trunk to the initial position
    def InitPosition(self):
        Logging.info('Moving trunk to initial position')

        # Move the trunk until the touch sensor is pressed
        self.Speed = -400
        self.StopAction = 'brake'
        
        self.RunForever()

        while not self.__Sensor.is_pressed:
            Sleep(.01)

        # Set position to 0
        self.MotorReset()

    #
    # MakeItRoar
    # Make roaring the elephant
    def MakeItRoar(self, Wait):
        Logging.info('Roaring')

        self.__Speaker.play_file(
            wav_file = 'Sounds/elephant8.wav',
            volume = 100,
            play_type = self.__Speaker.PLAY_NO_WAIT_FOR_COMPLETE
        )
        
        Logging.info('Moving trunk in roar position')

        self.Position = 0
        self.Speed = 400
        self.StopAction = 'brake'
        
        self.RunToAbsolutePosition()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # MakeItEat
    # Make eating the elephant
    def MakeItEat(self, Wait):
        Logging.info('Moving trunk in eat position')

        self.Position = 1400
        self.Speed = 400
        self.StopAction = 'brake'
        
        self.RunToAbsolutePosition()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # PutToNormalPosition
    # Move the trunk to the normal position
    def PutToNormalPosition(self, Wait = True):
        Logging.info('Moving trunk to normal position')

        self.Position = 300
        self.Speed = 400
        self.StopAction = 'brake'
        
        self.RunToAbsolutePosition()

        if Wait:
            self.WaitWhileRunning()
            self.MotorOff()

    #
    # PutTrunkDown
    # Put the elephant trunk down
    def PutTrunkDown(self, Wait):
        Logging.info('Moving trunk down')

        self.Position = 600
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
