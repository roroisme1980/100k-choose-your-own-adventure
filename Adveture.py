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
    print("you can either choose to go forward to band or walk into fashion")
    print("choose 1 for fasion and 2 for band")
    c=input("make your choice")
    if c=="1":
        print("you walk into fashion and are greated by many kids")
        print("All of the students smile at you deviously and start pulling out complete outfits")
        print("You end up getting dressed up in a lot of outfits from sweeters and sweetpants to dresses to a tuxedo")
        print("You end up getting trapped forrever as a modle for the fashion students")
        GS="lose"
    if c=="2":
        print("you continoue forward arriving at the etrance to band")
        GS="4b"
        print("//////////////////////////////////////")
##layer 4
if GS=="4":
    print("you arrive at the third intercection and must once more choose a path")
    print("you can go to the library or keep going forward")
    print("choose 1 for continoue forward choose 2 for the library")
    c=input("make your choice")
    if c=="1":
        print("you keep walking forward with determination")
        GS="5"
        print("//////////////////////////////////////")
    if c=="2":
        print("you walk twords the library")
        print("you arrive at the doors and swing them open only to relise a dragon has come out of a book")
        print("quickly you dash to the side and hide behind a fliped over table")
        print("while behind the table you see a book laying open face down")
        print('you pick up the book and inspect it the title says the "tale of a dragon"')
        print("you quickly slam the book shut and the dragon vanashies")
        print("even though you have saved the day you do hear the seconde bell go")
        print("you are late for computers class")
        GS="lose"
        print("//////////////////////////////////////")
if GS=="4b":
    print("two options await you could either go into the music room where sweet melodies come from or continoue outside")
    print("choose 1 for the music room and choose 2 to go outside")
    c=input("make your choice")
    if c=="1":
        print("You enter the music rooms lured by the sweet songs that are played")
        print("You end up surrounded by plesent sounds and songs you've never heard befor")
        print("they offer for you to stay and keep listening to their sweet songs")
        print("there's no way you could possibly deny that offer")
        print("you stay forever in the music room traped by song")
        GS="lose"
        print("//////////////////////////////////////")
    if c=="2":
        print("you break free of the song and keep going")
        print("you push open the doors and end up outside in the cool crisp air")
        GS="5b"
        print("//////////////////////////////////////")
if GS=="4c":
    print("the math hydra confronts you")