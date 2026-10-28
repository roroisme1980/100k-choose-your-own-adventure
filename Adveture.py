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
if c=="2":
    GS="2a"
    print("You have entered into the theater")
if c!=("1","2"):
    print("You're in the backrooms")
    GS="?"
##layer 2
if GS=="2":
    print("Your are now at an intercection choose to go into the cafatiria twords fashion or to the next intercetion")
    print("choose 1 for continue 2 for the caf 3 for fashion")
    c=input("make your decision ")
    if c=="1":
        print("you have continued to the seconde intersection")
        GS="3"
    if c=="2":
        print("You have ended up in the caf. Maybe you should stay and enjoy the food")
        print("You get drawn into the food and end up staying too long")
        print("the seconde bell goes you are late")
        GS="e"
    if c=="3":
        print("you move in the direction of fashion evetualy reaching it's doors")
        GS="3b"
if GS=="2a":
    print("You stand in the middle of the theater")
    print("all eyes are on you and they are all inviteing you to join the games,")
    print("the theater games. You could join and abadon your class but should you?")
    print("choose 1 to play the games 2 to exit the other side of the theater")
