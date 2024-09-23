# A robot has been given a list of movement instructions. Each instruction is
# either _left_, _right_, _up_ or _down_, followed by a distance to move. The
# robot starts at [0, 0]. You want to calculate where the robot will end up and
# return its final position as a list. For example, if the robot is given the
# instructions `["right 10", "up 50", "left 30", "down 10"]`, it will end up 20
# left and 40 up from where it started, so you should return `[-20, 40]`.

# Write your function here.
def track_robot(instructions):
    x = 0
    y = 0

    if len(instructions) == 0:
        return [x, y]

    for m in instructions:
        mSplit = m.split(' ')
        if mSplit[0] == 'right':
            x += int(mSplit[1])
        elif mSplit[0] == 'left':
            x -= int(mSplit[1])
        elif mSplit[0] == 'up':
            y += int(mSplit[1])
        elif mSplit[0] == 'down':
            y -= int(mSplit[1])

    return [x, y]

print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]
