def CreateRobot():
    class Robot():
        x,y,direction,step = 0,0,0,0
        name,instruction = '',''
        running,replay,silent,reverse = True,False,False,False
        command,history,range_r = [],[],[]
    return Robot

def InitVariables(rb):
    rb.name = input(f"What do you want to name your robot? ").strip()
    print(f"{rb.name}: Hello kiddo!")

def GetCommand(rb):
    rb.range_r = []
    rb.silent = False
    rb.reverse = False
    valid_commands = ['off','help','forward','back','right','left','sprint','replay']
    rb.command.clear()
    for _ in input(f"{rb.name}: What must I do next? ").split():
        rb.command.append(_)
    if rb.command[0].lower() not in valid_commands:
        print(f"{rb.name}: Sorry, I did not understand \'{' '.join(rb.command)}\'.")
        return GetCommand(rb)
    rb.instruction = rb.command[0].lower()

    if len(rb.command) > 1:
        if rb.command[0] == 'back':
            rb.step = int('-' + rb.command[1])
        elif rb.instruction == 'replay':
                if '-' in rb.command[1]:
                    rb.range_r.append(rb.command[1].split('-')[0])
                    rb.range_r.append(rb.command[1].split('-')[1])
                elif rb.command[1].isdigit():
                    rb.range_r = [rb.command[1]]
                valid_args = ['silent','reversed']
                for x in rb.command:
                    if x.lower() != rb.instruction and not x[-1].isdigit():
                        if x.lower() == 'silent':
                            rb.silent = True
                        if x.lower() == 'reversed':
                            rb.reverse = True
                        if x.lower() not in valid_args:
                            print(f"{rb.name}: Sorry, I did not understand \'{' '.join(rb.command)}\'.")
                            return GetCommand(rb)
        else:
            rb.step = int(rb.command[1])

def RobotOff(rb):
    print(f"{rb.name}: Shutting down..")
    rb.running = False

def RobotHelp(rb):
    print('''I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands''')

def UpdatePosition(rb):
    if rb.instruction != 'left' and rb.instruction != 'right':
        if rb.direction == 0:
            rb.y += rb.step
        if rb.direction == 1:
            rb.x += rb.step
        if rb.direction == 2:
            rb.y -= rb.step
        if rb.direction == 3:
            rb.x -= rb.step

def Move(rb):
    if (rb.x + rb.step) <= 100 and (rb.y + rb.step) <= 100: 
        if not rb.silent:
            print(f" > {rb.name} moved {rb.instruction} by {str(rb.step).strip('-')} steps.")
        UpdatePosition(rb)
    else:
        print(f"{rb.name}: Sorry, I cannot go outside my safe zone.")
    if not rb.silent:
        print(f" > {rb.name} now at position ({str(rb.x)},{str(rb.y)}).")

def ChangeDirection(rb):
    if rb.instruction == 'left':
        rb.direction -= 1
        if rb.direction == -1:
            rb.direction = 3
    if rb.instruction == 'right':
        rb.direction += 1
        if rb.direction == 4:
            rb.direction = 0
    print(f" > {rb.name} turned {rb.instruction}.")
    print(f" > {rb.name} now at position ({str(rb.x)},{str(rb.y)}).")
    UpdatePosition(rb)
            
def RecurSprint(rb, steps, sum_):
    if steps == 0:
        rb.instruction = 'forward'
        rb.step = sum_
        UpdatePosition(rb)
        print(f" > {rb.name} now at position ({str(rb.x)},{str(rb.y)}).")
        return sum_
    sum_ += steps
    print(f" > {rb.name} moved forward by {str(steps)} steps.")
    return RecurSprint(rb, steps - 1, sum_)
        
def Sprint(rb):
    RecurSprint(rb, rb.step, 0)

def Replay(rb):
    rb.replay = True
    comm_amm = 0
    if rb.reverse == True:
        rev = 1
    else:
        rev = 1
    if len(rb.range_r) == 0:
        rb.range_r.append(-1 * len(rb.history))
        n = int(rb.range_r[0])
        neg = 1
    else:
        n = int(rb.range_r[0])
        neg = -1
    new_history = []
    if len(rb.range_r) != 0:
        for x in rb.history[n - 1::1]:
            new_history.append(x)
    else:
        new_history = rb.history

    # print(new_history)
    for command in sorted(new_history, reverse=rb.reverse):
        comm_amm += 1
        rb.command = []
        rb.command.append(command.split()[0])
        if 'right' in command or 'left' in command:
            rb.command.append(0)
        else:
            rb.command.append(command.split()[1])
        rb.instruction = rb.command[0]
        if rb.instruction == 'back':
            rb.step = int('-' + rb.command[1])
        else:
            rb.step = int(rb.command[1])
        RunCommand(rb)
    silent = ''
    reverse = ''
    if rb.silent:
        silent = ' silently'
    if rb.reverse:
        reverse = ' in reverse'
    print(f" > {rb.name} replayed {str(comm_amm)} commands{reverse}{silent}.")
    print(f" > {rb.name} now at position ({str(rb.x)},{str(rb.y)}).")
    rb.replay = False

def RunCommand(rb):
    command_list = {'off':RobotOff,'help':RobotHelp,'forward':Move,'back':Move,'left':ChangeDirection,'right':ChangeDirection,'sprint':Sprint}
    for command in command_list:
        if rb.instruction == command:
            command_list[command](rb)
    if 'replay' not in rb.instruction and rb.replay != True:
        rb.history.append(' '.join(rb.command))
    if rb.instruction == 'replay':
        Replay(rb)

def robot_start():
    """This is the entry function, do not change"""
    rb = CreateRobot()
    InitVariables(rb)
    while rb.running:
        GetCommand(rb)
        RunCommand(rb)


if __name__ == "__main__":
    robot_start()