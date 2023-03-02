import socket
import pickle

UDP_IP = "192.168.0.143"
UDP_PORT = 5005

MESSAGE = b"Hello, World!"

controller_dataframe = pickle.dumps({
    "btn1": 1,
    "btn2": -1,
    "btn3": 0.5,
    "btn4": -0.48
})

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % controller_dataframe)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.sendto(controller_dataframe, (UDP_IP, UDP_PORT))