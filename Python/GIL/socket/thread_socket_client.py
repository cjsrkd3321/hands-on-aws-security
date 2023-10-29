# https://github.com/r4victor/pbts13_gil/blob/master/effect2_client.py

import socket
import time
from threading import Thread


requests_per_second = 0


def monitor():
    global requests_per_second
    while True:
        time.sleep(1)
        print(requests_per_second, "reqs/sec")
        requests_per_second = 0


def connect(host="127.0.0.1", port=33333):
    global requests_per_second

    sock = socket.socket()
    sock.connect((host, port))

    while True:
        sock.sendall(b"0")
        sock.recv(4096)
        requests_per_second += 1


if __name__ == "__main__":
    Thread(target=monitor).start()
    while True:
        try:
            connect()
        except ConnectionError:
            time.sleep(0.1)
