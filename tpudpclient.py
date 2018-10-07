# tpudpclient.py
# created on 4-10-2018
# ITIFN18 - Group 6

import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect to UDP TIME server')
    parser.add_argument('host', action="store", type=str, nargs='?', default="localhost",
                        help="Address of UDP TIME server")
    args = parser.parse_args()

    udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpclient.sendto(b'', (args.host, 37))
    reply, addr = udpclient.recvfrom(32)
    time = int.from_bytes(reply, byteorder='big')
    print(time)