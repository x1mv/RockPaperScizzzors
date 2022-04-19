## todo ##
## output win to txt file

## outcomes (note for me) ##

## rock > scissors
## scissors > paper
## paper > rock
from time import sleep
import os
import random
clear = lambda: os.system('cls')

## game ##
while True:
    userinput = input("Choose! (rock, paper, scissors): ")

## random win messages ##
    tie_replies = ["It's a tie!", "Both of you chose the same thing, tie!!!", "The winner is... nobody! Tie!", "Hey, how did that happen?? Tie!", "What a coincidence! Tie!"]
    rock_scissors_win = ["You won! Rock smacked the scissors back into the ER.", "Rock > scissors, you won.", "GG EZ git gud scissors", "Atleast the scissors tried to fight back."]
    scissors_paper_win = ["Haha, scissors go brrrrr (You won)", "Scissors SLICED the paper.", " Paper = noobie", "Rest in piss, paper!", "Paper went oof", "Paper, it's hardcore, you cannot respawn..."]
    paper_rock_win = ["Packaged that rock in christmas wrapping paper.", "The perfect present for a Rust player! Paper won.", "No more Eoka ammo. Paper won.", "Rocked the rock!", "Rock = nul (You won!)"]
    lost_anyhow = ["You lost. Try again!", "Welp, you got obliterated on that one", "Try harder!", "Usually, theres a 50/50 chance you win this. Turns out you didnt win this one.", "The enemy is laughing at you! Get back at them! (you lost)", "You got 360 No-scoped.", "Haha, you lost!!", "Remember, the enemy is probably laughing right now. Try again.", "These lose messages are getting longer.", "Hey, I'm here to inform you that you lost. Lol.", "Pretend the enemy was you (You lost)", "YOU HATE THE ENEMY RIGHT? (You lost)", "Kill the enemy next time! (You lost)"]

## random time wait ##
    randomwait = random.randrange(1, 3)

## print functions ##
    r_s_printfunc = random.choice(rock_scissors_win) ## rock won over scissors
    s_p_printfunc = random.choice(scissors_paper_win) ## scissors won over paper
    p_r_printfunc = random.choice(paper_rock_win) ## paper won over rock
    lost_printfunc = random.choice(lost_anyhow) ## you lost lol

## bot functions ##
    outcomes = ["rock", "paper", "scissors"]
    reply = random.choice(outcomes)

## win decision ##

    if userinput == reply:
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print("It's a tie!")
    elif userinput == "rock":
        if reply == "scissors":
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(r_s_printfunc)
        else:
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(lost_printfunc)
    elif userinput == "scissors":
        if reply == "paper":
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(s_p_printfunc)
        else:
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(lost_printfunc)
    elif userinput == "paper":
        if reply == "rock":
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(p_r_printfunc)
        else:
            print("Give the bot a second to think about what to pick...")
            sleep(randomwait)
            print(lost_printfunc)

    replay = input("Play once more? (Y/N): ")
    if replay.lower() != "y":
        clear()
        break
        clear()