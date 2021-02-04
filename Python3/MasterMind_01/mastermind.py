import random

#choices
def run_game():
    chances = 12
    code_list = [0,0,0,0]
    for x in range(len(code_list)):
        code_list[x] = random.randint(0, 8)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    win = 0
    correct_place = 0

    while True:
        user_input = input('Input 4 digit code: ')
        if not user_input.isdigit():
            print('Please enter exactly 4 digits.')
            continue
        if len(user_input) != 4:
            print('Please enter exactly 4 digits.')
            continue
        if '9' in user_input:
            continue
        if '0' in user_input:
            continue
        user_code = list(user_input)

        for x in range(len(code_list)):
            if int(user_code[x]) == code_list[x]:
                correct_place += 1
                if correct_place == 4:
                    win = win+1
        print('Number of correct digits in correct place:     ' +  str(correct_place))

        same = 0
        skip = []
        skip2 = []
        for x in range(len(code_list)):
            for y in range(len(user_code)):
                if code_list[x] == int(user_code[y]) and y not in skip and x not in skip2:
                    skip.append(y)
                    skip2.append(x)
                    same += 1
                    if same == 4:
                        win = win + 1
        same = same - correct_place
        correct_place = 0
        print('Number of correct digits not in correct place: ' + str(same))
        code_res = ''
        if win == 2:
            print('Congratulations! You are a codebreaker!')
            for x in range(4):
                code_res = code_res + str(code_list[x])
            print('The code was: ' + code_res)
            break
        win = 0
        chances -= 1
        print('Turns left: ' + str(chances))
        if chances == 0:
            print('you loose!')
            break
    


    
    
    """
    TODO: implement Mastermind code here
    """
    pass


if __name__ == "__main__":
    run_game()
