import random

def generateCode():
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code

def getInput():
    while True:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue 
        break
    return answer

def calculateCorrectAnswer(answer, code):
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    return correct_digits_and_position, correct_digits_only

def userWin(correct_digits_and_position, turns):
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))
    return correct

# TODO: Decompose into functions
def run_game():
    
    code = generateCode()
    # Generates a code for the user to guess

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    # Introduction print

    correct = False
    turns = 0
    while not correct and turns < 12:

        answer = getInput()
        # Gets input and runs tests to see if input is correct

        correct_digits_and_position, correct_digits_only = calculateCorrectAnswer(answer, code)
        # Calculates result of users input compared to the code

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        correct = userWin(correct_digits_and_position, turns)
        # Checks if user has put in the correct code


    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
