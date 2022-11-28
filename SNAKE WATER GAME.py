import random
i=0
count=0
pc=0
while i!=10:
    PC=["Snake", "Water", "Gun"]
    choice=random.choice(PC)
    user=input("""Enter your choice:
    S for SNAKE
    W for WATER
    G for Gun: """)
    user=user.upper()
    print(user)
    if choice=="Snake" and user=="W":
        print("""PC= SNAKE
YOU= WATER""")
        print("****WINNER IS COMPUTER***")
        pc=pc+1
    elif choice=="Water" and user=="G":
        print("""PC= "WATER"
YOU= GUN""")
        print("****WINNER IS COMPUTER***")
        pc=pc+1
    elif choice=="Gun" and user=="S":
        print("""PC= "GUN"
YOU= SNAKE""")
        print("****WINNER IS COMPUTER***")
        pc=pc+1
    elif user=="S" and choice=="Water":
        print("""USER= SNAKE
PC= WATER""")
        print("****YOU WON*****")
        count=count+1
    elif user=="W" and choice=="Gun":
        print("""USER= WATER
PC= GUN""")
        print("****YOU WON*****")
        count=count+1
    elif user=="G" and choice=="Snake":
        print("""USER= GUN
PC= SNAKE""")
        print("****YOU WON*****")
        count=count+1
    elif user=="S" and choice=="Snake":
        print("""USER= SNAKE
PC= SNAKE""")
        print("*****IT'S A TIE*****")
    elif user=="W" and choice=="Water":
        print("""USER= WATER
PC= WATER""")
        print("*****IT'S A TIE*****")
    elif user=="G" and choice=="Gun":
        print("""USER= GUN
PC= GUN""")
        print("*****IT'S A TIE*****")        
    i=i+1
print("PC WINS",pc,"TIMES")
print("YOU WINS",count,"TIMES")
if pc>count:
    print("*****VICTORY GOES TO COMPUTER*****")
elif count>pc:
    print("*****CONGRATULATIONS VICTORY GOES TO YOU****")
elif count==pc:
    print("******IT'S A TIE******")
    
