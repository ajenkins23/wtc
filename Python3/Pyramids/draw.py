

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    slist = ['pyramid', 'square', 'triangle', 'diamond']
    while True:
        shape = input("Shape?: ")
        shape = shape.lower()
        if len(shape) == 0:
            continue
        if shape in slist:
            break
        else:
            print("Please choose one of the following : " + " ".join(slist))
            continue
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        size = input("Height?: ")
        if not size.isdigit():
            continue
        if len(size) == 0:
            print("Please choose a number...")
            continue
        if int(size) > 80:
            print("Chosen number is larger than 80...")
            continue
        if int(size) < 0:
            print ("Please choose a positive number...")
            continue
        if int(size) >= 0 and int(size) <= 80:
            break
    return int(size)

def draw_diamond(height, outline):
    i = int(height)
    space = i
    pira = 1
    oline = 1
    if outline == False:
        for x in range(i):
            print(' ' * space + '*' * pira)
            i = i - 1
            pira = pira + 2
            space = space - 1
        for x in range(int(height) + 1):
            print(" " * space + '*' * pira)
            pira = pira - 2
            space = space + 1
    else:
        print(" " * (space + 1) + "*")
        for x in range(i - 1):
            print(' ' * space + '*' + " " * oline + "*")
            space = space - 1
            oline = oline + 2
        for x in range(int(height)):
            print(" " * space + '*' + " " * oline + "*" )
            oline = oline - 2
            space = space + 1
        print(" " * space + "*")
        

# TODO: Step 2
def draw_pyramid(height, outline):
    i = int(height)
    space = int(height) - 1
    pira = 1
    oline = 1
    if outline == False:
        for x in range(i):
            print(' ' * space + '*' * pira)
            i = i - 1
            pira = pira + 2
            space = space - 1
    else:
        print(" " * space + "*")
        space = space - 1
        for x in range(i - 2):
            print(' ' * space + '*' + " " * oline + "*")
            i = i - 1
            pira = pira + 2
            space = space - 1
            oline = oline + 2
        print("*" * ((int(height) * 2) - 1))
        



# TODO: Step 3
def draw_square(height, outline):
    i = int(height)
    sheight = int(height)
    if outline == False:
        for x in range(i):
            print("*" * sheight)
    else:
        print("*" * sheight)
        for x in range(i - 2):
            print("*" + (' ' * (sheight - 2)) + "*")
        if sheight > 1:
            print("*" * sheight)




# TODO: Step 4
def draw_triangle(height, outline):
    i = int(height)
    theight = 1
    space = 1
    if outline == False:
        for x in range(i):
            print("*" * theight)
            i = i - 1
            theight = theight + 1
    else:
        if i <= 3:
            for x in range(i):
                print("*" * theight)
                i = i - 1
                theight = theight + 1
        elif i >= 4:
            for x in range(2):
                print("*" * theight)
                theight = theight + 1
            for x in range(i - 3):
                print("*" + (" " * space) + "*")
                space = space + 1
            print("*" * int(height))


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'square':
        draw_square(height, outline)
    if shape == 'triangle':
        draw_triangle(height, outline)
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    if shape == 'diamond':
        draw_diamond(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline = input("To draw outline, press 'y'. To draw Solid, press 'n' : ")
        if len(outline) == 0:
            print("Please enter 'y' or 'n'...")
            continue
        if outline == 'y' or outline == 'Y':
            return True
        if outline == 'n' or outline == 'N':
            return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

