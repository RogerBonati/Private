alias cleanup="rm -r ~/.cache/konqueror"
alias wttr="curl http://wttr.in/traunstein"
#alias wttr="curl http://wttr.in/$2"
alias wttrt="curl http://wttr.in/traunstein"
alias wttrm="curl http://wttr.in/muenchen"
alias wttrl="curl http://wttr.in/langhirano"
alias ghidra="/opt/ghidra/ghidraRun"
# alias chrome='xhost local:root docker run -d --net host --security-opt seccomp=~/containers/chrome/seccomp-chrome.json -v ~/containers/chrome/:/home/chrome/chrome-profile -v /var/run/dbus:/var/run/dbus -v /etc/hosts:/etc/hosts -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -v ~/Downloads:/home/chrome/Downloads --device /dev/snd:/dev/snd --device /dev/dri -v /dev/shm:/dev/shm --name chrome aimvector/chrome'
#alias quemu='qemu-system-arm -kernel ~/Eigenedat/Tmp/quemu_vms/kernel-qemu-4.4.34-jessie -cpu arm1176 -m 256 -serial stdio -append "root=/dev/sda2 rootfstype=ext4 rw" -M versatilepb -hda ~/Eigenedat/Tmp/quemu_vms/2017-04-10-raspbian-jessie.img -nic user,hostfwd=tcp::5022-:22 -no-reboot'
alias vlc="~/Eigenedat/Skripte/Shell/disable-screensaver.sh && /usr/bin/vlc &"
alias st='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -'
# ---- Eza (better ls) -----

alias lse="eza --color=always --long --no-filesize --icons=always --no-time --no-user --no-permissions"
alias ls2="eza --color=always --long --icons=always"

# alias cd="z"

alias fman="compgen -c | fzf | xargs man"

alias bs="fzf --preview='bat --color=always {}'"
alias inv='nvim -c "tab all" $(fzf -m --preview "bat --color always {}")'

cheat() {
  curl https://cheat.sh/$1
}

alias pbcopy='xsel --input --clipboard'
alias pbpaste='xsel --output --clipboard'

# yt-dlp
alias yt="yt-dlp --no-playlist"
alias screenconfig="xrandr --output eDP-1 --primary --mode 1920x1080 --output DP-2-2 --mode 1920x1200 --above eDP-1"
