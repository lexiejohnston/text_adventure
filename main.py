print("""WELCOME TO THE ADVENTURE GAME!
    Let's start the action! ☆-🎬-☆

    Ben wakes up in his bedroom in the middle of the night. He heard a loud BANG outside the house.
    Now he has two choices: he can either stay in the room or check what the sound might be about.

    Type your choice: Stay or Evaluate?
""")

def scene1(): # the name for the first scene   fff
    import time #used to bring the date into the scene
    print("""WELCOME TO THE ADVENTURE GAME!
    Let's start the action! ☆-🎬-☆

    Ben wakes up in his bedroom in the middle of the night. \nHe heard a loud BANG outside the house.
    Now he has two choices: \nHe can either stay in the room or check what the sound might be about.

    Type your choice: Stay or Evaluate?
""")

    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="STAY"):
            print("\nBen decides to stay in the room and ends up staying inside forever as no one seems to come to help him.")
            ans = 'correct'
        elif(c1.upper()=="EVALUATE"):
            print("Ben exits the room silently and reaches the main hall.")
            ans='correct'
            scene2()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Evaluate?")
            c1 = input()

import time
print("""
            In the main hall, he finds a strange but cute teddy bear on the floor. 
            He wanted to pick the teddy up. 
            But should he? It doesn't belong to him. (•˳̂•̆)

            Type your choice: Pick or Ignore?
""")
time.sleep(2)
c1 = input()
ans = 'incorrect'
while(ans=='incorrect'):
  if(c1.upper()=="PICK"):
    print("""\nThe moment Ben picked up the the teddy bear.\n The Teddy bear starts TALKING! The bear tells Ben that he is in grave danger as there is a monster in      
the house.And the monster has captured his parents as well! But he hugged him and       told him not to get scared as he knows how to beat the moster!""")
    time.sleep(2)
    print("""\nThe bear handed Ben a magical potion which can weaken the moster and       make him run away! He handed him the potion and then DISAPPEARED! Ben moved             forward.""")
    ans = 'correct'
    pick = "True"
  elif(c1.upper()=='IGNORE'):
    print("""\nBen decided not to pick up the bear and walked forward.""")
    ans='correct'
    pick="False"
  else:
    print("Wrong Input! Enter pick or ignore?")
    c1=input()
    time.sleep(2)
    scene3(pick)

def scene3(pick_value):
    import time
    print("""\n\nAfter walking for a while, Ben saw the MONSTOR in front of him!
    It had red eyes and evil looks. He got very scared! """)
    time.sleep(2)
    if(pick_value=="True"):
        time.sleep(2)
        print("""But then he remembered! He had the magic portion and he threw it on the moster!
              Well he had nothing to lose!""")
        time.sleep(2)
        print("\n The monster SCREAMED in pain but he managed to make a portal and pushed Ben to a new world!")
    elif(pick_value=="False"):
        print("The monster attacked Ben and hurt him! He was then thrown to the new world by the monster!")

scene1()
print(("\n\n""=================================END OF CHAPTER 1================================="))