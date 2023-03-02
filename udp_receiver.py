import socket
import pickle 
from pprint import pprint

UDP_IP = "192.168.0.143"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    controller_dataframe = pickle.loads(data)
    print("received message: ", end ="\t")
    pprint(controller_dataframe)