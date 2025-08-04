import sys, time

# dbus
from dasbus.loop import EventLoop
from dasbus.connection import SessionMessageBus
from dasbus.typing import Variant


class Screencast:
    DESKTOP_PATH = "/org/freedesktop/portal/desktop"
    DESKTOP_IFACE = "org.freedesktop.portal.Desktop"

    SCREENCAST_IFACE = "org.freedesktop.portal.ScreenCast"

    # /org/freedesktop/portal/desktop/request/SENDER/TOKEN
    REQUEST_PATH = "/org/freedesktop/portal/desktop/request"
    REQUEST_IFACE = "org.freedesktop.portal.Request"

    # /org/freedesktop/portal/desktop/session/SENDER/TOKEN
    SESSION_PATH = "/org/freedesktop/portal/desktop/session"
    SESSION_IFACE = "org.freedesktop.portal.Session"

    request_token = 0
    session_token = 0

    def __init__(self):
        self.loop = EventLoop()
        self.bus = SessionMessageBus()
        self.desktop = self.bus.get_proxy(self.DESKTOP_IFACE, self.DESKTOP_PATH)

        print(self.get_sender())
        options = {
            "handle_token": Variant.new_string(self.get_request_token()),
            "session_handle_token": Variant.new_string(self.get_session_token()),
        }

        handle = self.desktop._get_member(self.SCREENCAST_IFACE, "CreateSession")(
            options
        )  # type: ignore

        options = {
            "handle_token": Variant.new_string(self.get_request_token()),
            "multiple": Variant.new_boolean(False),
            "types": Variant.new_uint32(3),
        }

        handle = self.desktop.SelectSources(self.get_session_path(), options)  # type: ignore

        options = {
            "handle_token": Variant.new_string(self.get_request_token()),
        }

        handle = self.desktop._get_member(self.SCREENCAST_IFACE, "Start")(
            self.get_session_path(), "test_window", options
        )  # type: ignore

        print(handle)

        request = self.bus.get_proxy(self.DESKTOP_IFACE, handle)
        # self.desktop._get_member(self.REQUEST_IFACE, "Response")

        self.session = self.bus.get_proxy(self.DESKTOP_IFACE, self.get_session_path())

        fd = self.desktop._get_member(self.SCREENCAST_IFACE, 'OpenPipeWireRemote')(self.get_session_path(), options)  # type: ignore
        print(fd)

    def callback(self, *a):
        print(*a)

    def get_sender(self) -> str:
        return self.bus.connection.get_unique_name()[1:].replace(".", "_")  # type: ignore

    def new_request_token(self):
        self.request_token += 1

    def new_session_token(self):
        self.session_token += 1

    def get_request_token(self):
        return "u%s" % self.request_token

    def get_session_token(self):
        return "u%s" % self.session_token

    def get_request_path(self):
        return f"{self.REQUEST_PATH}/{self.get_sender()}/{self.get_request_token()}"

    def get_session_path(self):
        return f"{self.SESSION_PATH}/{self.get_sender()}/{self.get_session_token()}"

    def run(self):
        self.loop.run()

    def exit(self):
        if self.session is not None:
            self.session.close()  # type: ignore
        self.loop.quit()


if __name__ == "__main__":
    sc = Screencast()
    try:
        sc.run()
    except KeyboardInterrupt:
        sc.exit()
    finally:
        sc.exit()
