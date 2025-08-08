import gi

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib # type: ignore # noqa: E402


def main():
    global pipeline
    global loop

    pipeline = new_pipeline_elementfactory()

    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect("message", message_handler)

    pipeline.set_state(Gst.State.PLAYING)

    loop = GLib.MainLoop()

    try:
        loop.run()
    finally:
        terminate()


def message_handler(bus, msg: Gst.Message):
    # stop on end of stream
    if msg.type == Gst.MessageType.EOS:
        terminate()


def terminate():
    pipeline.set_state(Gst.State.NULL)
    loop.quit()


def new_pipeline_strparsing():
    # Initialize GStreamer
    Gst.init(None)

    # Create pipeline using parse_launch
    pipeline = Gst.parse_launch("videotestsrc ! videoconvert ! autovideosink")

    return pipeline


def new_pipeline_elementfactory():
    # Initialize GStreamer
    Gst.init(None)

    # Create elements
    src = Gst.ElementFactory.make("videotestsrc", "src")
    conv = Gst.ElementFactory.make("videoconvert", "conv")
    sink = Gst.ElementFactory.make("autovideosink", "sink")

    # Create pipeline
    pipeline = Gst.Pipeline(name="test-pipeline")

    # Check elements were created
    if src is None or conv is None or sink is None:
        raise Exception("Error creating elements")

    # Add elements to pipeline
    pipeline.add(src)
    pipeline.add(conv)
    pipeline.add(sink)

    # Link elements
    if not src.link(conv) or not conv.link(sink):
        raise Exception("Elements could not be linked")

    return pipeline


if __name__ == "__main__":
    main()
