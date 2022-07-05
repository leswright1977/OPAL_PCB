# OPAL_PCB
PCB design for OpenGalvo OPAL

These are the PCB files and schematic for this awesome project: https://github.com/opengalvo/OPAL/
I have sucessfully used this to Drive a Domino D100+ Coder Head
(Video will be posted soon)

As discussed itn eh original design, an SN75174 Line Driver is used to drive the Galvo head.
Additionally a CD74HC4050 is used to raise the logic levels for the Galvo SSR, Laser SSR and Laser PWM signals from 3v3 to 5V.


![Screenshot](media/xy2100.png)


PCB Top Side:

![Screenshot](media/front.png)

PCB Back Side:

![Screenshot](media/back.png)


Populated PCB:

![Screenshot](media/populated.png)




***Note:***
When I Scoped the Tickle pulse, the width is too short for a Synrad 48. It should have a width of 1uS
Easy fix, in lib/LaserController/Synrad48Ctrl.h line 54 change this
const static uint16_t ticklePWM = 4;
To this:
const static uint16_t ticklePWM = 21;

An issue has been opened in the original project.

(For now, fixed code is availble here OPAL-master.zip)
