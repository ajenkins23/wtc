def CreateRobot():
    class Robot():
        pos_x, pos_y, pos_dir = 0, 0, 0
        name, name_dot, command, prompt, instruction, name_arrow, steps = '', '', '', '', '', '',''
        val_inputs, functions = [], []
        call_func = {}
        rb_on = True
    rb = Robot
    rb.name = input('What do you want to name your robot? ')
    rb.name_dot = rb.name+': '
    rb.name_arrow = ' > '+rb.name+' '
    rb.prompt = rb.name_dot + 'What must I do next? '
    rb.val_inputs = ['off','help','forward','back','right','left','sprint']
    rb.functions = [RobotOff,RobotHelp,RobotMove,RobotMove,RobotMove,RobotMove,RobotMove]
    for input_ in range(len(rb.val_inputs)):
        rb.call_func.update({rb.val_inputs[input_]: rb.functions[input_]})
    return rb

def RobotHelp(rb):
    print('''I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands''')

def RobotOff(rb):
    rb.rb_on = False
    print(rb.name_dot+'Shutting down..')

def IsInRange(rb):
    if rb.pos_dir == 0:
        if rb.pos_y + int(rb.steps) > 200 or rb.pos_y + int(rb.steps) < -200:
            return False
    elif rb.pos_dir == 1:
        if rb.pos_x + int(rb.steps) > 100 or rb.pos_x + int(rb.steps) < -100:
            return False
    elif rb.pos_dir == 2:
        if rb.pos_y - int(rb.steps) > 200 or rb.pos_y - int(rb.steps) < -200:
            return False
    elif rb.pos_dir == 3:
        if rb.pos_x - int(rb.steps) > 100 or rb.pos_x - int(rb.steps) < -100:
            return False
    return True

def RobotMove(rb):
    move_pos = ['forward','back','sprint']
    move_dir = ['right','left']
    if rb.instruction in move_pos:
        if IsInRange(rb):
            if rb.instruction != 'sprint':
                print(rb.name_arrow +'moved '+rb.instruction+' by '+rb.steps.strip('-')+' steps.')
            else:
                print(rb.name_arrow +'moved forward by '+rb.steps.strip('-')+' steps.')
            if rb.pos_dir == 0:
                rb.pos_y += int(rb.steps)
            elif rb.pos_dir == 1:
                rb.pos_x += int(rb.steps)
            elif rb.pos_dir == 2:
                rb.pos_y -= int(rb.steps)
            elif rb.pos_dir == 3:
                rb.pos_x -= int(rb.steps)
            if rb.instruction == 'sprint':
                rb.steps = int(rb.steps) - 1
                rb.steps = str(rb.steps)
                if rb.steps != '0': 
                    return RobotMove(rb)
        else:
            print(rb.name_dot+'Sorry, I cannot go outside my safe zone.')
    elif rb.command in move_dir:
        print(rb.name_arrow +'turned '+rb.instruction+'.')
        if rb.instruction == 'right':
            rb.pos_dir += 1
            if rb.pos_dir == 4:
                rb.pos_dir = 0
        elif rb.instruction == 'left':
            rb.pos_dir -= 1
            if rb.pos_dir == -1:
                rb.pos_dir = 3
    print(rb.name_arrow+'now at position ('+str(rb.pos_x)+','+str(rb.pos_y)+').')

def GetCommand(rb):
    rb.command = input(rb.prompt).strip()
    if rb.command.split()[0].lower() not in rb.val_inputs:
        print(rb.name_dot + 'Sorry, I did not understand \'' + rb.command + '\'.')
        return GetCommand(rb)
    if len(rb.command.split()) > 1 and rb.command.split()[1].isdigit:
        if rb.command.split()[0] == 'back':
            rb.steps = '-'+rb.command.split()[1]
        else:
            rb.steps = rb.command.split()[1]
    rb.instruction = rb.command.split()[0].lower()

def RunCommand(rb):
    GetCommand(rb)
    for command in rb.call_func:
        if rb.instruction == command:
            rb.call_func[command](rb)
    if rb.rb_on == True:
        return RunCommand(rb)

def robot_start():
    """This is the entry function, do not change"""
    rb = CreateRobot()
    print(rb.name_dot + 'Hello kiddo!')
    RunCommand(rb)


if __name__ == "__main__":
    robot_start()