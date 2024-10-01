import random

MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 14
MAX_CHANGE = 2
UP_BIAS = 0.5
DOWN_BIAS = 0.8
MIN_FRAMES = 20
MAX_FRAMES = 40
DISSOLVE_TIME = 0.4
PERC_UP_FRAMES = 0.7
FIREFLIES = 6
SEED = 10

random.seed(SEED)

def genrand(minval, maxval):
    return minval + random.random() * (maxval - minval)

for i in range(0, FIREFLIES):
    print(f"image firefly_v{i + 1}:")
    frames = random.randint(MIN_FRAMES, MAX_FRAMES)
    up_frames = round(frames * PERC_UP_FRAMES)
    brightness = 0
    for curr_frame in range(0, frames):
        print(f"    \"firefly b{brightness}\" with Dissolve({DISSOLVE_TIME})")
        print(f"    {DISSOLVE_TIME}")
        if brightness <= MIN_BRIGHTNESS:
            change = random.randint(1, MAX_CHANGE)
        elif brightness >= MAX_BRIGHTNESS:
            change = -random.randint(1, MAX_CHANGE)
        else:
            change = random.randint(1, MAX_CHANGE)
            if random.random() < 0.5:
                change = -change
            if curr_frame < up_frames:
                if change < 0 and random.random() < UP_BIAS:
                    change = -change
            else:
                if change > 0 and random.random() < DOWN_BIAS:
                    change = -change
        brightness += change
        if brightness < MIN_BRIGHTNESS:
            brightness = MIN_BRIGHTNESS
        elif brightness > MAX_BRIGHTNESS:
            brightness = MAX_BRIGHTNESS
    print("    repeat")