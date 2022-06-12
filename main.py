import random
from math import trunc
from random import randint
import time
import keyboard

dadJokes = []


def titleScreen():
    choice = input("Welcome to Dad simulator. Press 1 to begin")
    if choice == "1":
        jokes()

def jokes():
    j = "I didn't like my beard at first. Then it grew on me."
    j2 = "I was up all night wondering where the sun went, but then it dawned on me."
    j3 = "How do you find Will Smith in the snow? Look for fresh prints."
    j4 = "I'm reading a book about anti-gravity. I can't put it down."
    j5 = "What did the grape say when it was stepped on? Nothing, it just let out a little wine."
    j6 = "Once you've seen one shopping center, you've seen the mall."
    dadJokes.append(j)
    dadJokes.append(j2)
    dadJokes.append(j3)
    dadJokes.append(j4)
    dadJokes.append(j5)
    dadJokes.append(j6)
    print("--------------------------------------------------------------------------------")
    print("Python Console Dad: " + random.choice(dadJokes))
    print("--------------------------------------------------------------------------------")

    titleScreen()


titleScreen()
