# timeServer.py
# created on 7-10-2018
# ITIFN18 - Group 6

import abc
import socket
from timeServer import timeServer

class tcpTimeServer(timeServer):
    def __init__(self, conns=1):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 37))
        self.socket.listen(conns)
        self.protocol = "TCP"

    def send(self, res, addr):
        self.conn.sendall(res)

    def recv(self):
        self.conn, addr = self.socket.accept()
        data = self.conn.recv(0)
        return data, addr


if __name__ == "__main__":
    server = tcpTimeServer()
    print("Server started")
    server.listen()