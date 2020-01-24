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

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from libqtile.log_utils import logger

from typing import List  # noqa: F401
import os
import subprocess
import time

mod = "mod4"

# https://wiki.archlinux.org/index.php/IBus
# For some applications, e.g. Emacs, ibus doesn't work without these.
# There are only two here as in GNOME.
os.environ["QT_IM_MODULE"] = "ibus"
os.environ["XMODIFIERS"] = "@im=ibus"


# @hook.subscribe.screen_change
def set_screens(qtile, event):
    logger.warning("screen change event")
    xrandr_state = subprocess.check_output(["xrandr"])
    if b"DP-1 connected" in xrandr_state:
        xrandr_command = "xrandr --output eDP-1 --off --output DP-1 --auto"
    else:
        xrandr_command = "xrandr --output eDP-1 --auto"  # FIXME why this fails
    subprocess.call(xrandr_command.split())
    qtile.cmd_restart()


def build_widgets():
    widgets = [
        widget.Prompt(prompt="🐶 "),
        widget.CurrentLayout(),
        widget.Spacer(width=10),
        widget.GroupBox(disable_drag=True),
        widget.Systray(),
        widget.Volume(fmt="🔉 {}"),
        widget.Notify(fmt="💡 {}"),
    ]

    if os.path.isdir("/sys/class/power_supply/BAT0"):
        widgets.append(widget.Battery(
            fmt="🔋 {}",
            format='{char} {percent:2.0%} {hour:d}:{min:02d}',
        ))

    widgets.append(widget.Clock(
        fmt="☯ {}",
        format='%m-%d %a %H:%M %p',
        update_interval=60))
    return widgets

keys = [
    # Switch between windows in current stack pane(only pointer is moved around)
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack(windows are sheffuled)
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Only available for bsp, columns, and stack layout.
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    Key([mod], "Return", lazy.spawn("urxvt256c-ml")),
    Key([], "Scroll_Lock", lazy.spawn("i3lock -d")),
    Key([mod], "grave", lazy.screen.toggle_group()),
    Key([mod], "e", lazy.spawn("emacsclient --eval '(make-frame-command)'")),
    Key([mod, "shift"], "e", lazy.spawn("emacs")),
    Key([mod], "c", lazy.spawn("google-chrome")),
    Key([mod], "z", lazy.spawn("zeal")),

    # Toggle between different layouts as defined below
    Key([mod], "Right", lazy.next_layout()),
    Key([mod], "Left", lazy.prev_layout()),

    Key([mod], "x", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "f", lazy.window.toggle_floating()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # mod + shift + letter of group = move focused window to that group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

emacs_purple = '#7359B5'
border_width = 1
border = dict(
    border_focus=emacs_purple,
    border_width=border_width
)

layouts = [
    layout.Tile(add_after_last=True, **border),
    layout.Max(),
    layout.MonadWide(**border, ratio=0.618),
    layout.MonadTall(**border),
    layout.Stack(num_stacks=2),
    layout.Columns(**border),
    # layout.Bsp(name="bsp", margin=20, **border),
    # layout.Matrix(name="matrix", **border),
    # layout.MonadWide(name="monadwide", **border),
    # layout.RatioTile(name="ratiotile", **border),
    # layout.TreeTab(name="treetab", border_width=border_width),
    # layout.VerticalTile(name="verticaltile", **border),
    # layout.Zoomy(name="zoomy"),
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(build_widgets(), 28),
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
dgroups_app_rules = []  # type: List

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
    ],
    **border
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


def enable_tap_to_click():
    # Enable "Tap to Click"
    # https://www.reddit.com/r/i3wm/comments/516e8c/tap_to_click_touchpad/d79onal
    # Currently it's system specific.
    device = 'DLL0665:01 06CB:76AD Touchpad'
    try:
        id = subprocess.check_output(["xinput", "list", "--id-only", device],
                                     encoding='utf-8')
        id = id.strip()
    except Exception:
        return
    subprocess.run(["xinput", "set-prop", id, "317", "1"])
    subprocess.run(["xinput", "set-prop", id, "318", "1"])


# callback entrance, e.g. def main(qtile_instance): pass
def main(qtile):
    subprocess.run(["ibus-daemon", "-drx"])

    # Set a wallpaper
    subprocess.run(["feh", "--bg-fill",
                    "/usr/share/backgrounds/f29/default/standard/f29.png"])

    enable_tap_to_click()
