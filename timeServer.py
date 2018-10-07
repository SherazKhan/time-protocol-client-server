# timeServer.py
# created on 7-10-2018
# ITIFN18 - Group 6

import datetime as dt
import socket
import abc

class timeServer(metaclass=abc.ABCMeta):
    def listen(self):
        """Listen for connections and send back
           current TIME protocol time if received
           packet is empty.
        """
        while 1:
            print("\nWaiting for " + self.protocol + " packet")
            data, addr = self.recv()
            print("Packet received: " + str(data) + " from " + str(addr))

            # check if packet is empty
            if data == b'':
                time = self.time()
                print("Time: " + str(time))

                # save time as 32-bit integer
                res = time.to_bytes(4, byteorder='big')
                self.send(res, addr)
                print("Time sent back to " + str(addr))
            else:
                print( self.protocol + " packet was not empty, not responding")

    def time(self):
        """Return TIME protocol time."""
        start_time = dt.datetime(1900,1,1,0,0,0)
        now = dt.datetime.now()
        return int((now-start_time).total_seconds())

    @abc.abstractmethod
    def send(self, res, addr):
        """Send response message to the client."""

    @abc.abstractmethod
    def recv(self):
        """Receive request send by client."""