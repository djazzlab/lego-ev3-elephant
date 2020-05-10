#!/usr/bin/env python3

# EV3 Motors
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_D as OutPortD

# EV3 Sensors
from ev3dev2.sensor import INPUT_1 as InPort1
from ev3dev2.sensor import INPUT_4 as InPort4

# Robot Classes
from Classes.Robot.Head import Head
from Classes.Robot.Legs import Legs
from Classes.Robot.Trunk import Trunk

# Python
from time import sleep as Sleep

class Elephant:
    __ElephantHead = None
    __ElephantLegs = None
    __ElephantTrunk = None

    ##########################
    # Initialization Methods #
    ##########################
    def __init__(self):
        # Configure the elephant head motor
        self.__ElephantHead = Head(MotorPort = OutPortD, SensorPort = InPort4)
        # Move the elephant head down to the initial position
        self.__ElephantHead.InitPosition()

        # Configure the elephant legs motor
        self.__ElephantLegs = Legs(MotorPort = OutPortA)

        # Configure the elephant trunk motor
        self.__ElephantTrunk = Trunk(MotorPort = OutPortB, SensorPort = InPort1)
        # Move the elephant trunk until the touch sensor is pressed
        self.__ElephantTrunk.InitPosition()

    ###################
    # Exposed Methods #
    ###################
    #
    # Run
    # Run a define and coded scenario
    def Run(self):
        # Set the trunk to a "normal" (aka beautiful) position
        self.__ElephantTrunk.PutToNormalPosition()

        # Move forward
        self.__ElephantLegs.MoveForward(Wait = False)

        while self.__ElephantLegs.IsRunning():
            # Make the elephant roaring
            self.__Roar()

            # Sleeping
            Sleep(5)

            # Make the elephant eating
            self.__MoveTrunk(Action = 'Eat')
            self.__ElephantTrunk.PutTrunkDown(Wait = True)

            # Sleeping
            Sleep(5)


    ###################
    # Private Methods #
    ###################
    #
    # MoveHead
    # Move the elephant head down or up depending on the direction
    def __MoveHead(self, Direction, WaitWhileRunning = True):
        if str(Direction).lower().title() == 'Down':
            self.__ElephantHead.MoveDown(Wait = WaitWhileRunning)
        else:
            self.__ElephantHead.MoveUp(Wait = WaitWhileRunning)

    #
    # MoveTrunk
    # Move the elephant trunk to make it eat or make it roar
    def __MoveTrunk(self, Action, WaitWhileRunning = True):
        if str(Action).lower().title() == 'Roar':
            self.__ElephantTrunk.MakeItRoar(Wait = WaitWhileRunning)
        else:
            self.__ElephantLegs.Stop()
            self.__ElephantTrunk.MakeItEat(Wait = WaitWhileRunning)

            # Back moving
            self.__ElephantLegs.MoveForward(Wait = False)

    #
    # Roar
    # Make the elephant roaring
    def __Roar(self):
        # Make it roar
        self.__MoveHead(Direction = 'Up', WaitWhileRunning = False)
        self.__MoveTrunk(Action = 'Roar', WaitWhileRunning = False)

        while self.__ElephantHead.IsRunning():
            Sleep(.01)

        while self.__ElephantTrunk.IsRunning():
            Sleep(.01)

        self.__ElephantHead.Stop()
        self.__ElephantTrunk.Stop()

        # Back to normal position for head and trunk
        self.__MoveHead(Direction = 'Down', WaitWhileRunning = False)
        self.__ElephantTrunk.PutTrunkDown(Wait = False)

        while self.__ElephantHead.IsRunning():
            Sleep(.01)

        while self.__ElephantTrunk.IsRunning():
            Sleep(.01)

        self.__ElephantHead.Stop()
        self.__ElephantTrunk.Stop()

################
# Main Program #
################
Dumbo = Elephant()
Dumbo.Run()