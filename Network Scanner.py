#!/usr/bin/env python3

import argparse
import socket

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True, help="Target IP/IP range.")
    options = parser.parse_args()
    return options

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target_ip, port))
        print("[+] Port " + str(port) + " is open")
        sock.close()
    except:
        pass

options = get_arguments()
target_ip = options.target
for port in range(1, 1001):
    scan_port(target_ip, port)