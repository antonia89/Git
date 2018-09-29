import random
import string

def get_word_string(filename):
    '''Opens a file, if the file exists then it turns the text into a string
         but if file does not exist the string will stay empty'''
    word_string = ""
    try:
        a_file = open(filename,"r")
        for line in a_file:
            word_string += line
    except:
        print("File",filename,"not found\n")
    return word_string

def punctuation_not_affect(word):
    '''If a word has a punctuation in it - function makes sure it does not affect the shuffling of the letters'''
    start = 1
    end = len(word)-1
    while word[start] in string.punctuation:
        start += 1
    while word[end] in string.punctuation:
        end -= 1
    return start,end

def scramble_string(a_string):
    '''Takes a string and scrambles each word and puts it in a list'''
    a_list = a_string.split()
    scrambled_list = []
    for string, word in enumerate(a_list):
        if len(word) > 3:
            word = list(word)
            a_str = shuffle_makes_str(word)
            scrambled_list.append(a_str)
        else:
            scrambled_list.append(word)
        new_string = " "
        new_string = new_string.join(scrambled_list)
    return new_string

def shuffle_makes_str(word):
    '''Takes the list and shuffles it, then turns it in to a string'''
    a_str = ""
    start,end = punctuation_not_affect(word)
    stringy = word[start:end]
    random.shuffle(stringy)
    word[start:end] = stringy
    word.append(" ")
    a_str = a_str.join(word)
    return a_str

random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)