# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision J, 09/24/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
import os
import sys
import platform
import time
import datetime
import math
import collections
from copy import * #for deepcopy
import inspect #To enable 'TellWhichFileWereIn'
import threading
import traceback
###########################################################

###########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###########################################################

###########################################################
if sys.version_info[0] < 3:
    import Queue  # Python 2
else:
    import queue as Queue  # Python 3
###########################################################

###########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
########################################################### "sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

###########################################################
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.RCServo import *
from Phidget22.RCServoVoltage import *
###########################################################

class PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    #######################################################################################################################
    #######################################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 0
        self.EnableInternal_MyPrint_Flag = 0
        self.MainThread_still_running_flag = 0
        self.MostRecentDataDict = dict()

        self.DesiredBoardEnglishName_AcceptableValuesList = ["RCC0004", "RCC1000"]
        self.Voltage_AcceptableValuesList = [5.0, 6.0, 7.4]
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            #########################################################
            #########################################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = self.PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, must pass in 'root'")
                return
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: NumberOfPrintLines = " + str(self.NumberOfPrintLines))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: GUIparametersDict: " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DesiredBoardEnglishName" in setup_dict:
            DesiredBoardEnglishName_TEMP = str(setup_dict["DesiredBoardEnglishName"])

            if DesiredBoardEnglishName_TEMP in self.DesiredBoardEnglishName_AcceptableValuesList:
                self.DesiredBoardEnglishName = DesiredBoardEnglishName_TEMP

                #########################################################
                if self.DesiredBoardEnglishName == "RCC0004":
                    self.NumberOfServos = 8

                elif self.DesiredBoardEnglishName == "RCC1000":
                    self.NumberOfServos = 16

                else:
                    self.NumberOfServos = -1
                #########################################################

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, DesiredBoardEnglishName must be contained in " + str(self.DesiredBoardEnglishName_AcceptableValuesList))
                return
        else:
            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Must input DesiredBoardEnglishName.")
            return
        
        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DesiredBoardEnglishName: " + str(self.DesiredBoardEnglishName))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_PhidgetsServoObjects = list()
        self.ServosList_AttachedAndOpenFlag = [-1.0] * self.NumberOfServos
        self.ServosList_ErrorCallbackFiredFlag = [-1.0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_ListOfOnAttachCallbackFunctionNames = [self.Servo0onAttachCallback, self.Servo1onAttachCallback, self.Servo2onAttachCallback, self.Servo3onAttachCallback, self.Servo4onAttachCallback, self.Servo5onAttachCallback, self.Servo6onAttachCallback, self.Servo7onAttachCallback, self.Servo8onAttachCallback, self.Servo9onAttachCallback, self.Servo10onAttachCallback, self.Servo11onAttachCallback, self.Servo12onAttachCallback, self.Servo13onAttachCallback, self.Servo14onAttachCallback, self.Servo15onAttachCallback]
        self.ServosList_ListOfOnDetachCallbackFunctionNames = [self.Servo0onDetachCallback, self.Servo1onDetachCallback, self.Servo2onDetachCallback, self.Servo3onDetachCallback, self.Servo4onDetachCallback, self.Servo5onDetachCallback, self.Servo6onDetachCallback, self.Servo7onDetachCallback, self.Servo8onDetachCallback, self.Servo9onDetachCallback, self.Servo10onDetachCallback, self.Servo11onDetachCallback, self.Servo12onDetachCallback, self.Servo13onDetachCallback, self.Servo14onDetachCallback, self.Servo15onDetachCallback]
        self.ServosList_ListOfOnErrorCallbackFunctionNames = [self.Servo0onErrorCallback, self.Servo1onErrorCallback, self.Servo2onErrorCallback, self.Servo3onErrorCallback, self.Servo4onErrorCallback, self.Servo5onErrorCallback, self.Servo6onErrorCallback, self.Servo7onErrorCallback, self.Servo8onErrorCallback, self.Servo9onErrorCallback, self.Servo10onErrorCallback, self.Servo11onErrorCallback, self.Servo12onErrorCallback, self.Servo13onErrorCallback, self.Servo14onErrorCallback, self.Servo15onErrorCallback]
        self.ServosList_ListOfOnPositionChangeCallbackFunctionNames = [self.Servo0onPositionChangeCallback, self.Servo1onPositionChangeCallback, self.Servo2onPositionChangeCallback, self.Servo3onPositionChangeCallback, self.Servo4onPositionChangeCallback, self.Servo5onPositionChangeCallback, self.Servo6onPositionChangeCallback, self.Servo7onPositionChangeCallback, self.Servo8onPositionChangeCallback, self.Servo9onPositionChangeCallback, self.Servo10onPositionChangeCallback, self.Servo11onPositionChangeCallback, self.Servo12onPositionChangeCallback, self.Servo13onPositionChangeCallback, self.Servo14onPositionChangeCallback, self.Servo15onPositionChangeCallback]
        self.ServosList_ListOfOnVelocityChangeCallbackFunctionNames = [self.Servo0onVelocityChangeCallback, self.Servo1onVelocityChangeCallback, self.Servo2onVelocityChangeCallback, self.Servo3onVelocityChangeCallback, self.Servo4onVelocityChangeCallback, self.Servo5onVelocityChangeCallback, self.Servo6onVelocityChangeCallback, self.Servo7onVelocityChangeCallback, self.Servo8onVelocityChangeCallback, self.Servo9onVelocityChangeCallback, self.Servo10onVelocityChangeCallback, self.Servo11onVelocityChangeCallback, self.Servo12onVelocityChangeCallback, self.Servo13onVelocityChangeCallback, self.Servo14onVelocityChangeCallback, self.Servo15onVelocityChangeCallback]
        #self.ServosList_ListOfOnTargetPositionReachedCallbackFunctionNames = [self.Servo0onTargetPositionReachedCallback, self.Servo1onTargetPositionReachedCallback, self.Servo2onTargetPositionReachedCallback, self.Servo3onTargetPositionReachedCallback, self.Servo4onTargetPositionReachedCallback, self.Servo5onTargetPositionReachedCallback, self.Servo6onTargetPositionReachedCallback, self.Servo7onTargetPositionReachedCallback, self.Servo8onTargetPositionReachedCallback, self.Servo9onTargetPositionReachedCallback, self.Servo10onTargetPositionReachedCallback, self.Servo11onTargetPositionReachedCallback, self.Servo12onTargetPositionReachedCallback, self.Servo13onTargetPositionReachedCallback, self.Servo14onTargetPositionReachedCallback, self.Servo15onTargetPositionReachedCallback]
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_Position_ActualRxFromBoard = [-11111.0] * self.NumberOfServos
        self.ServosList_Position_NeedsToBeChangedFlag = [1] * self.NumberOfServos
        self.ServosList_Position_ToBeSet = [-11111.0] * self.NumberOfServos

        self.ServosList_Position_Min_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_Position_Max_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_Position_Starting_PhidgetsUnits = [-11111.0] * self.NumberOfServos

        self.ServosList_Position_GUIscale_LabelObject = list()
        self.ServosList_Position_GUIscale_Value = list()
        self.ServosList_Position_GUIscale_ScaleObject = list()
        self.ServosList_Position_GUIscale_NeedsToBeChangedFlag = [0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_Velocity_ActualRxFromBoard = [-11111.0] * self.NumberOfServos
        self.ServosList_Velocity_NeedsToBeChangedFlag = [1] * self.NumberOfServos
        self.ServosList_Velocity_ToBeSet = [-11111.0] * self.NumberOfServos

        self.ServosList_Velocity_Min_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_Velocity_Max_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_Velocity_Starting_PhidgetsUnits = [-11111.0] * self.NumberOfServos

        self.ServosList_Velocity_GUIscale_LabelObject = list()
        self.ServosList_Velocity_GUIscale_Value = list()
        self.ServosList_Velocity_GUIscale_ScaleObject = list()
        self.ServosList_Velocity_GUIscale_NeedsToBeChangedFlag = [0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_EngagedState_ActualRxFromBoard = [-1] * self.NumberOfServos
        self.ServosList_EngagedState_NeedsToBeChangedFlag = [1] * self.NumberOfServos
        self.ServosList_EngagedState_ToBeSet = [-1] * self.NumberOfServos
        self.ServosList_EngagedState_Starting = [-1] * self.NumberOfServos

        self.ServosList_EngagedState_GUIcheckbutton_Value = list()
        self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject = list()
        self.ServosList_EngagedState_GUIcheckbutton_NeedsToBeChangedFlag = [0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_SpeedRampingState_ActualRxFromBoard = [-1] * self.NumberOfServos
        self.ServosList_SpeedRampingState_NeedsToBeChangedFlag = [1] * self.NumberOfServos
        self.ServosList_SpeedRampingState_ToBeSet = [-1] * self.NumberOfServos
        self.ServosList_SpeedRampingState_Starting = [-1] * self.NumberOfServos

        self.ServosList_SpeedRampingState_GUIcheckbutton_Value = list()
        self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject = list()
        self.ServosList_SpeedRampingState_GUIcheckbutton_NeedsToBeChangedFlag = [0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_PulseWidthMin_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_PulseWidthMax_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_Voltage_PhidgetsUnits_UserSet = [-11111.0] * self.NumberOfServos
        self.ServosList_DataIntervalMilliseconds = [-11111.0] * self.NumberOfServos
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DesiredSerialNumber" in setup_dict:
            try:
                self.DesiredSerialNumber = int(setup_dict["DesiredSerialNumber"])
            except:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error: DesiredSerialNumber invalid.")
        else:
            self.DesiredSerialNumber = -1
        
        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DesiredSerialNumber: " + str(self.DesiredSerialNumber))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in setup_dict:
            self.NameToDisplay_UserSet = str(setup_dict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: NameToDisplay_UserSet: " + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WaitForAttached_TimeoutDuration_Milliseconds" in setup_dict:
            self.WaitForAttached_TimeoutDuration_Milliseconds = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("WaitForAttached_TimeoutDuration_Milliseconds", setup_dict["WaitForAttached_TimeoutDuration_Milliseconds"], 0.0, 60000.0))

        else:
            self.WaitForAttached_TimeoutDuration_Milliseconds = 5000

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: WaitForAttached_TimeoutDuration_Milliseconds: " + str(self.WaitForAttached_TimeoutDuration_Milliseconds))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "UsePhidgetsLoggingInternalToThisClassObjectFlag" in setup_dict:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UsePhidgetsLoggingInternalToThisClassObjectFlag", setup_dict["UsePhidgetsLoggingInternalToThisClassObjectFlag"])
        else:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = 1

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: UsePhidgetsLoggingInternalToThisClassObjectFlag: " + str(self.UsePhidgetsLoggingInternalToThisClassObjectFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MainThread_TimeToSleepEachLoop" in setup_dict:
            self.MainThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MainThread_TimeToSleepEachLoop", setup_dict["MainThread_TimeToSleepEachLoop"], 0.001, 100000)

        else:
            self.MainThread_TimeToSleepEachLoop = 0.005

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: MainThread_TimeToSleepEachLoop: " + str(self.MainThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_DataIntervalMilliseconds" in setup_dict:
            ServosList_DataIntervalMilliseconds_TEMP = setup_dict["ServosList_DataIntervalMilliseconds"]

            if self.IsInputListOfNumbers(ServosList_DataIntervalMilliseconds_TEMP) == 1:
                if len(ServosList_DataIntervalMilliseconds_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_DataIntervalMilliseconds_TEMP_ELEMENT in enumerate(ServosList_DataIntervalMilliseconds_TEMP):
                        self.ServosList_DataIntervalMilliseconds[ServoChannel] = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_DataIntervalMilliseconds, ServoChannel " + str(ServoChannel), ServosList_DataIntervalMilliseconds_TEMP_ELEMENT, 32.0, 60000.0))

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_DataIntervalMilliseconds must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_DataIntervalMilliseconds must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_DataIntervalMilliseconds = [32]*self.NumberOfServos #32ms, fastest update rate possible

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_DataIntervalMilliseconds: " + str(self.ServosList_DataIntervalMilliseconds))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_EngagedState_Starting" in setup_dict:
            ServosList_EngagedState_Starting_TEMP = setup_dict["ServosList_EngagedState_Starting"]

            if self.IsInputListOfNumbers(ServosList_EngagedState_Starting_TEMP) == 1:
                if len(ServosList_EngagedState_Starting_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_EngagedState_Starting_TEMP_ELEMENT in enumerate(ServosList_EngagedState_Starting_TEMP):
                        self.ServosList_EngagedState_Starting[ServoChannel] = int(self.PassThrough0and1values_ExitProgramOtherwise("ServosList_EngagedState_Starting, ServoChannel " + str(ServoChannel), ServosList_EngagedState_Starting_TEMP_ELEMENT))

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_EngagedState_Starting must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_EngagedState_Starting must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_EngagedState_Starting = [0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_EngagedState_Starting: " + str(self.ServosList_EngagedState_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_EngagedState_ToBeSet = list(self.ServosList_EngagedState_Starting)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_SpeedRampingState_Starting" in setup_dict:
            ServosList_SpeedRampingState_Starting_TEMP = setup_dict["ServosList_SpeedRampingState_Starting"]

            if self.IsInputListOfNumbers(ServosList_SpeedRampingState_Starting_TEMP) == 1:
                if len(ServosList_SpeedRampingState_Starting_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_SpeedRampingState_Starting_TEMP_ELEMENT in enumerate(ServosList_SpeedRampingState_Starting_TEMP):
                        self.ServosList_SpeedRampingState_Starting[ServoChannel] = int(self.PassThrough0and1values_ExitProgramOtherwise("ServosList_SpeedRampingState_Starting, ServoChannel " + str(ServoChannel), ServosList_SpeedRampingState_Starting_TEMP_ELEMENT))

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_SpeedRampingState_Starting must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_SpeedRampingState_Starting must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_SpeedRampingState_Starting = [0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_SpeedRampingState_Starting: " + str(self.ServosList_SpeedRampingState_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_SpeedRampingState_ToBeSet = list(self.ServosList_SpeedRampingState_Starting)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Position_Min_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_Position_Min_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_Position_Min_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_Position_Min_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_Position_Min_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Position_Min_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Position_Min_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Position_Min_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_Position_Min_PhidgetsUnits_TEMP_ELEMENT, -1000000.0, 1000000.0)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Min_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Min_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Position_Min_PhidgetsUnits_UserSet = [0.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Position_Min_PhidgetsUnits_UserSet: " + str(self.ServosList_Position_Min_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Position_Max_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_Position_Max_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_Position_Max_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_Position_Max_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_Position_Max_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Position_Max_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Position_Max_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Position_Max_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_Position_Max_PhidgetsUnits_TEMP_ELEMENT, -1000000.0, 1000000.0)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Max_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Max_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Position_Max_PhidgetsUnits_UserSet = [180.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Position_Max_PhidgetsUnits_UserSet: " + str(self.ServosList_Position_Max_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        for ServoChannel in range(0, self.NumberOfServos):
            if self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel] <= self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel]:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, Position_Max is smaller than or equal to Position_Min for ServoChannel " + str(ServoChannel))
                return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Position_Starting_PhidgetsUnits" in setup_dict:
            ServosList_Position_Starting_PhidgetsUnits_TEMP = setup_dict["ServosList_Position_Starting_PhidgetsUnits"]

            if self.IsInputListOfNumbers(ServosList_Position_Starting_PhidgetsUnits_TEMP) == 1:
                if len(ServosList_Position_Starting_PhidgetsUnits_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Position_Starting_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Position_Starting_PhidgetsUnits_TEMP):
                        self.ServosList_Position_Starting_PhidgetsUnits[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Position_Starting_PhidgetsUnits, ServoChannel " + str(ServoChannel), ServosList_Position_Starting_PhidgetsUnits_TEMP_ELEMENT, self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel], self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel])

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Starting_PhidgetsUnits must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Position_Starting_PhidgetsUnits must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Position_Starting_PhidgetsUnits = list(self.ServosList_Position_Min_PhidgetsUnits_UserSet)

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Position_Starting_PhidgetsUnits: " + str(self.ServosList_Position_Starting_PhidgetsUnits))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_Position_ToBeSet = list(self.ServosList_Position_Starting_PhidgetsUnits)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Velocity_Min_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_Velocity_Min_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_Velocity_Min_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_Velocity_Min_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_Velocity_Min_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Velocity_Min_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Velocity_Min_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Velocity_Min_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_Velocity_Min_PhidgetsUnits_TEMP_ELEMENT, 0.0, 6467.368)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Min_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Min_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Velocity_Min_PhidgetsUnits_UserSet = [0.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Velocity_Min_PhidgetsUnits_UserSet: " + str(self.ServosList_Velocity_Min_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Velocity_Max_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_Velocity_Max_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_Velocity_Max_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_Velocity_Max_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_Velocity_Max_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Velocity_Max_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Velocity_Max_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Velocity_Max_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_Velocity_Max_PhidgetsUnits_TEMP_ELEMENT, 0.0, 6467.368)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Max_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Max_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Velocity_Max_PhidgetsUnits_UserSet = [6467.368]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Velocity_Max_PhidgetsUnits_UserSet: " + str(self.ServosList_Velocity_Max_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        for ServoChannel in range(0, self.NumberOfServos):
            if self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel] <= self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel]:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, Velocity_Max is smaller than or equal to Velocity_Min for ServoChannel " + str(ServoChannel))
                return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Velocity_Starting_PhidgetsUnits" in setup_dict:
            ServosList_Velocity_Starting_PhidgetsUnits_TEMP = setup_dict["ServosList_Velocity_Starting_PhidgetsUnits"]

            if self.IsInputListOfNumbers(ServosList_Velocity_Starting_PhidgetsUnits_TEMP) == 1:
                if len(ServosList_Velocity_Starting_PhidgetsUnits_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Velocity_Starting_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Velocity_Starting_PhidgetsUnits_TEMP):
                        self.ServosList_Velocity_Starting_PhidgetsUnits[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Velocity_Starting_PhidgetsUnits, ServoChannel " + str(ServoChannel), ServosList_Velocity_Starting_PhidgetsUnits_TEMP_ELEMENT, self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel], self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel])

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Starting_PhidgetsUnits must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Velocity_Starting_PhidgetsUnits must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_Velocity_Starting_PhidgetsUnits = [180.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Velocity_Starting_PhidgetsUnits: " + str(self.ServosList_Velocity_Starting_PhidgetsUnits))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ServosList_Velocity_ToBeSet = list(self.ServosList_Velocity_Starting_PhidgetsUnits)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_PulseWidthMin_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_PulseWidthMin_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_PulseWidthMin_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_PulseWidthMin_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_PulseWidthMin_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_PulseWidthMin_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_PulseWidthMin_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_PulseWidthMin_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_PulseWidthMin_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_PulseWidthMin_PhidgetsUnits_TEMP_ELEMENT, 0.083, 2730.666)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_PulseWidthMin_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_PulseWidthMin_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_PulseWidthMin_PhidgetsUnits_UserSet = [0.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_PulseWidthMin_PhidgetsUnits_UserSet: " + str(self.ServosList_PulseWidthMin_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_PulseWidthMax_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_PulseWidthMax_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_PulseWidthMax_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_PulseWidthMax_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_PulseWidthMax_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_PulseWidthMax_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_PulseWidthMax_PhidgetsUnits_UserSet_TEMP):
                        self.ServosList_PulseWidthMax_PhidgetsUnits_UserSet[ServoChannel] = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_PulseWidthMax_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_PulseWidthMax_PhidgetsUnits_TEMP_ELEMENT, 0.083, 2730.666)

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_PulseWidthMax_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_PulseWidthMax_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " numbers.")
                return

        else:
            self.ServosList_PulseWidthMax_PhidgetsUnits_UserSet = [0.0]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_PulseWidthMax_PhidgetsUnits_UserSet: " + str(self.ServosList_PulseWidthMax_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ServosList_Voltage_PhidgetsUnits_UserSet" in setup_dict:
            ServosList_Voltage_PhidgetsUnits_UserSet_TEMP = setup_dict["ServosList_Voltage_PhidgetsUnits_UserSet"]

            if self.IsInputListOfNumbers(ServosList_Voltage_PhidgetsUnits_UserSet_TEMP) == 1:
                if len(ServosList_Voltage_PhidgetsUnits_UserSet_TEMP) == self.NumberOfServos:

                    for ServoChannel, ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT in enumerate(ServosList_Voltage_PhidgetsUnits_UserSet_TEMP):
                        ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("ServosList_Voltage_PhidgetsUnits_UserSet, ServoChannel " + str(ServoChannel), ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT, 5.0, 7.4)

                        if ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT != ServosList_Voltage_PhidgetsUnits_UserSet_TEMP[0]:
                            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Voltage_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " IDENTICAL numbers.")
                            return

                        if ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT in self.Voltage_AcceptableValuesList:

                            #########################################################
                            if ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT == 5.0:
                                self.ServosList_Voltage_PhidgetsUnits_UserSet[ServoChannel] = RCServoVoltage.RCSERVO_VOLTAGE_5V

                            elif ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT == 6.0:
                                self.ServosList_Voltage_PhidgetsUnits_UserSet[ServoChannel] = RCServoVoltage.RCSERVO_VOLTAGE_6V

                            elif ServosList_Voltage_PhidgetsUnits_TEMP_ELEMENT == 7.4:
                                self.ServosList_Voltage_PhidgetsUnits_UserSet[ServoChannel] = RCServoVoltage.RCSERVO_VOLTAGE_7_4V

                            else:
                                self.ServosList_Voltage_PhidgetsUnits_UserSet[ServoChannel] = RCServoVoltage.RCSERVO_VOLTAGE_5V
                            #########################################################

                        else:
                            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Voltage_PhidgetsUnits_UserSet can only contain values in the set " + str(self.Voltage_AcceptableValuesList))
                            return

                else:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Voltage_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " IDENTICAL numbers.")
                    return

            else:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Error, ServosList_Voltage_PhidgetsUnits_UserSet must be a list of " + str(self.NumberOfServos) + " IDENTICAL numbers.")
                return

        else:
            self.ServosList_Voltage_PhidgetsUnits_UserSet = [Phidget.RCSERVO_VOLTAGE_5V]*self.NumberOfServos

        print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: ServosList_Voltage_PhidgetsUnits_UserSet: " + str(self.ServosList_Voltage_PhidgetsUnits_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PrintToGui_Label_TextInputHistory_List = [" "]*self.NumberOfPrintLines
        self.PrintToGui_Label_TextInput_Str = ""
        self.GUI_ready_to_be_updated_flag = 0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.CurrentTime_CalculatedFromMainThread = -11111.0
        self.LastTime_CalculatedFromMainThread = -11111.0
        self.StartingTime_CalculatedFromMainThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromMainThread = -11111.0
        self.DataStreamingDeltaT_CalculatedFromMainThread = -11111.0

        self.DetectedDeviceName = "default"
        self.DetectedDeviceID = "default"
        self.DetectedDeviceVersion = "default"
        self.DetectedDeviceSerialNumber = "default"
        self.DetectedBoardEnglishName = "default"
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:

            #########################################################
            for ServoChannel in range(0, self.NumberOfServos):
                self.ServosList_PhidgetsServoObjects.append(RCServo())

                if self.DesiredSerialNumber != -1:
                    self.ServosList_PhidgetsServoObjects[ServoChannel].setDeviceSerialNumber(self.DesiredSerialNumber)

                self.ServosList_PhidgetsServoObjects[ServoChannel].setChannel(ServoChannel)
                self.ServosList_PhidgetsServoObjects[ServoChannel].setOnAttachHandler(self.ServosList_ListOfOnAttachCallbackFunctionNames[ServoChannel])
                self.ServosList_PhidgetsServoObjects[ServoChannel].setOnDetachHandler(self.ServosList_ListOfOnDetachCallbackFunctionNames[ServoChannel])
                self.ServosList_PhidgetsServoObjects[ServoChannel].setOnErrorHandler(self.ServosList_ListOfOnErrorCallbackFunctionNames[ServoChannel])
                self.ServosList_PhidgetsServoObjects[ServoChannel].setOnPositionChangeHandler(self.ServosList_ListOfOnPositionChangeCallbackFunctionNames[ServoChannel])
                self.ServosList_PhidgetsServoObjects[ServoChannel].setOnVelocityChangeHandler(self.ServosList_ListOfOnVelocityChangeCallbackFunctionNames[ServoChannel])
                self.ServosList_PhidgetsServoObjects[ServoChannel].openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            #########################################################

            self.PhidgetsDeviceConnectedFlag = 1

        except PhidgetException as e:
            self.PhidgetsDeviceConnectedFlag = 0
            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__Failed to attach, Phidget Exception %i: %s" % (e.code, e.details))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.PhidgetsDeviceConnectedFlag == 1:

            #########################################################
            if self.UsePhidgetsLoggingInternalToThisClassObjectFlag == 1:
                try:
                    Log.enable(LogLevel.PHIDGET_LOG_INFO, os.getcwd() + "\PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class_PhidgetLog_INFO.txt")
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Enabled Phidget Logging.")
                except PhidgetException as e:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to enable Phidget Logging, Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceName = self.ServosList_PhidgetsServoObjects[0].getDeviceName()
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DetectedDeviceName: " + self.DetectedDeviceName)

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to call 'getDeviceName', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceSerialNumber = self.ServosList_PhidgetsServoObjects[0].getDeviceSerialNumber()
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DetectedDeviceSerialNumber: " + str(self.DetectedDeviceSerialNumber))

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to call 'getDeviceSerialNumber', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceID = self.ServosList_PhidgetsServoObjects[0].getDeviceID()
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DetectedDeviceID: " + str(self.DetectedDeviceID))

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to call 'getDeviceID', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceVersion = self.ServosList_PhidgetsServoObjects[0].getDeviceVersion()
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DetectedDeviceVersion: " + str(self.DetectedDeviceVersion))

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to call 'getDeviceVersion', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            ######################################################### DetectedDeviceVersion differentiates but isn't long-term, reliable method.
            if str(self.DetectedDeviceVersion)[0] == "1":
                self.DetectedBoardEnglishName = "RCC1000"

            elif str(self.DetectedDeviceVersion)[0]  == "4":
                self.DetectedBoardEnglishName = "RCC0004"

            else:
                self.DetectedBoardEnglishName = "default"

            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: self.DetectedBoardEnglishName: " + str(self.DetectedBoardEnglishName))

            if self.DetectedBoardEnglishName != self.DesiredBoardEnglishName:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: self.DetectedBoardEnglishName: " + str(self.DetectedBoardEnglishName) + " does not match self.DesiredBoardEnglishName: " + str(self.DesiredBoardEnglishName))
                return
            #########################################################

            #########################################################
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceLibraryVersion = self.ServosList_PhidgetsServoObjects[0].getLibraryVersion()
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: DetectedDeviceLibraryVersion: " + str(self.DetectedDeviceLibraryVersion))

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Failed to call 'getLibraryVersion', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            if self.DesiredSerialNumber != -1: #'-1' means we should open the device regardless os serial number.
                if self.DetectedDeviceSerialNumber != self.DesiredSerialNumber:
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: The desired Serial Number (" + str(self.DesiredSerialNumber) + ") does not match the detected serial number (" + str(self.DetectedDeviceSerialNumber) + ").")
                    input("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class __init__: Press any key (and enter) to exit.")
                    sys.exit()
            #########################################################

            #########################################################
            self.MainThread_ThreadingObject = threading.Thread(target=self.MainThread, args=())
            self.MainThread_ThreadingObject.start()
            #########################################################

            #########################################################
            if self.USE_GUI_FLAG == 1:
                self.StartGUI(self.root)
            #########################################################

            #########################################################
            time.sleep(0.25)
            #########################################################

            #########################################################
            self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
            #########################################################

        #########################################################
        #########################################################

    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    def __del__(self):
        pass
    #######################################################################################################################
    #######################################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be 0 or 1 (value was " +
                          str(InputNumber_ConvertedToFloat) +
                          "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be in the range [" +
                          str(RangeMinValue) +
                          ", " +
                          str(RangeMaxValue) +
                          "] (value was " +
                          str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServoGENERALonAttachCallback(self, ServoChannel):

        try:
            if self.DetectedBoardEnglishName == "RCC0004":
                self.ServosList_PhidgetsServoObjects[ServoChannel].setDataInterval(self.ServosList_DataIntervalMilliseconds[ServoChannel])
                #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getDataInterval() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getDataInterval()))

            self.ServosList_PhidgetsServoObjects[ServoChannel].setMinPosition(self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel])
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getMinPosition() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getMinPosition()))

            self.ServosList_PhidgetsServoObjects[ServoChannel].setMaxPosition(self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel])
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getMaxPosition() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getMaxPosition()))

            self.ServosList_PhidgetsServoObjects[ServoChannel].setMinPulseWidth(self.ServosList_PulseWidthMin_PhidgetsUnits_UserSet[ServoChannel])
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getMinPulseWidth() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getMinPulseWidth()))

            self.ServosList_PhidgetsServoObjects[ServoChannel].setMaxPulseWidth(self.ServosList_PulseWidthMax_PhidgetsUnits_UserSet[ServoChannel])
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getMaxPulseWidth() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getMaxPulseWidth()))

            self.ServosList_PhidgetsServoObjects[ServoChannel].setVoltage(self.ServosList_Voltage_PhidgetsUnits_UserSet[ServoChannel])
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel, getVoltage() for " + str(ServoChannel) + ", returning: " + str(self.ServosList_PhidgetsServoObjects[ServoChannel].getVoltage()))

            self.ServosList_AttachedAndOpenFlag[ServoChannel] = 1
            #self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonAttachCallback event for ServoChannel " + str(ServoChannel) + ", Attached! $$$$$$$$$$")

        except PhidgetException as e:
            self.ServosList_AttachedAndOpenFlag[ServoChannel] = 0
            self.MyPrint_WithoutLogFile("ServoGENERALonAttachCallback event for ServoChannel " + str(ServoChannel) + ", Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServoGENERALonDetachCallback(self, ServoChannel):

        self.ServosList_AttachedAndOpenFlag[ServoChannel] = 0
        self.MyPrint_WithoutLogFile("$$$$$$$$$$ ServoGENERALonDetachCallback event for ServoChannel " + str(ServoChannel) + ", Detatched! $$$$$$$$$$")

        try:
            self.ServosList_PhidgetsServoObjects[ServoChannel].openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            time.sleep(0.250)

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("ServoGENERALonDetachCallback event for ServoChannel " + str(ServoChannel) + ", Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServoGENERALonErrorCallback(self, ServoChannel, code, description):

        self.ServosList_ErrorCallbackFiredFlag[ServoChannel] = 1

        self.MyPrint_WithoutLogFile("ServoGENERALonErrorCallback event for ServoChannell " + str(ServoChannel) + ", Error Code " + ErrorEventCode.getName(code) + ", description: " + str(description))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServoGENERALonPositionChangeCallback(self, ServoChannel, UpdatedPositionFromBoard):

        try:
            self.ServosList_Position_ActualRxFromBoard[ServoChannel] = UpdatedPositionFromBoard

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("ServoGENERALonPositionChangeCallback event for ServoChannel " + str(ServoChannel) + ", Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServoGENERALonVelocityChangeCallback(self, ServoChannel, UpdatedVelocityFromBoard):

        try:
            self.ServosList_Velocity_ActualRxFromBoard[ServoChannel] = UpdatedVelocityFromBoard

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("ServoGENERALonVelocityChangeCallback event for ServoChannel " + str(ServoChannel) + ", Phidget Exception %i: %s" % (e.code, e.details))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo0onAttachCallback(self, HandlerSelf):

        ServoChannel = 0
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo0onDetachCallback(self, HandlerSelf):

        ServoChannel = 0
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo0onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 0
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo0onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 0
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo0onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 0
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo1onAttachCallback(self, HandlerSelf):

        ServoChannel = 1
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo1onDetachCallback(self, HandlerSelf):

        ServoChannel = 1
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo1onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 1
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo1onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 1
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo1onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 1
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo2onAttachCallback(self, HandlerSelf):

        ServoChannel = 2
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo2onDetachCallback(self, HandlerSelf):

        ServoChannel = 2
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo2onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 2
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo2onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 2
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo2onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 2
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo3onAttachCallback(self, HandlerSelf):

        ServoChannel = 3
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo3onDetachCallback(self, HandlerSelf):

        ServoChannel = 3
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo3onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 3
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo3onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 3
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo3onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 3
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo4onAttachCallback(self, HandlerSelf):

        ServoChannel = 4
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo4onDetachCallback(self, HandlerSelf):

        ServoChannel = 4
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo4onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 4
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo4onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 4
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo4onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 4
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo5onAttachCallback(self, HandlerSelf):

        ServoChannel = 5
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo5onDetachCallback(self, HandlerSelf):

        ServoChannel = 5
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo5onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 5
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo5onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 5
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo5onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 5
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo6onAttachCallback(self, HandlerSelf):

        ServoChannel = 6
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo6onDetachCallback(self, HandlerSelf):

        ServoChannel = 6
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo6onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 6
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo6onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 6
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo6onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 6
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo7onAttachCallback(self, HandlerSelf):

        ServoChannel = 7
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo7onDetachCallback(self, HandlerSelf):

        ServoChannel = 7
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo7onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 7
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo7onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 7
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo7onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 7
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo8onAttachCallback(self, HandlerSelf):

        ServoChannel = 8
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo8onDetachCallback(self, HandlerSelf):

        ServoChannel = 8
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo8onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 8
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo8onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 8
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo8onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 8
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo9onAttachCallback(self, HandlerSelf):

        ServoChannel = 9
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo9onDetachCallback(self, HandlerSelf):

        ServoChannel = 9
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo9onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 9
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo9onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 9
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo9onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 9
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo10onAttachCallback(self, HandlerSelf):

        ServoChannel = 10
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo10onDetachCallback(self, HandlerSelf):

        ServoChannel = 10
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo10onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 10
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo10onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 10
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo10onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 10
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo11onAttachCallback(self, HandlerSelf):

        ServoChannel = 11
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo11onDetachCallback(self, HandlerSelf):

        ServoChannel = 11
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo11onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 11
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo11onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 11
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo11onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 11
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo12onAttachCallback(self, HandlerSelf):

        ServoChannel = 12
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo12onDetachCallback(self, HandlerSelf):

        ServoChannel = 12
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo12onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 12
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo12onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 12
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo12onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 12
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo13onAttachCallback(self, HandlerSelf):

        ServoChannel = 13
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo13onDetachCallback(self, HandlerSelf):

        ServoChannel = 13
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo13onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 13
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo13onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 13
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo13onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 13
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo14onAttachCallback(self, HandlerSelf):

        ServoChannel = 14
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo14onDetachCallback(self, HandlerSelf):

        ServoChannel = 14
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo14onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 14
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo14onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 14
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo14onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 14
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo15onAttachCallback(self, HandlerSelf):

        ServoChannel = 15
        self.ServoGENERALonAttachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo15onDetachCallback(self, HandlerSelf):

        ServoChannel = 15
        self.ServoGENERALonDetachCallback(ServoChannel)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Servo15onErrorCallback(self, HandlerSelf, code, description):

        ServoChannel = 15
        self.ServoGENERALonErrorCallback(ServoChannel, code, description)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo15onPositionChangeCallback(self, HandlerSelf, UpdatedPositionFromBoard):

        ServoChannel = 15
        self.ServoGENERALonPositionChangeCallback(ServoChannel, UpdatedPositionFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def Servo15onVelocityChangeCallback(self, HandlerSelf, UpdatedVelocityFromBoard):

        ServoChannel = 15
        self.ServoGENERALonVelocityChangeCallback(ServoChannel, UpdatedVelocityFromBoard)

    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):

        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = float(test_val)

        return test_val

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ########################################################################################################## unicorn
    def SetPosition(self, ServoChannel, Position_ToBeSet):

        if ServoChannel in range(0, self.NumberOfServos):
            Position_ToBeSet_LIMITED = self.LimitNumber_FloatOutputOnly(self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel], self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel], Position_ToBeSet)

            self.ServosList_Position_ToBeSet[ServoChannel] = Position_ToBeSet_LIMITED
            self.ServosList_Position_NeedsToBeChangedFlag[ServoChannel] = 1
            self.ServosList_Position_GUIscale_NeedsToBeChangedFlag[ServoChannel] = 1

        else:
            print("SetPosition ERROR, ServoChannel must be in " + str(list(range(0, self.NumberOfServos))) + ".")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ########################################################################################################## unicorn
    def SetVelocity(self, ServoChannel, Velocity_ToBeSet):

        if ServoChannel in range(0, self.NumberOfServos):
            Velocity_ToBeSet_LIMITED = self.LimitNumber_FloatOutputOnly(self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel], self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel], Velocity_ToBeSet)

            self.ServosList_Velocity_ToBeSet[ServoChannel] = Velocity_ToBeSet_LIMITED
            self.ServosList_Velocity_NeedsToBeChangedFlag[ServoChannel] = 1
            self.ServosList_Velocity_GUIscale_NeedsToBeChangedFlag[ServoChannel] = 1

        else:
            print("SetVelocity ERROR, ServoChannel must be in " + str(list(range(0, self.NumberOfServos))) + ".")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetEnagagedState(self, ServoChannel, EngagedState_ToBeSet):

        if ServoChannel in range(0, self.NumberOfServos):
            if EngagedState_ToBeSet in [0, 1]:
                self.ServosList_EngagedState_ToBeSet[ServoChannel] = int(EngagedState_ToBeSet)
                self.ServosList_EngagedState_NeedsToBeChangedFlag[ServoChannel] = 1
                self.ServosList_EngagedState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] = 1
            else:
                print("SetEnagagedState ERROR, EngagedState_ToBeSet must be 0 or 1.")
        else:
            print("SetEnagagedState ERROR, ServoChannel must be in " + str(list(range(0, self.NumberOfServos))) + ".")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetSpeedRampingState(self, ServoChannel, SpeedRampingState_ToBeSet):

        if ServoChannel in range(0, self.NumberOfServos):
            if SpeedRampingState_ToBeSet in [0, 1]:
                self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] = int(SpeedRampingState_ToBeSet)
                self.ServosList_SpeedRampingState_NeedsToBeChangedFlag[ServoChannel] = 1
                self.ServosList_SpeedRampingState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] = 1
            else:
                print("SetSpeedRampingState ERROR, SpeedRampingState_ToBeSet must be 0 or 1.")
        else:
            print("SetSpeedRampingState ERROR, ServoChannel must be in " + str(list(range(0, self.NumberOfServos))) + ".")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:
            self.MostRecentDataDict = dict([("ServosList_ErrorCallbackFiredFlag", self.ServosList_ErrorCallbackFiredFlag),
                                            ("Time", self.CurrentTime_CalculatedFromMainThread)])
    
            return deepcopy(self.MostRecentDataDict) #deepcopy IS required as MostRecentDataDict contains lists.
        
        else:
            return dict() #So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_MainThread(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread - self.LastTime_CalculatedFromMainThread

            if self.DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
                self.DataStreamingFrequency_CalculatedFromMainThread = 1.0/self.DataStreamingDeltaT_CalculatedFromMainThread

            self.LastTime_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_MainThread ERROR with Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## unicorn
    def MainThread(self):

        self.MyPrint_WithoutLogFile("Started MainThread for PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class object.")
        
        self.MainThread_still_running_flag = 1

        self.StartingTime_CalculatedFromMainThread = self.getPreciseSecondsTimeStampString()

        ##########################################################################################################
        ##########################################################################################################
        while self.EXIT_PROGRAM_FLAG == 0:

            ##########################################################################################################
            self.CurrentTime_CalculatedFromMainThread = self.getPreciseSecondsTimeStampString() - self.StartingTime_CalculatedFromMainThread
            ##########################################################################################################

            ##########################################################################################################
            try:
                for ServoChannel in range(0, self.NumberOfServos):

                    ############################################### SpeedRampingState
                    if self.ServosList_SpeedRampingState_NeedsToBeChangedFlag[ServoChannel] == 1:
                        self.ServosList_PhidgetsServoObjects[ServoChannel].setSpeedRampingState(self.ServosList_SpeedRampingState_ToBeSet[ServoChannel])
                        #print("Issuing 'setSpeedRampingState' of " + str(self.ServosList_SpeedRampingState_ToBeSet[ServoChannel]) + " on channel " + str(ServoChannel))
                        self.ServosList_SpeedRampingState_NeedsToBeChangedFlag[ServoChannel] = 0
                    ###############################################

                    ############################################### Position
                    if self.ServosList_Position_NeedsToBeChangedFlag[ServoChannel] == 1:
                        self.ServosList_PhidgetsServoObjects[ServoChannel].setTargetPosition(self.ServosList_Position_ToBeSet[ServoChannel])
                        #print("Issuing 'setTargetPosition' of " + str(self.ServosList_Position_ToBeSet[ServoChannel]) + " on channel " + str(ServoChannel))
                        self.ServosList_Position_NeedsToBeChangedFlag[ServoChannel] = 0
                    ###############################################

                    ############################################### Velocity
                    if self.ServosList_Velocity_NeedsToBeChangedFlag[ServoChannel] == 1:
                        self.ServosList_PhidgetsServoObjects[ServoChannel].setVelocityLimit(self.ServosList_Velocity_ToBeSet[ServoChannel])
                        #print("Issuing 'setVelocityLimit' of " + str(self.ServosList_Velocity_ToBeSet[ServoChannel]) + " on channel " + str(ServoChannel))
                        self.ServosList_Velocity_NeedsToBeChangedFlag[ServoChannel] = 0
                    ###############################################

                    ############################################### EngagedState "Phidget Exception 57: Target position must be set before engaging the servo."
                    if self.ServosList_EngagedState_NeedsToBeChangedFlag[ServoChannel] == 1:
                        self.ServosList_PhidgetsServoObjects[ServoChannel].setEngaged(self.ServosList_EngagedState_ToBeSet[ServoChannel])
                        #print("Issuing 'setEngagedState' of " + str(self.ServosList_EngagedState_ToBeSet[ServoChannel]) + " on channel " + str(ServoChannel))
                        self.ServosList_EngagedState_NeedsToBeChangedFlag[ServoChannel] = 0
                    ###############################################

            except PhidgetException as e:
                print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class MainThread, Phidget Exception %i: %s" % (e.code, e.details))
            ##########################################################################################################

            ########################################################################################################## USE THE TIME.SLEEP() TO SET THE LOOP FREQUENCY
            self.UpdateFrequencyCalculation_MainThread()

            if self.MainThread_TimeToSleepEachLoop > 0.0:
                time.sleep(self.MainThread_TimeToSleepEachLoop)
            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        for ServoChannel in range(0, self.NumberOfServos):
            self.ServosList_PhidgetsServoObjects[ServoChannel].close()
        ##########################################################################################################
        ##########################################################################################################

        self.MyPrint_WithoutLogFile("Finished MainThread for PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class object.")
        self.MainThread_still_running_flag = 0
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StartGUI(self, GuiParent):

        self.GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
        self.GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        self.GUI_Thread_ThreadingObject.start()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_Thread(self, parent):

        print("Starting the GUI_Thread for PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class object.")

        ###################################################
        self.root = parent
        self.parent = parent
        ###################################################

        ###################################################
        self.myFrame = Frame(self.root)

        if self.UseBorderAroundThisGuiObjectFlag == 1:
            self.myFrame["borderwidth"] = 2
            self.myFrame["relief"] = "ridge"

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN)
        ###################################################

        ###################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        ###################################################

        #################################################
        self.DeviceInfo_Label = Label(self.myFrame, text="Device Info", width=125)

        self.DeviceInfo_Label["text"] = self.NameToDisplay_UserSet + \
                                         "\nDevice Name: " + self.DetectedDeviceName + \
                                         "\nDevice Serial Number: " + str(self.DetectedDeviceSerialNumber) + \
                                         "\nDevice Version: " + str(self.DetectedDeviceVersion) + \
                                         "\nDevice BoardEnglishName: " + str(self.DetectedBoardEnglishName)

        self.DeviceInfo_Label.grid(row=0, column=0, padx=10, pady=10, columnspan=1, rowspan=1)
        #################################################

        #################################################
        self.Data_Label = Label(self.myFrame, text="Device Info", width=125)
        self.Data_Label["text"] = "Data_Label"
        self.Data_Label.grid(row=1, column=0, padx=10, pady=10, columnspan=1, rowspan=1)
        #################################################

        ###################################################
        self.ServoControlsFrame = Frame(self.myFrame)
        self.ServoControlsFrame.grid(row = 2, column = 0, padx = 10, pady = 10, rowspan = 1, columnspan= 1)
        ###################################################

        ###################################################
        self.TkinterScaleWidth = 5
        self.TkinterScaleLength = 200
        self.PosVelAccelGuiLabelWidth = 6
        ###################################################

        ##################################################################################################
        ##################################################################################################
        for ServoChannel in range(0, self.NumberOfServos):

            ###########################################################
            self.ServosList_Position_GUIscale_LabelObject.append(Label(self.ServoControlsFrame, text="PosM" + str(ServoChannel), width=self.PosVelAccelGuiLabelWidth))
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1:  # There is a servo physically connected,
                self.ServosList_Position_GUIscale_LabelObject[ServoChannel].grid(row=0+ServoChannel, column=0, padx=1, pady=1, columnspan=1, rowspan=1)

            self.ServosList_Position_GUIscale_Value.append(DoubleVar())
            self.ServosList_Position_GUIscale_ScaleObject.append(Scale(self.ServoControlsFrame, \
                                            #label="Position Deg for Motor : " + str(ServoChannel), \
                                            from_=self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel],\
                                            to=self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel],\
                                            #tickinterval=(self.ServosList_Position_Max_PhidgetsUnits_UserSet[ServoChannel] - self.ServosList_Position_Min_PhidgetsUnits_UserSet[ServoChannel]) / 2.0,\
                                            orient=HORIZONTAL,\
                                            borderwidth=2,\
                                            showvalue=True,\
                                            width=self.TkinterScaleWidth,\
                                            length=self.TkinterScaleLength,\
                                            resolution=1,\
                                            variable=self.ServosList_Position_GUIscale_Value[ServoChannel]))
            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].bind('<Button-1>', lambda event, name=ServoChannel: self.ServosList_Position_GUIscale_EventResponse(event, name))
            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].bind('<B1-Motion>', lambda event, name=ServoChannel: self.ServosList_Position_GUIscale_EventResponse(event, name))
            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].bind('<ButtonRelease-1>', lambda event, name=ServoChannel: self.ServosList_Position_GUIscale_EventResponse(event, name))
            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].set(self.ServosList_Position_Starting_PhidgetsUnits[ServoChannel])
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1: #There is a servo physicallyt connected,
                self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].grid(row=0+ServoChannel, column=1, padx=1, pady=1, columnspan=1, rowspan=1)
            ###########################################################

            ###########################################################
            self.ServosList_Velocity_GUIscale_LabelObject.append(Label(self.ServoControlsFrame, text="VelM" + str(ServoChannel), width=self.PosVelAccelGuiLabelWidth))
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1:  # There is a servo physically connected,
                self.ServosList_Velocity_GUIscale_LabelObject[ServoChannel].grid(row=0+ServoChannel, column=2, padx=1, pady=1, columnspan=1, rowspan=1)

            self.ServosList_Velocity_GUIscale_Value.append(DoubleVar())
            self.ServosList_Velocity_GUIscale_ScaleObject.append(Scale(self.ServoControlsFrame, \
                                            #label="Velocity Deg for Motor : " + str(ServoChannel), \
                                            from_=self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel],\
                                            to=self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel],\
                                            #tickinterval=(self.ServosList_Velocity_Max_PhidgetsUnits_UserSet[ServoChannel] - self.ServosList_Velocity_Min_PhidgetsUnits_UserSet[ServoChannel]) / 2.0,\
                                            orient=HORIZONTAL,\
                                            borderwidth=2,\
                                            showvalue=True,\
                                            width=self.TkinterScaleWidth,\
                                            length=self.TkinterScaleLength,\
                                            resolution=1,\
                                            variable=self.ServosList_Velocity_GUIscale_Value[ServoChannel]))
            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].bind('<Button-1>', lambda event, name=ServoChannel: self.ServosList_Velocity_GUIscale_EventResponse(event, name))
            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].bind('<B1-Motion>', lambda event, name=ServoChannel: self.ServosList_Velocity_GUIscale_EventResponse(event, name))
            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].bind('<ButtonRelease-1>', lambda event, name=ServoChannel: self.ServosList_Velocity_GUIscale_EventResponse(event, name))
            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].set(self.ServosList_Velocity_Starting_PhidgetsUnits[ServoChannel])
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1: #There is a servo physicallyt connected,
                self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].grid(row=0+ServoChannel, column=3, padx=1, pady=1, columnspan=1, rowspan=1)
            ###########################################################

            ###########################################################
            self.ServosList_EngagedState_GUIcheckbutton_Value.append(DoubleVar())

            if self.ServosList_EngagedState_ToBeSet[ServoChannel] == 1:
                self.ServosList_EngagedState_GUIcheckbutton_Value[ServoChannel].set(1)
            else:
                self.ServosList_EngagedState_GUIcheckbutton_Value[ServoChannel].set(0)

            self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject.append(Checkbutton(self.ServoControlsFrame,
                                                            width=15,
                                                            text='Engage M' + str(ServoChannel),
                                                            state="normal",
                                                            variable=self.ServosList_EngagedState_GUIcheckbutton_Value[ServoChannel]))
            self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject[ServoChannel].bind('<ButtonRelease-1>', lambda event,name=ServoChannel: self.ServosList_EngagedState_GUIcheckbutton_EventResponse(event, name))
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1:  # There is a servo physically connected,
                self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject[ServoChannel].grid(row=0+ServoChannel, column=4, padx=1, pady=1, columnspan=1, rowspan=1)
            ###########################################################

            ###########################################################
            self.ServosList_SpeedRampingState_GUIcheckbutton_Value.append(DoubleVar())

            if self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] == 1:
                self.ServosList_SpeedRampingState_GUIcheckbutton_Value[ServoChannel].set(1)
            else:
                self.ServosList_SpeedRampingState_GUIcheckbutton_Value[ServoChannel].set(0)

            self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject.append(Checkbutton(self.ServoControlsFrame,
                                                            width=15,
                                                            text='SpdRmp M' + str(ServoChannel),
                                                            state="normal",
                                                            variable=self.ServosList_SpeedRampingState_GUIcheckbutton_Value[ServoChannel]))
            self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject[ServoChannel].bind('<ButtonRelease-1>', lambda event,name=ServoChannel: self.ServosList_SpeedRampingState_GUIcheckbutton_EventResponse(event, name))
            if 1:#self.ServoType_PhidgetIntegerList[ServoChannel] != -1:  # There is a servo physically connected,
                self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject[ServoChannel].grid(row=0+ServoChannel, column=5, padx=1, pady=1, columnspan=1, rowspan=1)
            ###########################################################

        ##################################################################################################
        ##################################################################################################

        ###########################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=125)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=3, column=0, padx=10, pady=10, columnspan=10, rowspan=1)
        ###########################################################

        ###########################################################
        self.GUI_ready_to_be_updated_flag = 1
        ###########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServosList_Position_GUIscale_EventResponse(self, event, name):

        ServoChannel = name
        self.ServosList_Position_ToBeSet[ServoChannel] = self.ServosList_Position_GUIscale_Value[ServoChannel].get()
        self.ServosList_Position_NeedsToBeChangedFlag[ServoChannel] = 1

        #self.MyPrint_WithoutLogFile("ServosList_Position_GUIscale_EventResponse: Position set to " + str(self.ServosList_Position_ToBeSet[ServoChannel]) + " on motor " + str(ServoChannel))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServosList_Velocity_GUIscale_EventResponse(self, event, name):

        ServoChannel = name
        self.ServosList_Velocity_ToBeSet[ServoChannel] = self.ServosList_Velocity_GUIscale_Value[ServoChannel].get()
        self.ServosList_Velocity_NeedsToBeChangedFlag[ServoChannel] = 1

        #self.MyPrint_WithoutLogFile("ServosList_Velocity_GUIscale_EventResponse: Velocity set to " + str(self.ServosList_Velocity_ToBeSet[ServoChannel]) + " on motor " + str(ServoChannel))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServosList_EngagedState_GUIcheckbutton_EventResponse(self, event, name):

        ServoChannel = name
        temp_value = self.ServosList_EngagedState_GUIcheckbutton_Value[ServoChannel].get()

        if temp_value == 0:
            self.ServosList_EngagedState_ToBeSet[ServoChannel] = 1 ########## This reversal is needed for the variable state to match the checked state, but we don't know why
        elif temp_value == 1:
            self.ServosList_EngagedState_ToBeSet[ServoChannel] = 0

        self.ServosList_EngagedState_NeedsToBeChangedFlag[ServoChannel] = 1
        
        print("ServosList_EngagedState_GUIcheckbutton_EventResponse: EngagedState changed to " + str(self.ServosList_EngagedState_ToBeSet[ServoChannel]) + " on motor " + str(ServoChannel))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ServosList_SpeedRampingState_GUIcheckbutton_EventResponse(self, event, name):

        ServoChannel = name
        temp_value = self.ServosList_SpeedRampingState_GUIcheckbutton_Value[ServoChannel].get()

        if temp_value == 0:
            self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] = 1 ########## This reversal is needed for the variable state to match the checked state, but we don't know why
        elif temp_value == 1:
            self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] = 0

        self.ServosList_SpeedRampingState_NeedsToBeChangedFlag[ServoChannel] = 1
        
        print("ServosList_SpeedRampingState_GUIcheckbutton_EventResponse: SpeedRampingState changed to " + str(self.ServosList_SpeedRampingState_ToBeSet[ServoChannel]) + " on motor " + str(ServoChannel))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

        #######################################################
        #######################################################
        #######################################################
        #######################################################
        if self.USE_GUI_FLAG == 1 and self.EXIT_PROGRAM_FLAG == 0:

            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                try:

                    #######################################################
                    self.Data_Label["text"] = "\nPosition ActualRx: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.ServosList_Position_ActualRxFromBoard, 0, 1) + \
                                                "\nVelocity ActualRx: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.ServosList_Velocity_ActualRxFromBoard, 0, 6) + \
                                                "\nTime: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.CurrentTime_CalculatedFromMainThread, 0, 3) + \
                                                "\nMain Thread Frequency: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_CalculatedFromMainThread, 0, 3)
                    #######################################################
    
                    #######################################################
                    #######################################################
                    for ServoChannel in range(0, self.NumberOfServos):
                        #########################################################
                        if self.ServosList_Position_GUIscale_NeedsToBeChangedFlag[ServoChannel] == 1:
                            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel].set(self.ServosList_Position_ToBeSet[ServoChannel])
                            self.ServosList_Position_GUIscale_NeedsToBeChangedFlag[ServoChannel] = 0
                        #########################################################

                        #########################################################
                        if self.ServosList_Velocity_GUIscale_NeedsToBeChangedFlag[ServoChannel] == 1:
                            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel].set(self.ServosList_Velocity_ToBeSet[ServoChannel])
                            self.ServosList_Velocity_GUIscale_NeedsToBeChangedFlag[ServoChannel] = 0
                        #########################################################

                        '''
                        #########################################################
                        if self.ServosList_Acceleration_GUIscale_NeedsToBeChangedFlag[ServoChannel] == 1:
                            self.ServosList_Acceleration_GUIscale_ScaleObject[ServoChannel].set(self.ServosList_Acceleration_ToBeSet[ServoChannel])
                            self.ServosList_Acceleration_GUIscale_NeedsToBeChangedFlag[ServoChannel] = 0
                        #########################################################
                        '''
                        
                        #########################################################
                        if self.ServosList_EngagedState_ToBeSet[ServoChannel] == 1:
                            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightGreenColor
                            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightGreenColor
                            #self.ServosList_Acceleration_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightGreenColor
                        else:
                            self.ServosList_Position_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightRedColor
                            self.ServosList_Velocity_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightRedColor
                            #self.ServosList_Acceleration_GUIscale_ScaleObject[ServoChannel]["troughcolor"] = self.TKinter_LightRedColor
                        #########################################################

                        #########################################################
                        if self.ServosList_EngagedState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] == 1:

                            if self.ServosList_EngagedState_ToBeSet[ServoChannel] == 1:  # This actually changes how the widget looks
                                self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject[ServoChannel].select()
                            elif self.ServosList_EngagedState_ToBeSet[ServoChannel] == 0:
                                self.ServosList_EngagedState_GUIcheckbutton_CheckbuttonObject[ServoChannel].deselect()

                            self.ServosList_EngagedState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] = 0
                        #########################################################
                        
                        #########################################################
                        if self.ServosList_SpeedRampingState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] == 1:

                            if self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] == 1:  # This actually changes how the widget looks
                                self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject[ServoChannel].select()
                            elif self.ServosList_SpeedRampingState_ToBeSet[ServoChannel] == 0:
                                self.ServosList_SpeedRampingState_GUIcheckbutton_CheckbuttonObject[ServoChannel].deselect()

                            self.ServosList_SpeedRampingState_GUIcheckbutton_NeedsToBeChangedFlag[ServoChannel] = 0
                        #########################################################
                        
                    #######################################################
                    #######################################################

                    #######################################################
                    self.PrintToGui_Label.config(text=self.PrintToGui_Label_TextInput_Str)
                    #######################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
                    traceback.print_exc()
                #######################################################
                #######################################################

            #######################################################
            #######################################################
            #######################################################

        #######################################################
        #######################################################
        #######################################################
        #######################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputListOfNumbers(self, InputToCheck):

        if isinstance(InputToCheck, list) == 1:
            for element in InputToCheck:
                if isinstance(element, int) == 0 and isinstance(element, float) == 0:
                    return 0
        else:
            return 0

        return 1  # If InputToCheck was a list and no element failed to be a float or int, then return a success/1
    ##########################################################################################################
    ##########################################################################################################

    '''
    ##########################################################################################################
    ##########################################################################################################
    def ServosList_ButtonObjectsResponse(self, ServoChannel):

        if self.ServosList_State[ServoChannel] == 1:
            self.ServosList_State_ToBeSet[ServoChannel] = 0
        else:
            self.ServosList_State_ToBeSet[ServoChannel] = 1

        self.ServosList_State_NeedsToBeChangedFlag[ServoChannel] = 1

        self.MyPrint_WithoutLogFile("ServosList_ButtonObjectsResponse: Event fired for ServoChannel " + str(ServoChannel))

    ##########################################################################################################
    ##########################################################################################################
    '''

    ##########################################################################################################
    ##########################################################################################################
    def MyPrint_WithoutLogFile(self, input_string):

        input_string = str(input_string)

        if input_string != "":

            #input_string = input_string.replace("\n", "").replace("\r", "")

            ################################ Write to console
            # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
            # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
            if self.PrintToConsoleFlag == 1:
                sys.stdout.write(input_string + "\n")
            ################################

            ################################ Write to GUI
            self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
            self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

            self.PrintToGui_Label_TextInput_Str = ""
            for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

                if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                    self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
            ################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputList(self, InputToCheck):

        result = isinstance(InputToCheck, list)
        return result
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
