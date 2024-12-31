# https://github.com/r4victor/pbts13_gil/blob/master/effect2_server_threads.py

from threading import Thread
import socket


def compute():
    n = 0
    while True:
        n += 1
        n -= 1


def run_server(host="127.0.0.1", port=33333):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
        client_sock, addr = sock.accept()
        print("Connection from", addr)
        Thread(target=handle_client, args=(client_sock,)).start()


def handle_client(sock):
    while True:
        received_data = sock.recv(4096)
        if not received_data:
            break
        sock.sendall(received_data)

    print("Client disconnected:", sock.getpeername())
    sock.close()


def main():
    for _ in range(10):
        Thread(target=compute).start()
    run_server()


if __name__ == "__main__":
    main()
