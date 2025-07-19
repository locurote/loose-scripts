import sys

# GObjects
from gi.repository import GLib  # pyright: ignore[reportMissingModuleSource]

# dbus
from pydbus import SessionBus


def main(*args):
    bus = SessionBus()

    # Proxy Object
    dev = bus.get("org.freedesktop.Notifications", "/org/freedesktop/Notifications")

    # help(dev)

    #  Notify(
    #  |    self,
    #  |    app_name: 's',
    #  |    replaces_id: 'u',
    #  |    app_icon: 's',
    #  |    summary: 's',
    #  |    body: 's',
    #  |    actions: 'as',
    #  |    hints: 'a{sv}',
    #  |    timeout: 'i',
    #  |
    #  |) -> 'u'

    dev.Notify("hello-me", 1222321, "", "title", "body", "", "", 10000)


def exit():
    loop.quit()
    sys.exit()


if __name__ == "__main__":
    global loop
    loop = GLib.MainLoop()

    main(sys.argv)

    try:
        loop.run()
    except KeyboardInterrupt:
        exit()
