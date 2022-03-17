#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser= optparse.OptionParser()

    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")

    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac, use --help for more info.")
    return options


def change_mac(interface,new_mac):
    print("[+] Changing MAC address for "+interface+" to "+new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface,options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig",options.interface])

regex = r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w'
mac_address_search_result = re.search(regex, str(ifconfig_result))

if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[-] Could not read MAC address.")

