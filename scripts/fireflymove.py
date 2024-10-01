import random
import math

LEFT = 0.0
RIGHT = 1.0
BOTTOM = 0.0
TOP = 1.0
KNOTS = 6
ITERATIONS = 10
MIN_TIME = 12.0
MAX_TIME = 20.0
MIN_DIST = 0.05
MAX_DIST = 0.2
MAX_ANGLE_ATTEMPTS = 25
SEED = 100
FIREFLIES = 6

random.seed(SEED)

def genrand(minval, maxval):
    return minval + random.random() * (maxval - minval)

for a in range(0, FIREFLIES):
    print(f"show firefly_v{a + 1}:")
    #print(f"transform firefly_move{a + 1}:")
    last_point = [genrand(LEFT, RIGHT), genrand(BOTTOM, TOP)]
    print(f"    anchor (0.5,0.5) pos ({round(last_point[0], 2)},{round(last_point[1], 2)})")
    print("    block:")
    for i in range(0, ITERATIONS):
        t = genrand(MIN_TIME, MAX_TIME)
        pos = f"pos ({round(last_point[0], 2)},{round(last_point[1], 2)})"
        knots = ""
        for j in range(0, KNOTS):
            find_attempts = 0
            while find_attempts < MAX_ANGLE_ATTEMPTS:
                angle = genrand(0, math.pi * 2)
                dist = genrand(MIN_DIST, MAX_DIST)
                xpos = math.cos(angle) * dist + last_point[0]
                ypos = math.sin(angle) * dist + last_point[1]
                if xpos >= LEFT and xpos <= RIGHT and ypos >= BOTTOM and ypos <= TOP:
                    knots += f" knot ({round(xpos, 2)},{round(ypos, 2)})"
                    last_point[0] = xpos
                    last_point[1] = ypos
                    break
                else:
                    find_attempts += 1
            if find_attempts >= MAX_ANGLE_ATTEMPTS:
                print(f"ERROR: Could not locate additional point after ({round(last_point[0], 2)}, {round(last_point[1], 2)})")
        print(f"        ease {round(t, 2)} {pos}{knots}")
    print("        repeat")
    print()