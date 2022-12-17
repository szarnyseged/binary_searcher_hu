def search_number(array, value):
    """"
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

    turns the alphabet to numbers, then sort them. (sort itself also works like this with ascii)
    """

    alphabet = "0123456789-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ"
    #short:
    #new_list = sorted(array, key= lambda word: [alphabet.index(char) for char in word])
    def turn_number(word):
        turned_to_number = []
        for char in word:
            turned_to_number.append(alphabet.index(char))
        return turned_to_number
    
    new_list = sorted(array, key=turn_number)
    return new_list


def binary_search_hu(array, value):
    """
    array must be sorted (hu alphabet).
    array: list of strings
    value: value to search
    returns the value index or None
    """
    

    def turn_to_number(word):
        alphabet = "0123456789-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ"
        turned_to_number = []
        for char in word:
            turned_to_number.append(alphabet.index(char))
        return turned_to_number


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
my_list = [1,2,3,4,5,6, 7]
my_list_str = ["alma", "kabát", "Répa", "Álmos", "banán"]
print("search number:", search_number(my_list, 5))
new_sorted = sort_hu(my_list_str)
print("sorted alphabet:", new_sorted)
print(binary_search_hu(new_sorted, "banán"))
"""