########################

PhidgetsAdvancedServo8MotorRCC0004_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) to control Phidgets Advanced Servo 8-Motor RCC0004_0 (non VINT).

From Phidgets' website:
"The PhidgetAdvancedServo 8-Motor allows you to control the position, velocity,
and acceleration of up to 8 RC servo motors. It requires a 8-30VDC external power supply; its switching power supply
allows the RCC0004 to efficiently operate from 8 to 30 VDC and can be used with a wide range of batteries.
You can control the regulator and choose a global servo voltage of 5.0V, 6.0V, or 7.4V.
A servo will have more torque when running at a higher voltage, but will have a shorter overall lifespan.
Check your servo's data sheet and balance the voltage for your specific application.
For a list of compatible power supplies, see the Connection & Compatibility tab.
The RCC0004 connects directly to a computer’s USB port."

Phidget Advanced Servo 8-Motor
ID: RCC0004_0
https://phidgets.com/?tier=3&catid=21&pcid=18&prodid=1147

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision F, 03/13/2022

Verified working on: 
Python 2.7, 3.8.
Windows 8.1, 10 64-bit
Raspberry Pi Buster 
(no Mac testing yet)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

########################  

########################### Python module installation instructions, all OS's

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22
 
###########################