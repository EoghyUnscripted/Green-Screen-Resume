import json
import time
import os


def data_compiler():
    """ Decorator used to get JSON file data for processing. """

    file = open("Data/resume.json", "r")

    data = json.load(file)

    return data


def snooze(count=5):
    """ Function used to call sleep timer. """

    time.sleep(count)


def typewriter(message, speed=.005):
    """ Function used to mimic typing on screen for a string. """

    string = message

    #    typing = ""

    for char in string:

        time.sleep(speed*5)
        #      typing += char
        #      os.system('clear')
        #      print(char)
        print(char, end='', flush=True)

    print("\n")

