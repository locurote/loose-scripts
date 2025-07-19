import sys

# GObjects
from gi.repository import GLib  # pyright: ignore[reportMissingModuleSource]

# dbus
from pydbus import SessionBus


def main(*args):
    bus = SessionBus()

    # Desktop
    # dev = bus.get("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop")
    # dev.SelectSources('')

    dev = bus.get(
        "org.freedesktop.FileManager1",
        "/org/freedesktop/FileManager1"
    )

    dev.ShowFolders(["/home/linux", "/home/linux/Downloads"], "sasss")
    # help(dev)


def exit():
    if loop is not None:
        loop.quit()
    sys.exit()


if __name__ == "__main__":
    global loop
    # loop = GLib.MainLoop()

    main(sys.argv)

    try:
        
    except KeyboardInterrupt:
        exit()
