# tpudpclient.py
# created on 4-10-2018
# ITIFN18 - Group 6

import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect to TCP TIME server')
    parser.add_argument('host', action="store", type=str, nargs='?', default="localhost",
                        help="Address of TCP TIME server")
    args = parser.parse_args()
    
    tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpclient.connect((args.host, 37))
    tcpclient.sendall(b'')
    reply = tcpclient.recv(32)
    tcpclient.close()
    time = int.from_bytes(reply, byteorder='big')
    print(time)