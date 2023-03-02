import socket
import threading

# Define the IP address and port number to use
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Create a socket object for sending and receiving UDP packets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a subscription function that binds a subscriber to the specified topic
def subscribe(topic):
    sock.bind((UDP_IP, UDP_PORT))
    print("Subscribed to topic: " + topic)

    # Continuously receive and print messages from the publisher
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message: " + str(data))

# Create a publish function that sends a message to all subscribers of the specified topic
def publish(topic, message):
    print("Publishing message to topic: " + topic)
    sock.sendto(message, (UDP_IP, UDP_PORT))

# Create a thread for publishing messages
class PublisherThread(threading.Thread):
    def __init__(self, topic, message):
        threading.Thread.__init__(self)
        self.topic = topic
        self.message = message
    
    def run(self):
        publish(self.topic, self.message)

# Example usage:
subscribe_thread = threading.Thread(target=subscribe, args=("my_topic",))
subscribe_thread.start()

publish_thread = PublisherThread("my_topic", b'Hello, subscribers!')
publish_thread.start()
