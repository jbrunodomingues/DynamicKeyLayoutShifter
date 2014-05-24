__author__ = 'bruno'


import subprocess
from evdev import InputDevice, ecodes

dev = InputDevice('/dev/input/by-path/platform-i8042-serio-0-event-kbd')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.code == 125:
            if event.value == 1:
                subprocess.call(["/home/bruno/keycontrol/keyShiftArrows"])
            elif event.value == 0:
                subprocess.call(["/home/bruno/keycontrol/keyShiftLetters"])



