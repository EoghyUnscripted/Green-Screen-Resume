import json
import time
import os


def data_compiler():
    """ Decorator used to get JSON file data for processing. """

    with open(f"/Users/eoghy/Desktop/External-6-10-22/Web Development/Personal Projects/Interactive Resume/Data/resume.json") as file:

        data = json.load(file)

    return data


def snooze(count=5):
    """ Function used to call sleep timer. """

    time.sleep(count)


def typewriter(message, speed=.005):
    """ Function used to mimic typing on screen for a string. """

    string = message

    typing = ""

    for char in string:

        time.sleep(speed)
        typing += char
        os.system('clear')
        print(typing)
