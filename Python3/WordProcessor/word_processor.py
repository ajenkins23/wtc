
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    return [a.strip(',;?.').lower() for a in text.split()]

def words_longer_than(length, text):
    return [a.strip(',;?.') for a in text.split() if len(a) > length]

def words_lengths_map(text):
    text_list = convert_to_word_list(text)
    text_list = sorted(text_list,key=len)
    int_list = []
    for word in text_list:
        int_list.append(len(word))
    int_map = {}
    for num in int_list:
        int_map.update({num:0})
    for num in int_map:
        int_map.update({num:int_list.count(num)})
    return int_map

def letters_count_map(text):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    text = text.lower()
    text.strip(',;?.')
    count_map = {}
    for char in alpha:
        count_map.update({char:text.count(char)})
    return count_map

def most_used_character(text):
    if len(text) == 0:
        return None
    count_map =  letters_count_map(text)
    popular = ''
    count = 0
    for key, item in count_map.items():
        if count < item:
            popular = key
            count = item
    return popular

def get_alphabet_characters():
    pass