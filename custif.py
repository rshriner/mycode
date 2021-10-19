#!/usr/bin/env python3
"""Alta3 course | RShriner
   if, elif, else - A simple program using conditionals to make a decision."""

import random
from os import system

message = """\
   The Magic PyBall!
   No question too silly - only silly answers!
   
   Type QUIT to exit
   
   """

quest = ""
while quest != "QUIT":
    system('clear')
    print(message)
    quest = input("What question do you have for the Magic PyBall?\n> ")
    index = random.randint(1,10)
    if index == 1:
        ans = "With certainty!"
    elif index == 2:
        ans = "Ground control to Major Tom...Check ignition and may God's love be with you."
    elif index == 3:
        ans = "No... I'm afraid not."
    elif index == 4:
        ans = "Maybe, I misunderstood you?"
    elif index == 5:
        ans = "Highly unlikely!"
    elif index == 6:
        ans = "Don't make me laugh!"
    elif index == 7:
        ans = "Outcome uncertain..."
    elif index == 8:
        ans = "Like a Donkey's butt in a pepper patch!"
    elif index == 9:
        ans = "Don't be crazy!"
    else:
        ans = "You know it!"
    if quest == "QUIT":
        ans = "Thanks for playing!  Goodbye!"
    print("\nMagic PyBall says...\n" + ans + "\n")
    if quest == "QUIT":
        break
    input("Press ENTER to try again")
