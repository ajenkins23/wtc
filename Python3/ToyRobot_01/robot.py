
def moveInSquare(size):
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def moveInRectangle(length, width):
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def moveInCircle(degrees):
    print("Moving in a circle")
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def moveSquareDancing(size):
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        moveInSquare(20)

def moveCropCircles(length, degrees):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        moveInCircle(degrees)

# TODO: Decompose into functions
def move():
    size = 10
    length = 20
    width = 10
    degrees = 1

    moveInSquare(size)
    moveInRectangle(length, width)
    moveInCircle(degrees)

    moveSquareDancing(size)
    moveCropCircles(length, degrees)

def robot_start():
    move()

if __name__ == "__main__":
    robot_start()
