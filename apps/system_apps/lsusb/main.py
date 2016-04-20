menu_name = "lsusb"

from ui import Menu, Printer

import lsusb

def ellipsize(string, length):
    ellipsis = "..."
    if len(string) <= length:
        return string
    string = string[:(length-len(ellipsis))]
    return string+ellipsis

def show_devices():
    menu_contents = []
    usb_devices = lsusb.lsusb()
    for bus, dev, vid_pid, name in usb_devices:   
        ell_name = ellipsize(name, o.cols)
        menu_contents.append([["{}{},{}".format(bus, dev, vid_pid), ell_name], lambda x=name: Printer(x, i, o, skippable=True)])
    Menu(menu_contents, i, o, entry_height=2).activate()


#Some globals for pyLCI
callback = show_devices
#Some globals for us
i = None
o = None


def init_app(input, output):
    global i, o
    i = input; o = output

