import random
from TimesTables import MultiplesQsAndAs
from pytimedinput import timedInput

def tmsg(r):
    print(f"Times up! The Correct answer is: {MultiplesQsAndAs[r +1]}\n\n")
def refresh():
    while(True):
        randomqanda = random.randrange(0,104,2)
        question = input(MultiplesQsAndAs[randomqanda])
        question = int(question)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break
def refreshT(limit):
    while(True):
        randomqanda = random.randrange(0,104,2)
        limit = int(limit)
        question, timedOut = timedInput(prompt=MultiplesQsAndAs[randomqanda], timeout=limit, resetOnInput= False)
        if(timedOut):
            print(f"Times Up!\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
            continue
        question = int(question)
        timedOut = int(timedOut)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break
def Natural():
    while(True):
        randomqanda = random.randrange(0,234,2)
        question = input(MultiplesQsAndAs[randomqanda])
        question = int(question)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break
def NaturalT(limit):
    while(True):
        randomqanda = random.randrange(0,234,2)
        limit = int(limit)
        question, timedOut = timedInput(prompt=MultiplesQsAndAs[randomqanda], timeout=limit, resetOnInput= False)
        if(timedOut):
            print(f"Times Up!\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
            continue
        question = int(question)
        timedOut = int(timedOut)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break
def All():
    while(True):
        randomqanda = random.randrange(0,363,2)
        question = input(MultiplesQsAndAs[randomqanda])
        question = int(question)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break
def AllT(limit):
    while(True):
        randomqanda = random.randrange(0,363,2)
        limit = int(limit)
        question, timedOut = timedInput(prompt=MultiplesQsAndAs[randomqanda], timeout=limit, resetOnInput= False)
        if(timedOut):
            print(f"Times Up!\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
            continue
        question = int(question)
        timedOut = int(timedOut)
        if(question == MultiplesQsAndAs[randomqanda +1]):
            print("Correct\n\n")
        elif(question == -1):
            print("Going Back to Game Options.")
        else:
            print(f"Incorrect\nThe Correct answer is: {MultiplesQsAndAs[randomqanda +1]}\n\n")
        if(question ==-1):
            break