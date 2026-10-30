from os import system
from rich import print

GS="1"
C=0

##layer 1
print("The first bell just rang and you need to get to computers class")
print("you need to choose between going into the theater or going forward")
print("Choose 1 to move forwarf choose 2 to go to the theater")
c=input("Make your decision ")
if c=="1" :
    GS="2"
    print("you have reached the first intersection")
    print("//////////////////////////////////////")
if c=="2":
    GS="2a"
    print("You have entered into the theater")
    print("//////////////////////////////////////")
if c not in ("1","2"):
    print("You're in the backrooms")
    print("//////////////////////////////////////")
    GS="?"
##layer 2
if GS=="2":
    print("Your are now at an intercection choose to go into the cafatiria twords fashion or to the next intercetion")
    print("choose 1 for continue 2 for the caf 3 for fashion")
    c=input("make your decision ")
    if c=="1":
        print("you have continued to the seconde intersection")
        print("//////////////////////////////////////")
        GS="3"
    if c=="2":
        print("You have ended up in the caf. Maybe you should stay and enjoy the food")
        print("You get drawn into the food and end up staying too long")
        print("the seconde bell goes you are late")
        print("//////////////////////////////////////")
        GS="lose"
    if c=="3":
        print("you move in the direction of fashion evetualy reaching it's doors")
        print("//////////////////////////////////////")
        GS="3b"
if GS=="2a":
    print("You stand in the middle of the theater")
    print("all eyes are on you and they are all inviteing you to join the games,")
    print("the theater games. You could join and abadon your class but should you?")
    print("choose 1 to play the games 2 to exit the other side of the theater")
    c=input("make your decision")
    if c=="1":
        print("You join the games. They are fun and you can't even here the seconde bell ring")
        print("by the time you leave the theater school is already over you were marked absent")
        print("//////////////////////////////////////")
        GS="lose"
    if c=="2":
        print("you avoid temptation and push past the fun and games")
        print("eventually you come out on the otherside and arive at the seconde intercetion")
        print("//////////////////////////////////////")
        GS="3"
##layer 3
if GS=="3":
    print("you arrive at the seconde intersection and are faced with another decision")
    print("three options present themselfs continue down the main hall, look in the lost and found, go twords math hall")
    print("choose 1 for continue 2 for lost and found and 3 for math")
    c=input("make your decision")
    if c==1:
        print("you head directly for the third intercection")
        print("//////////////////////////////////////")
        GS="4"
    if c=="2":
        print("You turn twords the lost and found what tresures might await you")
        print("you walk up to the bin and feel compelled to pluge your arm into it")
        print("your arm sinks into the mass of clothes and water bottles befor you feel something or the lack of something?")
        print("you reach for the bottom but it never comes and befor you know whats happening you get pulled into the bin")
        print("you wake up on a pile of clothes and look around")
        print("all you can see for kilometers is giant piles of clothes you are stuck in the lost and found")
        print("//////////////////////////////////////")
        GS="lose"
    if c=="3":
        print("you move down the hallway and aproche the stairs to the math hall befor going up")
        print("once you reach the top the three headed math hydra confronts you and makes you participate in the math guantlet")
        print("//////////////////////////////////////")
        GS="4c"
if GS=="3b":
    print("You arive outside the doors to fashion")
