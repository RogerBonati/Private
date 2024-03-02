alias cleanup="rm -r ~/.cache/konqueror"
alias wttr="curl http://wttr.in/traunstein"
#alias wttr="curl http://wttr.in/$2"
alias wttrt="curl http://wttr.in/traunstein"
alias wttrm="curl http://wttr.in/muenchen"
alias wttrl="curl http://wttr.in/langhirano"
alias ghidra="/opt/ghidra/ghidraRun"
# alias chrome='xhost local:root docker run -d --net host --security-opt seccomp=~/containers/chrome/seccomp-chrome.json -v ~/containers/chrome/:/home/chrome/chrome-profile -v /var/run/dbus:/var/run/dbus -v /etc/hosts:/etc/hosts -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -v ~/Downloads:/home/chrome/Downloads --device /dev/snd:/dev/snd --device /dev/dri -v /dev/shm:/dev/shm --name chrome aimvector/chrome'
alias quemu='qemu-system-arm -kernel ~/Eigenedat/Tmp/quemu_vms/kernel-qemu-4.4.34-jessie -cpu arm1176 -m 256 -serial stdio -append "root=/dev/sda2 rootfstype=ext4 rw" -M versatilepb -hda ~/Eigenedat/Tmp/quemu_vms/2017-04-10-raspbian-jessie.img -nic user,hostfwd=tcp::5022-:22 -no-reboot'
alias vlc="~/Eigenedat/Skripte/Shell/disable-screensaver.sh && /usr/bin/vlc &"
alias st='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -'

cheat() {
  curl https://cheat.sh/$1
}
