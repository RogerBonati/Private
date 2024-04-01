# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

powerline = {
    "decorations": [
        PowerLineDecoration()
    ]
}

#from qtile_extras.widget import StatusNotifier
import colors

mod1 = "mod4"              # Sets mod key to SUPER/WINDOWS
mod = "mod1"
myTerm = "alacritty"      # My terminal of choice
bwidth = 2

dgrey="#333333"
dgrey2="#A9A9A9"
lgrey="#CCCCCC"
lgrey2="#D3D3D3"
black="#000000"
white="#FFFFFF"

#myTerm = "xterm"      # My terminal of choice

# Allows you to input a name when adding treetab section.

@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()
           
# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == 'monadtall':
        qtile.current_group.layout = 'max'
    elif current_layout_name == 'max':
        qtile.current_group.layout = 'monadtall'

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "d",
        lazy.layout.down()
    ),
    Key(
        [mod], "u",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod1, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod1, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    Key([mod, "control"], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod, "control"], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod, "control"], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "control"], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "control"], "space", lazy.layout.next(), desc="Move window focus to other window"),




    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # launch brave browser
    Key([mod], "b", lazy.spawn("brave-browser")),
    
    # launch chromium
    Key([mod], "c", lazy.spawn("chromium")),

    # launch forefox
    Key([mod], "f", lazy.spawn("firefox")),
    
    # launch google-chrome
    Key([mod], "g", lazy.spawn("google-chrome")),
    
    # launch konqueror
    Key([mod], "k", lazy.spawn("konqueror")),

    # launch screensaver
    Key([mod], "l", lazy.spawn("mate-screensaver-command -l")),
    
    #Key([mod], "m", lazy.layout.maximize(), desc='Toggle between min and max sizes'),
    Key([mod], "m", lazy.window.toggle_fullscreen()),

    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),

    Key([mod], "r", lazy.spawncmd()),
  
    # launch vlc
    Key([mod], "v", lazy.spawn("vlc")),

    Key([mod], "w", lazy.window.kill()),
    
    # launch keepassx
    Key([mod], "x", lazy.spawn("keepassx")),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # launch menu window
    Key([mod, "control"], "m", lazy.spawn("rofi -show drun")),
    
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    
    # select a new wallpaper
    # Key([mod, "control"], "w", lazy.spawn_multiple("find ~/Eigenedat/Bilder -type f | shuf -n 1 | xargs xwallpaper --stretch"))
    Key([mod, "control"], "w", lazy.spawn("sh -c 'find ~/Eigenedat/Bilder -type f | shuf -n 1 | xargs xwallpaper --stretch'"))
]

groups = []
#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_names = ["1", "2", "3", "4", "5", "6", "7"]

#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["WWW", "TERM", "CHROM", "KONQ", "VID", "SYS", "REST"]
#group_labels = ["", "", "", "", "", "", "", "", "",]

#group_layouts = ["monadtall", "monadtall", "tile", "tile", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]
group_layouts = ["max", "max", "tile", "tile", "max", "stack", "monadtall"]
#group_layouts = ["max", "max", "max", "max", "max", "max"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
 
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod1],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod1, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

#colors = colors.DoomOne
colors = colors.Dracula

layout_theme = {
    "border_width": 4,
    "margin": 0,
    "border_focus": lgrey2, # Dark grey for focused windows
    "border_normal": dgrey # Light grey for unfocused windows
}

layouts = [
    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme)
    layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.Tile(
        shift_windows=True,
        border_width = bwidth,
        margin = 0,
        ratio = 0.335,
    ),
    layout.Max(
        border_width = bwidth,
        margin = 0,
    ),
    layout.Stack(**layout_theme, num_stacks=2),
    #layout.Columns(**layout_theme),
    layout.TreeTab(
        font = "Ubuntu Bold",
        fontsize = 11,
        border_width = bwidth,
        bg_color = colors[0],
        active_bg = colors[8],
        active_fg = colors[2],
        inactive_bg = colors[1],
        inactive_fg = colors[0],
        padding_left = 8,
        padding_x = 8,
        padding_y = 6,
        sections = ["ONE", "TWO", "THREE"],
        section_fontsize = 10,
        section_fg = colors[7],
        section_top = 15,
        section_bottom = 15,
        level_shift = 8,
        vspace = 3,
        panel_width = 240
    ),
    #layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 12,
    padding = 8,
    background=colors[0]
)

# extension_defaults = widget_defaults.copy()
widget_list_bottom = [
    widget.Image(
        filename = "~/.config/qtile/icons/qtile.png",
        mouse_callbacks = {'Button1': lambda: qtile.spawn("rofi -show drun")},
    ),
    widget.Spacer(length = 8),
    widget.WindowTabs(),
#    widget.Spacer(length = 8,
#        foreground = black,
#        background = lgrey2,
#        **powerline
#    ),
    widget.Bluetooth(
        mouse_callbacks={"Button1": lambda: qtile.spawn("blueman-manager")},
        background = dgrey,
        **powerline
    ),
    widget.Volume(
        volume_down_command="amixer set Master 5%-",
        volume_up_command="amixer set Master 5%+",
        mouse_callbacks={"Button1": lambda: qtile.spawn("pactl set-sink-mute 0 toggle")},
        background = lgrey2,
        foreground = black,
        fmt = ' Vol: {}',
        **powerline
    ), 
    widget.Clock(
        format = "⏱  %a, %d %b %Y - %H:%M:%S",
        background = dgrey,
        **powerline
    ),
    widget.QuickExit(
        background = lgrey2,
        **powerline
    ),
    widget.Spacer(
        length = 8,
        background = dgrey,
    ),
]

widget_end_with_systray = [
    widget.Spacer(length = 8,
        background = dgrey,
        **powerline
    ),
    widget.Systray(
        background = lgrey2,
        foreground = black,
        **powerline
    ),
    # widget.Spacer(length = 8),
    widget.Battery(
        background = dgrey,
        **powerline
    ),
    #widget.Spacer(length = 8),
    widget.Clock(
        #foreground = colors[8],
        format = "⏱  %a, %d %b %Y - %H:%M:%S",
        foreground = black,
        background = lgrey2,
        **powerline
    ),
    widget.QuickExit(
        background = dgrey,
        **powerline
    ),
]

widget_end_without_systray = [
    #widget.Spacer(length = 8),
    widget.Battery(
        background = dgrey,
        **powerline
    ),
    widget.Clock(
        #foreground = colors[8],
        format = "⏱  %a, %d %b %Y - %H:%M:%S",
        background = lgrey2,
        foreground = black,
        **powerline

    ),
    #widget.Spacer(length = 8),
    widget.QuickExit(
        background = dgrey,
        **powerline
    ),
]

widget_list_top = [
    widget.Image(
        filename = "~/.config/qtile/icons/logo.png",
        scale = "False",
        mouse_callbacks = {'Button1': lambda: qtile.spawn('dmenu_run -i')},
    ),
    
    widget.Spacer(length = 8),
    widget.Prompt(
        font = "Ubuntu Mono",
        fontsize=14,
        foreground = colors[1]
    ),
    widget.Spacer(length = 8),
    widget.GroupBox(
        fontsize = 11,
        margin_y = 5,
        margin_x = 5,
        padding_y = 0,
        padding_x = 1,
        borderwidth = 3,
        active = colors[8],
        inactive = colors[1],
        rounded = False,
        highlight_color = colors[2],
        highlight_method = "line",
        this_current_screen_border = colors[7],
        this_screen_border = colors [4],
        other_current_screen_border = colors[7],
        other_screen_border = colors[4],
    ),
    widget.Spacer(length = 8),
    widget.TextBox(
        text = '|',
        font = "Ubuntu Mono",
        foreground = colors[1],
        padding = 2,
        fontsize = 14
    ),
    widget.Spacer(length = 8),
    widget.CurrentLayout(
        foreground = colors[1],
        padding = 5
    ),
    widget.Spacer(length = 8),
    widget.TextBox(
        text = '|',
        font = "Ubuntu Mono",
        foreground = colors[1],
        padding = 2,
        fontsize = 14
    ),
    widget.Spacer(length = 8),
    widget.WindowName(
        foreground = colors[6],
        max_chars = 40
    ),
#    widget.Spacer(length = 8,
#        foreground = black,
#        background = lgrey2,
#        **powerline
#    ),
    widget.GenPollText(
        update_interval = 300,
        func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
        fmt = 'kernel: {}',
        background = dgrey,
        **powerline
    ),
    widget.CPU(
        #format = '▓  Cpu: {load_percent}%',
        format = 'cpu: {load_percent}%',
        background = lgrey2,
        foreground = black,
        **powerline
    ),
    widget.Memory(
        format = '{MemUsed: .0f}{mm}',
        #fmt = '🖥  Mem: {} used',
        fmt = 'memory: {} used',
        background = dgrey,
        **powerline
    ),
    widget.DF(
        update_interval = 60,
        partition = '/',
        #format = '[{p}] {uf}{m} ({r:.0f}%)',
        format = '{uf}{m} free',
        #fmt = '🖴  Disk: {}',
        fmt = 'disk: {}',
        visible_on_warn = False,
        background = lgrey2,
        foreground = black,
        **powerline
    ),
 ]

def init_widgets_screen1():
    return widget_list_top + widget_end_with_systray

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    return widget_list_top + widget_end_without_systray

# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),

def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), size=26),
            bottom=bar.Bar(widgets=widget_list_bottom, size=26),
        ),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
    ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

#floating_layout = layout.Floating(
#    border_focus=colors[8],
#    border_width=2,
#    float_rules=[
#        # Run the utility of `xprop` to see the wm class and name of an X client.
#        *layout.Floating.default_float_rules,
#        Match(wm_class="confirmreset"),   # gitk
#        Match(wm_class="dialog"),         # dialog boxes
#        Match(wm_class="download"),       # downloads
#        Match(wm_class="error"),          # error msgs
#        Match(wm_class="file_progress"),  # file progress boxes
#        Match(wm_class='kdenlive'),       # kdenlive
#        Match(wm_class="makebranch"),     # gitk
#        Match(wm_class="maketag"),        # gitk
#        Match(wm_class="notification"),   # notifications
#        Match(wm_class='pinentry-gtk-2'), # GPG key password entry
#        Match(wm_class="ssh-askpass"),    # ssh-askpass
#        Match(wm_class="toolbar"),        # toolbars
#        Match(wm_class="Yad"),            # yad boxes
#        Match(title="branchdialog"),      # gitk
#        Match(title='Confirmation'),      # tastyworks exit box
#        Match(title='Qalculate!'),        # qalculate-gtk
#        Match(title="pinentry"),          # GPG key password entry
#        Match(title="tastycharts"),       # tastytrade pop-out charts
#        Match(title="tastytrade"),        # tastytrade pop-out side gutter
#        Match(title="tastytrade - Portfolio Report"), # tastytrade pop-out allocation
#        Match(wm_class="tasty.javafx.launcher.LauncherFxApp"), # tastytrade settings
#    ]
#)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
