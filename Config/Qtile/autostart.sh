#!/usr/bin/env bash 

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
find "$HOME"/Eigenedat/Bilder -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

# Base directory for mount points
BASE_MOUNT_DIR="/media/br"

# Mount options as observed in MATE
MOUNT_OPTIONS="rw,nodev,nosuid,uid=1001,gid=1001,windows_names,uhelper=udisks2"

# List all block devices and their labels
DEVICES=$(udisksctl status | grep -oP '(?<=device: /dev/sd)[a-z]')

for DEVICE in $DEVICES; do
    # Get the label of the device
    LABEL=$(udisksctl info -b /dev/sd$DEVICE | grep -oP '(?<=label: ).*')
    
    # If the label is empty, use the device name as a fallback
    if [ -z "$LABEL" ]; then
        LABEL="Disc$DEVICE"
    fi
    
    # Create the mount point directory if it doesn't exist
    MOUNT_POINT="$BASE_MOUNT_DIR/$LABEL"
    mkdir -p "$MOUNT_POINT"
    
    # Mount the device
    udisksctl mount -b /dev/sd$DEVICE -o $MOUNT_OPTIONS
done

# Start udiskie for automounting
udiskie -2 &

setxkbmap de
#COLORSCHEME=DoomOne
COLORSCHEME=Dracula
mate-screensaver &


### AUTOSTART PROGRAMS ###
#lxsession &
picom --daemon &
#picom --daemon -f --xrender-fence

#/usr/bin/emacs --daemon &
#nm-applet &
# "$HOME"/.screenlayout/layout.sh &
#sleep 1
#conky -c "$HOME"/.config/conky/qtile/01/"$COLORSCHEME".conf || echo "Couldn't start conky."

