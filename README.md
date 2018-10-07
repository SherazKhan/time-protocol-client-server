# time-server

Simple python implementation of TIME protocol server ([RFC868](https://tools.ietf.org/html/rfc868)).

# Usage

* You need Python 3.6+
* run server (TCP) `python3 tptcpserver.py` or (UDP) `python3 tpudpserver.py`
* run client (TCP) `python3 tptcpclient.py <host>` or (UDP) `python3 tpudpclient.py <host>`
* default `<host>` is set to `localhost`
