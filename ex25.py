def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')#################
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)#############

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)##############
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentences(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and prints the first and the last one."""
    words = sort_sentences(sentence)
    print_first_word(words)
    print_last_word(words)

#python
#import ex25
#sentence = "All good things come to those who wait."
#words = ex25.break_words(sentence)
#####################
#help(ex25)   help(ex25.break_words)
#####################
#from ex25 import *
#sentence = "All good things come to those who wait."
#words = break_words(sentence)
