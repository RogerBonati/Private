#!/usr/bin/env bash 

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find "$HOME"/Eigenedat/Bilder -type f | shuf -n 1 | xargs xwallpaper --stretch &
pic=$(find "$HOME"/Eigenedat/Bilder -type f | shuf -n 1) && echo $(date) selected wallpaper: $pic >> ~/wallpaper_log.txt && xwallpaper --stretch $pic

# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

# map caps-lock to escape
setxkbmap -layout de -option caps:escape

#COLORSCHEME=DoomOne
COLORSCHEME=Dracula

### AUTOSTART PROGRAMS ###
udiskie &
mate-screensaver &
#lxsession &
picom --daemon &
#picom --daemon -f --xrender-fence
#nm-applet &
# "$HOME"/.screenlayout/layout.sh &

