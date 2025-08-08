just a loose collection of random scripts for personal use

## Index

+ [DBUS](#dbus)
+ [GObject](#gobject)
+ [GStream](#gstream)

## DBUS

### commands

some useful commands

| command | description |
| :------ | ----------- |
| `busctl` | introspect the D-Bus IPC bus |
| `busctl [--user] tree <service>` | prints the object tree of a service |
| `busctl [--user] introspect <service> <object path>` | introspect a service |
| `dbus-send` |  can be used to send signals |
| `qdbus6` | used to interact with dbus |
| `qdbusviewer6` | qt viewer of the current dbus |

### resources

list of some websites related to dbus

+ [archlinux wiki dbus entry](https://wiki.archlinux.org/title/D-Bus)
+ [freedesktop dbus docs](https://freedesktop.org/wiki/Software/dbus)
+ [freedesktop desktop dbus interfaces](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.impl.portal.ScreenCast.html)
+ [ageldama notifications snippets](https://gist.github.com/ageldama/d01c67208249c1f6980e894125042973)
+ [python3 dbus libraries](https://stackoverflow.com/questions/66916580/how-to-choose-and-use-a-python3-dbus-library-to-replace-a-dbus-send-call)
+ [pydbus repository](https://github.com/LEW21/pydbus)

## GObject

+ [pygobject](https://pygobject.gnome.org/)

## GStream

### commands

some useful commands

| command | description |
| :------ | ----------- |
| `gst-inspect-1.0 \| grep sink` | list of available sink elements |
| `gst-launch-1.0` | used to launch a pipeline |

### resources

list of some websites related to GStream

+ [gstream docs](https://gstreamer.freedesktop.org/documentation/?gi-language=python#GstPipeline)
+ [python gst tutorial](https://github.com/gkralik/python-gst-tutorial)
+ [gstreamer completion for zsh](https://github.com/CraigCarey/gstreamer-tab)
