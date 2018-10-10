# TIME protocol clients & servers

Simple Python implementation of TIME protocol clients and servers as described in ([RFC868](https://tools.ietf.org/html/rfc868)).

# Usage

* Tested on miniconda's Python 3.7
* run server (TCP) `python3 tptcpserver.py` or (UDP) `python3 tpudpserver.py`
* run client (TCP) `python3 tptcpclient.py <host>` or (UDP) `python3 tpudpclient.py <host>`
* default `<host>` is set to `localhost`
