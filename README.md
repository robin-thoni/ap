ap.py
=====


[ap.py](ap.py) is a wrapper for [create_ap.py](https://github.com/oblique/create_ap).
It allows you to run a simple access point using a predefined configuration in different environments easily.


Installation
----------------

Copy [default.conf](default.conf) to `/etc/create_ap/default.conf`
You can edit [default.conf](default.conf) to match your needs. For a basic setup, just edit `SSID` and `PASSPHRASE`.
`SHARE_METHOD`, `WIFI_IFACE` and `INTERNET_IFACE` fields will be overwritten at runtime with  [ap.py](ap.py) arguments.

Additionally, you can copy [ap.py](ap.py) to your path (/usr/local/bin/ap, for example)


Usage
--------

- Share your ethernet (eth0) network by forwarding requests (aka bridge) from your wireless interface (wlan0):
`ap bridge wlan0 eth0`
All requests done by a wireless device connected on wlan0 will be forwarded to your ethernet network. No need for local DHCP server.

- Share your ethernet (eth0) network by rewriting requests (aka NAT) from your wireless interface (wlan0):
`ap nat wlan0 eth0`
All requests done by a wireless device connected on wlan0 will be rewritten and sent as if your computer sent them. A local DHCP server is needed but will be setup by [create_ap.py](https://github.com/oblique/create_ap).

- Share your wireless network (wlan0) to another wireless interface (wlan1) (useful if your wireless network does not allow clients communication):
`ap nat wlan1 wlan0`
All requests done by a wireless device connected on wlan0 will be rewritten and sent as if your computer sent them. A local DHCP server is needed but will be setup by [create_ap.py](https://github.com/oblique/create_ap). **Please note that two wireless interfaces can not be bridged.**

- Create an 'empty' wireless (wlan0) network without internet access (allow devices to comunicate to each other):
`ap none wlan0`
A local DHCP server is needed but will be setup by [create_ap.py](https://github.com/oblique/create_ap). 
