#!/ usr / bin / python3

import os
from time import sleep 
while 1>0: 
	cmd = 'cat /sys/class/power_supply/BAT0/capacity'
	bat = int(os.popen(cmd).read())
	if bat < 10 or bat == 100: 
	    os.system('brightnessctl --device=\'asus::kbd_backlight\' set 0')
	    sleep(0.5) 
	    os.system('brightnessctl --device=\'asus::kbd_backlight\' set 1')
	    sleep(0.3) 
	    os.system('brightnessctl --device=\'asus::kbd_backlight\' set 2')
	    sleep(0.3) 
	    os.system('brightnessctl --device=\'asus::kbd_backlight\' set 3')
	    sleep(0.5) 
