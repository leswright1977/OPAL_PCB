# OPAL_PCB
PCB design for OpenGalvo OPAL

These are the PCB files and schematic for this awesome project: https://github.com/opengalvo/OPAL/

![Screenshot](media/xy2100.png)

***Note:***
When I Scoped the Tickle pulse, the width is too short for a Synrad 48. It should have a width of 1uS
Easy fix, in lib/LaserController/Synrad48Ctrl.h line 54 change this
const static uint16_t ticklePWM = 4;
To this:
const static uint16_t ticklePWM = 20;

An issue has been opened in the original project.
