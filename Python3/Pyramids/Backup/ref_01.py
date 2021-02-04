

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    sList = ["pyramid", "square", "triangle"]
    while True:
        shape_param = input("Shape?: ")
        shape_param = shape_param.lower()
        if len(shape_param) == 0:
            continue
        if shape_param in sList:
            break
        else:
            continue
    return shape_param


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height_param = input("Height?: ")
        if not height_param.isdigit():
            continue
        height_param = int(height_param)
        if height_param >= 0 and height_param <= 80:
            break
    return height_param


# TODO: Step 2
def draw_pyramid(height, outline):
    size = int(height)
    if not outline:
        x = 0
        y = 1
        while x in range(size):
            if x < 1:
                print(' ' * (size - y) + "*" * y)
            if x == 1 or x > 1 and x < size:
                print(' ' * (size - y) + "*" * (y + x))
            x = x + 1
            y = y + 1
    x = 0
    y = 1
    j = -1    
    if outline:
        while x in range(size):
            if x < 1:
                print(" " * (size - y) + "*" * y)
            if x == 1 or x > 1 and x < (size - 1):
                print(" " * (size - y) + "*" + " " * (x + j) + "*")
            if  x == size - 1:
                print("*" * (y + x))
            x = x + 1
            y = y + 1
            j = j + 1     


# TODO: Step 3
def draw_square(height, outline):
    size = int(height)
    x = 0
    y = 0
    # Solid Square
    if not outline:
        for x in range(size):
            print("*" * size)
    # Outline Square
    elif outline:
        while x in range(size):
            if x == 0:
                print("*" * size)
            while y > 0 and y < size - 1:
                print("*" + " " * (size -2) + "*")
                y = y + 1
            if x == size - 1:
                print("*" * size)
            x = x + 1
            y = y + 1
    
	

# TODO: Step 4
def draw_triangle(height, outline):
    size = int(height)
    x = 0
    y = 1
    if not outline:
        while x in range(size):
            print("*" * y)
            x = x + 1
            y = y + 1
    x = 0
    y = 1
    if outline:
        while x in range(size):
            if x <= 1:
                print("*" * y)
            if x > 1 and x < (size - 1):
                print("*" + " " * (x - 1) + "*")
            if x == size - 1:
                print("*" * size)
            x = x + 1
            y = y + 1


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline_param = input("Outline only? (Y/N): ")
        if len(outline_param) == 0:
            continue
        if outline_param.lower == 'y':
            return True
        if outline_param.lower == 'n':
            break
    return False



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)
