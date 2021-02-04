def find_the_min(element):
    if len(element) == 1:
        return element[0]
    if element[0] < element[1]:
        rem = 1
    else:
        rem = 0
    element.remove(element[rem])
    return(find_the_min(element))

def sum_it_all(element):
    if len(element) == 1:
        return element[0]
    element[0] += element[1]
    element.remove(element[1])
    return sum_it_all(element)

def permutation(char_list, n):
    all_ = []
    if n == 1:
        return char_list
    for x in char_list:
        temp = permutation(char_list, n-1)
        for y in temp:
            all_.append(x + y)
    return all_

def find_min(element):
    """Find the smallest value in given element and returns it"""
    temp = list(element)
    for x in temp:
        if type(x) != int:
            return -1
    if len(temp) == 0:
        return -1
    val_min = find_the_min(temp)
    return val_min


def sum_all(element):
    """Sums all values in element and returns sum"""
    temp = list(element)
    for x in temp:
        if type(x) != int:
            return -1
    if len(temp) == 0:
        return -1
    val_sum = sum_it_all(temp)
    return val_sum

def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    temp = list(character_set)
    for x in temp:
        if type(x) != str:
            return []
    if len(temp) == 0:
        return []
    res = permutation(temp, n)
    return res
