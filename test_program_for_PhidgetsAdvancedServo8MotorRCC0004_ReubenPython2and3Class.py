# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision E, 03/01/2022

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

from PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *

import os, sys, platform
import time, datetime
import threading
import collections

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

###############
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###############

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject
    global SERVOS_OPEN_FLAG
    global SHOW_IN_GUI_SERVOS_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if SERVOS_OPEN_FLAG == 1 and SHOW_IN_GUI_SERVOS_FLAG == 1:
                PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global GUI_RootAfterCallbackInterval_Milliseconds

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    TestButton = Button(root, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_SERVOS_FLAG
    USE_SERVOS_FLAG = 1

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1

    global USE_SERVOS_POSITION_CONTROL_FLAG
    USE_SERVOS_POSITION_CONTROL_FLAG = 1 #SET TO 0 FOR VELOCITY CONTROL

    global USE_SERVOS_SINUSOIDAL_INPUT_FLAG
    USE_SERVOS_SINUSOIDAL_INPUT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_SERVOS_FLAG
    SHOW_IN_GUI_SERVOS_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_SERVOS
    global GUI_COLUMN_SERVOS
    global GUI_PADX_SERVOS
    global GUI_PADY_SERVOS
    global GUI_ROWSPAN_SERVOS
    global GUI_COLUMNSPAN_SERVOS
    GUI_ROW_SERVOS = 1

    GUI_COLUMN_SERVOS = 0
    GUI_PADX_SERVOS = 1
    GUI_PADY_SERVOS = 10
    GUI_ROWSPAN_SERVOS = 1
    GUI_COLUMNSPAN_SERVOS = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl
    SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl = 0.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl
    SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl = 90.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl
    SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl = -1.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl
    SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl = 1.0

    global root

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject

    global SERVOS_OPEN_FLAG
    SERVOS_OPEN_FLAG = -1

    global NumberOfServos
    NumberOfServos = 8

    global ServosList_TestChannelsList
    ServosList_TestChannelsList = []#[0, 2]

    global SERVOS_MostRecentDict

    global SERVOS_MostRecentDict_ServosList_ErrorCallbackFiredFlag
    SERVOS_MostRecentDict_ServosList_ErrorCallbackFiredFlag = [-1] * NumberOfServos

    global SERVOS_MostRecentDict_Time
    SERVOS_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_SERVOS_FLAG),
                                    ("root", root),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_SERVOS),
                                    ("GUI_COLUMN", GUI_COLUMN_SERVOS),
                                    ("GUI_PADX", GUI_PADX_SERVOS),
                                    ("GUI_PADY", GUI_PADY_SERVOS),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_SERVOS),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_SERVOS)])

    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict
    PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                ("DesiredSerialNumber", 594289), #CHANGE THIS FOR YOUR UNIQUE SERIAL NUMBER
                                                                                ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                                                                                ("NameToDisplay_UserSet", "Reuben's Test Advanced Servo 8-Motor RCC0004_0 Controller"),
                                                                                ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                                                ("MainThread_TimeToSleepEachLoop", 0.002),
                                                                                ("ServosList_DataIntervalMilliseconds", [32.0, 32.0, 32.0, 32.0, 32.0, 32.0, 32.0, 32.0]),
                                                                                ("ServosList_EngagedState_Starting", [0, 0.0, 0, 0, 0, 0, 0, 1]),
                                                                                ("ServosList_SpeedRampingState_Starting", [0, 0, 0, 0, 0, 0, 1, 0]),
                                                                                ("ServosList_Position_Min_PhidgetsUnits_UserSet", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
                                                                                ("ServosList_Position_Max_PhidgetsUnits_UserSet", [2826.0, 180.0, 180.0, 180.0, 180.0, 180.0, 180.0, 180.0]),
                                                                                ("ServosList_Position_Starting_PhidgetsUnits", [90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0]),                                                                            ("ServosList_PositionMin_PhidgetsUnits_UserSet", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
                                                                                ("ServosList_Velocity_Min_PhidgetsUnits_UserSet", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
                                                                                ("ServosList_Velocity_Max_PhidgetsUnits_UserSet", [180.0, 180.0, 180.0, 180.0, 180.0, 180.0, 180.0, 180.0]),
                                                                                ("ServosList_Velocity_Starting_PhidgetsUnits", [90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0]),
                                                                                ("ServosList_PulseWidthMin_PhidgetsUnits_UserSet", [600.0, 550.0, 550.0, 550.0, 550.0, 550.0, 550.0, 550.0]),
                                                                                ("ServosList_PulseWidthMax_PhidgetsUnits_UserSet", [2400.0, 2450.0, 2450.0, 2450.0, 2450.0, 2450.0, 2450.0, 2450.0])])
                                                                                #### IMPLEMENT FAILSAFE
    if USE_SERVOS_FLAG == 1:
        try:
            PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class(PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            SERVOS_OPEN_FLAG = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", root),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_SERVOS_FLAG == 1 and SERVOS_OPEN_FLAG != 1:
        print("Failed to open PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_SERVOS_SINUSOIDAL_INPUT_FLAG == 1:
        for ServoChannel in range(0, NumberOfServos):
            if ServoChannel in ServosList_TestChannelsList:
                PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.SetEnagagedState(ServoChannel, 1)
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        ###################################################
        if USE_SERVOS_FLAG == 1:

            ##################### GET's
            SERVOS_MostRecentDict = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in SERVOS_MostRecentDict:
                SERVOS_MostRecentDict_ServosList_ErrorCallbackFiredFlag = SERVOS_MostRecentDict["ServosList_ErrorCallbackFiredFlag"]
                SERVOS_MostRecentDict_Time = SERVOS_MostRecentDict["Time"]

                #print("SERVOS_MostRecentDict_ServosList_State: " + str(SERVOS_MostRecentDict_ServosList_State))
            #####################

            #####################
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)

            if USE_SERVOS_SINUSOIDAL_INPUT_FLAG == 1:

                if USE_SERVOS_POSITION_CONTROL_FLAG == 1:
                    SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl + SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_PositionControl - SINUSOIDAL_MOTION_INPUT_MinValue_PositionControl)*math.sin(time_gain*CurrentTime_MainLoopThread)

                    for ServoChannel in range(0, NumberOfServos):
                        if ServoChannel in ServosList_TestChannelsList:
                            PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.SetPosition(ServoChannel, SINUSOIDAL_INPUT_TO_COMMAND)

                else:
                    SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl + SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_VelocityControl - SINUSOIDAL_MOTION_INPUT_MinValue_VelocityControl)*math.sin(time_gain*CurrentTime_MainLoopThread)

                    for ServoChannel in range(0, NumberOfServos):
                        if ServoChannel in ServosList_TestChannelsList:
                            PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.SetPosition(ServoChannel, SINUSOIDAL_INPUT_TO_COMMAND)
            #####################

        ###################################################

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class.")

    #########################################################
    if SERVOS_OPEN_FLAG == 1:
        PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################