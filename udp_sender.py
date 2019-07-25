import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 20401

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = b'\x7e\x7d'
sock.sendto(data, (UDP_IP, UDP_PORT))