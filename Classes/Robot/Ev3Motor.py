class Ev3Motor:
    __Motor = None
    _Position = 0
    _RampDown = 0
    _RampUp = 0
    _Speed = 0
    _StopAction = None

    #
    # Init
    # Initialize the motor
    def __init__(self, Motor):
        self.__Motor = Motor

    ######################
    # Properties Methods #
    ######################
    #
    # Position property
    @property
    def Position(self):
        return self._Position
    
    @Position.setter
    def Position(self, Position):
        if not isinstance(Position, int):
            raise ValueError('Not integer Position is not possible')

        self._Position = Position

    @Position.deleter
    def Position(self):
        del self._Position

    #
    # RampDown property
    @property
    def RampDown(self):
        return self._RampDown
    
    @RampDown.setter
    def RampDown(self, RampDown):
        if not isinstance(RampDown, int):
            raise ValueError('Not integer RampDown is not possible')

        self._RampDown = RampDown

    @RampDown.deleter
    def RampDown(self):
        del self._RampDown

    #
    # RampUp property
    @property
    def RampUp(self):
        return self._RampUp
    
    @RampUp.setter
    def RampUp(self, RampUp):
        if not isinstance(RampUp, int):
            raise ValueError('Not integer RampUp is not possible')

        self._RampUp = RampUp

    @RampUp.deleter
    def RampUp(self):
        del self._RampUp

    #
    # Speed property
    @property
    def Speed(self):
        return self._Speed
    
    @Speed.setter
    def Speed(self, Speed):
        if not isinstance(Speed, int):
            raise ValueError('Not integer Speed is not possible')

        self._Speed = Speed

    @Speed.deleter
    def Speed(self):
        del self._Speed

    #
    # StopAction property
    @property
    def StopAction(self):
        return self._StopAction
    
    @StopAction.setter
    def StopAction(self, StopAction):
        StopActions = [
            self.__Motor.STOP_ACTION_BRAKE,
            self.__Motor.STOP_ACTION_COAST,
            self.__Motor.STOP_ACTION_HOLD
        ]

        if StopAction not in StopActions:
            raise ValueError('StopAction should be one of {}'.format(StopActions))

        self._StopAction = StopAction

    @StopAction.deleter
    def StopAction(self):
        del self._StopAction

    ##################
    # Public Methods #
    ##################

    #
    # GetMotorPosition
    # Returns the current position of the motor
    def GetMotorPosition(self):
        return self.__Motor.position_sp

    #
    # GetMotorRampDown
    # Returns the current ramp down of the motor
    def GetMotorRampDown(self):
        return self.__Motor.ramp_down_sp

    #
    # GetMotorRampUp
    # Returns the current ramp up of the motor
    def GetMotorRampUp(self):
        return self.__Motor.ramp_up_sp

    #
    # GetMotorSpeed
    # Returns the current speed of the motor
    def GetMotorSpeed(self):
        return self.__Motor.speed_sp

    #
    # GetMotorStopAction
    # Returns the current stop action of the motor
    def GetMotorStopAction(self):
        return self.__Motor.stop_action

    #
    # GetState
    # Returns the current states list of the motor
    def GetState(self):
        return self.__Motor.state

    #
    # IsRunning
    # Expose the motor state: true if the motor is in the running state
    def IsRunning(self):
        return True if 'running' in self.GetState() else False

    #
    # MotorOff
    # Stop the motor 
    def MotorOff(self):
        self.__Motor.stop(stop_action = self.StopAction)

    #
    # MotorReset
    # Reset the motor
    def MotorReset(self):
        self.Position = 0
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 0
        self.StopAction = self.__Motor.STOP_ACTION_COAST
        self.__Motor.reset()

    #
    # RunForever
    # Run the motor until another command is sent
    def RunForever(self):
        self.__Motor.run_forever(
            ramp_down_sp = self.RampDown,
            ramp_up_sp = self.RampUp,
            speed_sp = self.Speed,
            stop_action = self.StopAction
        )

    #
    # RunToAbsolutePosition
    # Run to a position relative to the current position value
    def RunToAbsolutePosition(self):
        self.__Motor.run_to_abs_pos(
            position_sp = self.Position,
            ramp_down_sp = self.RampDown,
            ramp_up_sp = self.RampUp,
            speed_sp = self.Speed,
            stop_action = self.StopAction
        )

    #
    # RunToRelativePosition
    # Run to a position relative to the current position value
    def RunToRelativePosition(self):
        self.__Motor.run_to_rel_pos(
            position_sp = self.Position,
            ramp_down_sp = self.RampDown,
            ramp_up_sp = self.RampUp,
            speed_sp = self.Speed,
            stop_action = self.StopAction
        )

    #
    # WaitUntilStalled
    # Blocks until the motor is not turning when it should be
    def WaitUntilStalled(self):
        self.__Motor.wait_until(self.__Motor.STATE_STALLED)

    #
    # WaitWhileRunning
    # Blocks while the motor is running
    def WaitWhileRunning(self):
        self.__Motor.wait_while(self.__Motor.STATE_RUNNING)
