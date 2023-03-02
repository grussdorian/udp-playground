import pickle 
import sys

left_y = -0.5
left_x = -0.5
right_x = -0.4
right_y = -0.3
L2 = -0.3
R2 = -0.4
R1 = -0.6
L1 = -0.6
dpady = -0.5
dpadx = -0.3
x = -9.3
square = -0.4
circle = -0.3
triangle = -0.2
MESSAGE_RATE = 20

msg = {
            "ly": left_y,
            "lx": left_x,
            "rx": right_x,
            "ry": right_y,
            "L2": L2,
            "R2": R2,
            "R1": R1,
            "L1": L1,
            "dpady": dpady,
            "dpadx": dpadx,
            "x": x,
            "square": square,
            "circle": circle,
            "triangle": triangle,
            "message_rate": MESSAGE_RATE,
        }

dataframe = pickle.dumps(msg)
print(sys.getsizeof(dataframe))