#! /usr/bin/python3

import argparse
import re
import tempfile
import os

CONFIG_FILE_PATH = "/etc/create_ap/default.conf"

def read_config():
    with open(CONFIG_FILE_PATH, "r") as f:
        return f.read()

def write_config(config):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(config.encode('utf-8'))
        return f.name

def replace_config_item(config, item, value):
    return re.sub("(%s)=.*" % item, "\\1=%s" % value, config)

def replace_config_items(config, values):
    for item in values:
        config = replace_config_item(config, item, values[item])
    return config

def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def main():
    parser = argparse.ArgumentParser(description='Create Wi-Fi access point')
    parser.add_argument('method', help='The sharing method (bridge, nat, none)')
    parser.add_argument('wlan_iface', help='The wireless device to use (wlanX)')
    parser.add_argument('net_iface', help='The interface with network access (ethX)', default='', nargs='?')

    args = parser.parse_args()

    values = {
            "WIFI_IFACE": args.wlan_iface,
            "INTERNET_IFACE": args.net_iface,
            "SHARE_METHOD": args.method
            }

    config = read_config()
    config = replace_config_items(config, values)
    temp_file_path = write_config(config)

    print("Temp config file: %s" % temp_file_path)

    create_ap_path = which('create_ap')
    os.execv(create_ap_path, [create_ap_path, '--config', temp_file_path])


main()
