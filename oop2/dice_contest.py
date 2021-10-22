#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    # the player known as the trick_dice
    trick_dice = Cheat_Trick_Dice()
    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0
    trick_score = 0
    unaccounted_score = 0
    draw_count = 0
    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        trick_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()
        trick_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(trick_dice.get_dice()):
            #print("Dice swapper wins!")
            swapper_score+= 1
        elif sum(trick_dice.get_dice()) > sum(swapper.get_dice()) and sum(trick_dice.get_dice()) > sum(loaded_dice.get_dice()):
            #print("Trick Dice wins!")
            trick_score+= 1
        elif sum(loaded_dice.get_dice()) > sum(trick_dice.get_dice()) and sum(loaded_dice.get_dice()) > sum(swapper.get_dice()):
            #print("Loaded Dice wins!")
            loaded_dice_score+= 1
        elif sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) or sum(swapper.get_dice()) == sum(trick_dice.get_dice()) or sum(loaded_dice.get_dice()) == sum(trick_dice.get_dice()):
            #print("Draw!")
            draw_count+=1
            pass
        else:
            print("ERROR - SCENARIO UNACCOUNTED")
            print(f"Loaded {loaded_dice.get_dice()}; Trick {trick_dice.get_dice()}; Swapper {swapper.get_dice()}")
            unaccounted_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Trick dice won: {trick_score}")
    print("-------------------")
    print(f"Draws: {draw_count}")
    print(f"Unaccounted: {unaccounted_score}")
    print("╔════════════════════════════╗")

    # determine the winner
    if swapper_score == loaded_dice_score == trick_score:
        print("║       Game was drawn       ║")
    elif swapper_score > loaded_dice_score and swapper_score > trick_score:
        print("║   Swapper won most games   ║")
    elif trick_score > loaded_dice_score and trick_score > swapper_score:
        print("║ Trick dice  won most games ║")
    else:
        print("║ Loaded dice won most games ║")
    print("╚════════════════════════════╝")

if __name__ == "__main__":
    main()

