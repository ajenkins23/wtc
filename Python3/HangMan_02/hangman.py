import random


def read_file(file_name):
    '''Get words from file'''
    with open(file_name) as file:return file.readlines()

def select_random_word(words):
    '''Selects random word from argument'''
    return words[random.randint(0, len(words) -1)]

def select_random_letter_from(word):
    '''Selects a random letter from the word'''
    random_index = random.randint(0, len(word)-2)
    letter = word[random_index]
    print('Guess the word: '+word[:random_index]+"_"+word[random_index+1:])
    return letter, random_index

def get_user_input():
    '''Gets user's input'''
    return input('Guess the missing letter: ').strip()

def show_answer(answer, selected_word, missing_letter_index):
    '''Checks if answer is correct'''
    if answer in selected_word[missing_letter_index]:
        print("The word was: " + selected_word)
        print("Well done! You are awesome!")
    else:
        print("The word was: " + selected_word)
        print("Wrong! Do better next time.")
    pass

def ask_file_name():
    '''Asks for file, if none is given then use defualt file.'''
    newWordFile = input("Words file? [leave empty to use short_words.txt] : ").strip()
    if len(newWordFile) < 1:
        newWordFile = "short_words.txt"
    return newWordFile

def run_game(file_name):
    '''Runs the game'''
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)

if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

