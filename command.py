import socket
import pickle
import time

UDP_IP = "192.168.0.185"
UDP_PORT = 6666
UDP_PORT2 = 9999

MESSAGE = {
    "R1": 1,
    "x": 2,
    "L1": 1,
    "ly": -0.48,
    "lx": -0.48,
    "rx": -0.48,
    "ry": -0.3,
    "message_rate": 50,
    "dpady": 0.5,
    "dpadx": 0.5,
}
controller_dataframe = pickle.dumps(MESSAGE)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
while True:

    sock.sendto(controller_dataframe, (UDP_IP, UDP_PORT))
    sock.sendto(controller_dataframe, (UDP_IP, UDP_PORT2))
    print("Message sent")
    time.sleep(2)