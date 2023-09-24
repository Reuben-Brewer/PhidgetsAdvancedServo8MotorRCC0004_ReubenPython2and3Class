# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision J, 09/24/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
from PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
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
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

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
    global USE_MyPrint_FLAG

    if USE_MyPrint_FLAG == 1:
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
    global PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG
    global SHOW_IN_GUI_PhidgetsAdvancedServo8MotorRCC0004_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG == 1 and SHOW_IN_GUI_PhidgetsAdvancedServo8MotorRCC0004_FLAG == 1:
                PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
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
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsAdvancedServo8MotorRCC0004
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_PhidgetsAdvancedServo8MotorRCC0004 = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_PhidgetsAdvancedServo8MotorRCC0004, text='   SERVOS   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_PhidgetsAdvancedServo8MotorRCC0004 = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    TestButton = Button(Tab_MainControls, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
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

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1
    
    global USE_PhidgetsAdvancedServo8MotorRCC0004_FLAG
    USE_PhidgetsAdvancedServo8MotorRCC0004_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_PhidgetsAdvancedServo8MotorRCC0004_POSITION_CONTROL_FLAG
    USE_PhidgetsAdvancedServo8MotorRCC0004_POSITION_CONTROL_FLAG = 1 #SET TO 0 FOR VELOCITY CONTROL

    global USE_PhidgetsAdvancedServo8MotorRCC0004_SINUSOIDAL_INPUT_FLAG
    USE_PhidgetsAdvancedServo8MotorRCC0004_SINUSOIDAL_INPUT_FLAG = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_PhidgetsAdvancedServo8MotorRCC0004_FLAG
    SHOW_IN_GUI_PhidgetsAdvancedServo8MotorRCC0004_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_PhidgetsAdvancedServo8MotorRCC0004
    global GUI_COLUMN_PhidgetsAdvancedServo8MotorRCC0004
    global GUI_PADX_PhidgetsAdvancedServo8MotorRCC0004
    global GUI_PADY_PhidgetsAdvancedServo8MotorRCC0004
    global GUI_ROWSPAN_PhidgetsAdvancedServo8MotorRCC0004
    global GUI_COLUMNSPAN_PhidgetsAdvancedServo8MotorRCC0004
    GUI_ROW_PhidgetsAdvancedServo8MotorRCC0004 = 1

    GUI_COLUMN_PhidgetsAdvancedServo8MotorRCC0004 = 0
    GUI_PADX_PhidgetsAdvancedServo8MotorRCC0004 = 1
    GUI_PADY_PhidgetsAdvancedServo8MotorRCC0004 = 1
    GUI_ROWSPAN_PhidgetsAdvancedServo8MotorRCC0004 = 1
    GUI_COLUMNSPAN_PhidgetsAdvancedServo8MotorRCC0004 = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
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

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsAdvancedServo8MotorRCC0004
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

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
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject

    global PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG
    PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG = -1

    global NumberOfServos
    NumberOfServos = 16

    global DesiredBoardEnglishName
    DesiredBoardEnglishName = "RCC1000"# "RCC0004", "RCC1000" currently supported

    global ServosList_TestChannelsList
    ServosList_TestChannelsList = [0, 2]

    global PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict
    PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict = dict()

    global PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_PhidgetsAdvancedServo8MotorRCC0004List_ErrorCallbackFiredFlag
    PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_PhidgetsAdvancedServo8MotorRCC0004List_ErrorCallbackFiredFlag = [-1] * NumberOfServos

    global PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_Time
    PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
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
        Tab_MainControls = None
        Tab_PhidgetsAdvancedServo8MotorRCC0004 = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_PhidgetsAdvancedServo8MotorRCC0004_FLAG),
                                    ("root", Tab_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("GUI_COLUMN", GUI_COLUMN_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("GUI_PADX", GUI_PADX_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("GUI_PADY", GUI_PADY_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_PhidgetsAdvancedServo8MotorRCC0004),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_PhidgetsAdvancedServo8MotorRCC0004)])

    global PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict
    PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                ("DesiredBoardEnglishName", DesiredBoardEnglishName), #"RCC0004", "RCC1000" currently supported
                                                                                ("DesiredSerialNumber", -1), #-1 MEANS ANY SN, CHANGE THIS FOR YOUR UNIQUE SERIAL NUMBER
                                                                                ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                                                                                ("NameToDisplay_UserSet", "Reuben's Test Advanced Servo 8-Motor RCC0004_0 Controller"),
                                                                                ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                                                ("MainThread_TimeToSleepEachLoop", 0.002),
                                                                                ("ServosList_DataIntervalMilliseconds", [32.0]*NumberOfServos),
                                                                                ("ServosList_EngagedState_Starting", [1]*NumberOfServos),
                                                                                ("ServosList_SpeedRampingState_Starting", [0]*NumberOfServos),
                                                                                ("ServosList_Position_Min_PhidgetsUnits_UserSet", [0.0]*NumberOfServos),
                                                                                ("ServosList_Position_Max_PhidgetsUnits_UserSet", [180.0]*NumberOfServos),
                                                                                ("ServosList_Position_Starting_PhidgetsUnits", [90.0]*NumberOfServos),
                                                                                ("ServosList_Velocity_Min_PhidgetsUnits_UserSet", [0.0]*NumberOfServos),
                                                                                ("ServosList_Velocity_Max_PhidgetsUnits_UserSet", [180.0]*NumberOfServos),
                                                                                ("ServosList_Velocity_Starting_PhidgetsUnits", [90.0]*NumberOfServos),
                                                                                ("ServosList_PulseWidthMin_PhidgetsUnits_UserSet", [600.0]*NumberOfServos),
                                                                                ("ServosList_PulseWidthMax_PhidgetsUnits_UserSet", [2400.0]*NumberOfServos),
                                                                                ("ServosList_Voltage_PhidgetsUnits_UserSet", [7.4]*NumberOfServos)])
                                                                                #### IMPLEMENT FAILSAFE enableFailsafe()
    if USE_PhidgetsAdvancedServo8MotorRCC0004_FLAG == 1:
        try:
            PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class(PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject_setup_dict)
            PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PhidgetsAdvancedServo8MotorRCC0004_FLAG == 1 and PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG != 1:
        print("Failed to open PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PhidgetsAdvancedServo8MotorRCC0004_SINUSOIDAL_INPUT_FLAG == 1:
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
        if USE_PhidgetsAdvancedServo8MotorRCC0004_FLAG == 1:

            ##################### GET's
            PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict = PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict:
                PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_PhidgetsAdvancedServo8MotorRCC0004List_ErrorCallbackFiredFlag = PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict["ServosList_ErrorCallbackFiredFlag"]
                PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_Time = PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict["Time"]

                #print("PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_PhidgetsAdvancedServo8MotorRCC0004List_State: " + str(PhidgetsAdvancedServo8MotorRCC0004_MostRecentDict_PhidgetsAdvancedServo8MotorRCC0004List_State))
            #####################

            ##################### SET's
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)

            if USE_PhidgetsAdvancedServo8MotorRCC0004_SINUSOIDAL_INPUT_FLAG == 1:

                if USE_PhidgetsAdvancedServo8MotorRCC0004_POSITION_CONTROL_FLAG == 1:
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
    if PhidgetsAdvancedServo8MotorRCC0004_OPEN_FLAG == 1:
        PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################