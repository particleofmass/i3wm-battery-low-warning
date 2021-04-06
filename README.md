# i3wm-battery-low-warning
## Works only for back-lit keyboards

I suppose you're a linux intermediate/pro(btw I'm not) just because you use i3wm so you can edit the python file right away and you'll understand it easily but in case you want to go through some boring procedure then read below.

### How this works :
This is a simple python program that loops through the brightness levels of your backlight keyboard when you're battery is below 10%. I did not know how to create gui notifications so I thought this is a better way. 
And if you have only white backlight then you can edit this file to use the brightness flickering to make your keyboard feel like a gaming keyboard, but I basically use as a battery warning.

### How to use :
All you have to do is install brightnessctl, move the program to your preferred location, make it executable and then add a command in your i3 config file to run it on startup.
But before that you'll have to edit the file a bit. And to do that type " ls /sys/class/power_supply/BAT0/capacity " without quotes and that should output the current battery percentage if not then just skip the "BAT0/capacity" part and list all the directories in .../power_supply and check which one corresponds to the file capacity file.
If you find it then replace the value of 'cmd' in the python program.
And now one more line to go, for that type " ls /sys/class/leds/ " and find the device which corresponds to your keyboard backlight, mine is asus::kbd_backlight. Replace 'asus::kbd_backlight' with your device name in the python file.

Now you're almost done. Install brightnessctl by typing " sudo <your-pkg-manager> install brightnessctl " or
 " sudo pacman -S brightnessctl " for arch linux. 

Move gamer.py to your desired location and to make it executable type " sudo chmod +x gamer.py ".

Now add the below command i3 config file:
exec --no-startup-id python3 <location of gamer.py>
