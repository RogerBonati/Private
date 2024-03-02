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

#from libqtile.config import Key, Screen, Group, Drag, Click
#from libqtile.command import lazy
#from libqtile import layout, bar, widget
#import subprocess

import os
import re
import socket
import subprocess
import psutil
import json
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration


mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

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
    # Key([mod], "Return", lazy.spawn("xterm")),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

#groups = [Group(i) for i in "asdfuiop"]

def init_group_names():
    return [('WWW', {"layout": "max"}),
            ('DEV', {"layout": "max"}),
            ('TERM', {"layout": "stack"}),
            ('DOC', {"layout": "max"}),
            ('MUS', {"layout": "max"}),
            ('VID', {"layout": "max"}),
            ('GFX', {"layout": "max"})]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))  # switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

#for i in groups:
#    # mod1 + letter of group = switch to group
#    keys.append(
#        Key([mod], i.name, lazy.group[i.name].toscreen())
#    )
#
#    # mod1 + shift + letter of group = switch to & move focused window to group
#    keys.append(
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
#    )
#

# make a global layout definition
layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "AD69AF",
    "border_normal": "1D2330"
}


layouts = [
    # layout.Colums(),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Stack(num_stacks=2,**layout_theme),
    layout.TreeTab(**layout_theme)
]

widget_defaults = dict(
    font='Arial',
    fontsize=16,
    padding=3,
)
#### MOUSE CALLBACKS
def open_dmenu(qtile):
    qtile.spawn('dmenu_run')


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(),
                widget.GroupBox(),
                widget.AGroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("Sepp config", name="Seppis"),
                widget.Systray(),
                # widget.Volume(),
		widget.Volume(
			emoji=True,
        		mute_command=[
            			'amixer',
            			'-q',
            			'set',
            			'Master',
            			'toggle'],
        		),
                widget.Bluetooth(
                    mouse_callbacks = {"Button1": lambda: qtile.spawn("blueman-manager")},
                ),
                widget.Clock(
                    format='%a %d.%m (%b) %H:%M:%S',
                ),
            ],
            24,
        ),
        top=bar.Bar(
            [
                widget.Sep(),
                widget.Image(
                    filename = "~/.config/qtile/icons/python.png",
                    mouse_callbacks = {"Button1": lambda: qtile.spawn("dmenu_run")}
                ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.CurrentLayout(),
                widget.Net(interface="wlp115s0"),
                widget.Clock(
                    format='%a %d.%m.%Y %H:%M:%S',
                ),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
