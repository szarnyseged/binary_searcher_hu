alphabet = "0123456789-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ"


def turn_to_number(word: str):
    """
    turns the letters of a word to numbers using the alphabet.
    -> sort them later (sort itself also works like this with ascii)
    """
    turned_to_number = []
    for char in word:
        turned_to_number.append(alphabet.index(char))
    return turned_to_number


def search_number(array, value):
    """"
    Warning: binary search only works with sorted (ascending) data.
    array: list of numbers
    value: value to search
    returns: index of the value, returns None if value is not in array
    """
    array.sort()
    min = 0
    max = len(array)
    while min <= max:
        middle = int((min + max) / 2)
        if value == array[middle]:
            return middle
        # value is smaller -> go left
        elif value < array[middle]:
            max = middle-1
        # value is bigger -> go right
        elif value > array[middle]:
            min = middle+1
    return None


def sort_hu(array):
    """
    array: list of strings to sort (hu alphabet)
    returns a sorted list
    """
    hu_sorted_list = sorted(array, key=turn_to_number)
    # short:
    # hu_sorted_list = sorted(array, key=lambda word: [alphabet.index(char) for char in word])
    return hu_sorted_list


def binary_search_hu(array, value):
    """
    array must be sorted (hu alphabet). use sort_hu first.
    array: list of strings
    value: value to search
    returns the value index or None
    """
    min = 0
    max = len(array)
    while min <= max:
        middle = int((min + max) / 2)
        if array[middle] == value:
            return middle
        #value is bigger -> go right
        elif turn_to_number(array[middle]) < turn_to_number(value):
            min = middle + 1
        #value is smaller -> go left
        else:
            max = middle -1
    return None


"""
#test
my_list_number = [1,2,3,4,5,6, 7]
my_list_str = ["alma", "kabát", "Répa", "Álmos", "banán"]
number_to_search = 5
word_to_search = "banán"

print(f"location of number {number_to_search}:", search_number(my_list_number, number_to_search))
print("sorted alphabet:", sort_hu(my_list_str))
print(f"location of {word_to_search}:", binary_search_hu(sort_hu(my_list_str), word_to_search))
"""
