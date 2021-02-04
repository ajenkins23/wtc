#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    ''' Opens file and reads memory into variable'''
    with open(file_name, 'r') as file:
        return file.readlines()

def select_random_word(words):
    '''Selects a random word from argument'''
    word = words[random.randint(0, len(words) - 1)]
    j = random.randint(0, len(word) - 2)
    print ("Guess the word: " + word[:j] + '_' + word[j + 1:])
    return (word)

def get_user_input():
    '''Gets the user's input'''
    return(input("Guess the missing letter: "))


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

