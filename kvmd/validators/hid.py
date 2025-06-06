# ========================================================================== #
#                                                                            #
#    KVMD - The main PiKVM daemon.                                           #
#                                                                            #
#    Copyright (C) 2018-2024  Maxim Devaev <mdevaev@gmail.com>               #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


from typing import Any

from ..keyboard.mappings import WEB_TO_EVDEV
from ..mouse import MOUSE_TO_EVDEV

from ..mouse import MouseRange
from ..mouse import MouseDelta

from . import check_string_in_list

from .basic import valid_number


# =====
def valid_hid_keyboard_output(arg: Any) -> str:
    return check_string_in_list(arg, "Keyboard output", ["usb", "ps2", "disabled"])


def valid_hid_mouse_output(arg: Any) -> str:
    return check_string_in_list(arg, "Mouse output", ["usb", "usb_win98", "usb_rel", "ps2", "disabled"])


def valid_hid_key(arg: Any) -> str:
    return check_string_in_list(arg, "Keyboard key", WEB_TO_EVDEV, lower=False)


def valid_hid_mouse_move(arg: Any) -> int:
    arg = valid_number(arg, name="Mouse move")
    return MouseRange.normalize(arg)


def valid_hid_mouse_button(arg: Any) -> str:
    return check_string_in_list(arg, "Mouse button", MOUSE_TO_EVDEV)


def valid_hid_mouse_delta(arg: Any) -> int:
    arg = valid_number(arg, name="Mouse delta")
    return MouseDelta.normalize(arg)
