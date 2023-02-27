from gameclass import Game

Setup = input("\n\nWelcome!\nDo you want to play (1) timed? or (2) Not timed?\n\n > ")
while(True):
    if(Setup == "1" or Setup == "timed"):
        Time = input("\n\nWhat do you want the time limit to be (in seconds)?\n\n > ")
        Start = Game.Timed(Time)
        if(Start == -1):
            print("\n\nGoodbye.\n\n")
            break
    if(Setup == "2" or Setup == "not timed"):
        Start = Game.NoTime()
        if(Start == -1):
            print("\n\nGoodbye.\n\n")
            break
    else:
        Setup = input("That is not an option. \nDo you want to play (1) timed? or (2) Not timed?\n\n > ")