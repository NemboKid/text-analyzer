"""
All functions
"""

from collections import Counter
import re

global_dict = {}

standard_textfile = "phil.txt"

def open_file():
    """
    Opens file
    """
    global standard_textfile
    open(standard_textfile, "r")
    return standard_textfile

random = 0
def lines():
    """
    Counts number of lines
    """
    f = open(open_file(), "r")
    j = 0
    global random
    for item in enumerate(f):
        random = len(item)
        j += 1
    return j


def word_count():
    f = open(open_file(), "r")
    wordcount = Counter(f.read().split())
    list_words = []
    for words in wordcount.items():
        list_words.append(words)
    global global_dict
    global_dict['words'] = len(list_words)
    return len(list_words)


def letters():
    """
    count letters
    """
    f = open(open_file(), "r")
    lettercount = f.read().replace(" ", "")
    only_letters = re.sub('[^a-z]', '', lettercount)
    letter_list = []
    for i in only_letters:
        i.lower()
        letter_list.append(only_letters)
    global global_dict
    global_dict['letters'] = len(letter_list)
    return len(letter_list)


def word_frequency():
    """
    prints out 7 most frequent words
    """
    f = open(open_file(), "r")
    wordcount = Counter(f.read().split())
    most_freq = wordcount.most_common(7)

    global global_dict
    global_dict['word frequency'] = most_freq
    dict(wordcount)
    word_list = []
    percent_list = []
    keys = list(wordcount)

    for keys in most_freq:
        if keys in most_freq:
            word_list.append(keys)

        for item in keys:
            if wordcount[item] != 0:
                percent = wordcount[item] / word_count() * 100
                percent = round(percent, 1)
                percent_list.append(percent)

    i = 0
    while i < len(word_list):
        print(str(word_list[i]) + " | " + str(percent_list[i]) + "%")
        i += 1


def letter_frequency():
    """
    prints out 7 most frequent letters
    """
    f = open(open_file(), "r")
    wordcount = Counter(f.read().replace(" ", ""))
    most_freq = wordcount.most_common(7)
    dict(wordcount)
    keys = list(wordcount)
    letter_list = []
    percent_list = []

    for keys in most_freq:
        if keys in most_freq:
            letter_list.append(keys)

        for item in keys:
            if wordcount[item] != 0:
                percent = wordcount[item] / letters() * 100
                percent = round(percent, 1)
                percent_list.append(percent)
                
    global global_dict
    i = 0
    while i < len(letter_list):

        print(str(letter_list[i]) + " | " + str(percent_list[i]) + "%")
        i += 1


def do_all():
    """
    runs all functions together
    """
    print()
    print("Number of lines: " + str(lines()))
    print()
    print("Number of words: " + str(word_count()))
    print()
    print("Number of letters: " + str(letters()))
    print()
    print("The 7 most used words: ")
    word_frequency()
    print()
    print("The 7 most common letters: ")
    letter_frequency()
    print()


def change():
    """
    change file to analyze
    """
    global standard_textfile
    print("Try to change the file to \'max.txt\'")
    standard_textfile = input("Name of new textfile you want to analyze with the format \'text.txt\': ")
