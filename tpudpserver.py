# tpudpserver.py
# created on 4-10-2018
# ITIFN18 - Group 6

import abc
import socket
from timeServer import timeServer

class udpTimeServer(timeServer):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 37))
        self.protocol = "UDP"

    def send(self, res, addr):
        self.socket.sendto(res, addr)

    def recv(self):
        return self.socket.recvfrom(1)

if __name__ == "__main__":
    server = udpTimeServer()
    print("Server started")
    server.listen()