print(f'[Module] obstacles loaded.')

import sys
if 'turtle' in sys.argv:
    import turtle
    obstacle = turtle.Turtle()
import random

blocked = []
blocked_x = []
blocked_y = []

def ShowObstacles():
    if blocked != []:
        print(f'There are some obstacles:')
        for x in range(len(blocked)):
            print(f'- At position {blocked[x][0]},{blocked[x][1]} (to {blocked[x][0] + 4},{blocked[x][1] + 4}).')

def CreateObstacle(x,y):
    obstacle.hideturtle()
    obstacle.speed(0)
    obstacle.penup()
    obstacle.goto(x,y)
    obstacle.left(90)
    obstacle.pendown()
    obstacle.begin_fill()
    for _ in range(4):
        obstacle.fd(4)
        obstacle.right(90)
    obstacle.end_fill()

def FillWithObstacles():
    ran = random.randint(0,10)
    for _ in range(ran):
        ran_x = random.randint(-98,98)
        ran_y = random.randint(-198,198)
        blocked.append((ran_x,ran_y))
        if 'turtle' in sys.argv:
            CreateObstacle(ran_x,ran_y)

def get_obstacles():
    return blocked

def GetBlockedPositions():
    global blocked_x,blocked_y
    blocked_x = []
    blocked_y = []
    for i in range(len(blocked)):
        for j in range(4):
            blocked_x.append(blocked[i][0]+j)
            blocked_y.append(blocked[i][1]+j)

def IsValidPos(x1,y1,x2,y2):
    passed = False
    if x1 == x2:
        if not is_position_blocked(x2,y2): passed = True
        if not is_path_blocked(x1,y1,x2,y2): passed = True
    elif y1 == y2:
        if not is_position_blocked(x2,y2): passed = True
        if not is_path_blocked(x1,y1,x2,y2): passed = True
    return passed

def is_position_blocked(x,y):
    GetBlockedPositions()
    print(x, '  --  ', blocked_x)
    print(y, '  --  ', blocked_y)
    if x in blocked_x and y in blocked_y: return True
    return False

def is_path_blocked(x1,y1,x2,y2):
    if x1 == x2:
        steps = y2-y1
        for _ in range(steps):
            if _ + y1 in blocked_y: return True
    if y1 == y2:
        steps = x2-x1
        for _ in range(steps):
            if _ + x1 in blocked_x: return True
    return False