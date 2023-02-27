from Functions import refresh, Natural, All, refreshT, NaturalT, AllT
import sys

class Game():


    def Timed(timeperquestion):
        Multiplesss = input("\n\nWhat multiples do you want to learn? \n 1. Refresh (2's through 5's Tables) \n 2. Natural (2's through 10's Tables) \n 3. All (2's through 15's Tables)\n Or enter -1 to quit\n > ")

        if(Multiplesss == "1"):
            refreshT(timeperquestion)
        if(Multiplesss == "2"):
            NaturalT(timeperquestion)
        if(Multiplesss == "3"):
            AllT(timeperquestion)
        if(Multiplesss == "-1"):
            return -1
        else:
             print("That's not an option. Retry")

    def NoTime():
        Multiplesss = input("\n\nWhat multiples do you want to learn? \n 1. Refresh (2's through 5's Tables) \n 2. Natural (2's through 10's Tables) \n 3. All (2's through 15's Tables)\n Or enter -1 to quit\n > ")

        if(Multiplesss == "1"):
            refresh()
        if(Multiplesss == "2"):
            Natural()
        if(Multiplesss == "3"):
            All()
        if(Multiplesss == "-1"):
            return -1
        else:
             print("That's not an option. Retry")