import random
print("NUMBER GUESSIN GAME...!")
try:
    print("YOU HAVE A 7 CHANCE TO GUESS THE NUMBER.")
    r=int(input("ENTER YOUR RANGE:-"))
    no=random.randint(0,r)
    attempt=0
    while attempt<7:
        attempt+=1
        ui=int(input("ENTER YOUR CHOICE:-"))
        if ui<0 or ui>r:
            print("PLEASE ENTER NUMBER IN 0 TO ",r," RANGE")
            continue
        print("NUMBER OF ATTEMPT LEFT-",7-attempt)
        if attempt==7:
            print("SORRY ..YOU REACHED YOUR LIMIT..TRY AGAIN")
            print("NO IS-",no)
            break
        elif no==ui:
            print("CONGRATULATION..! YOU GUESS NO AT-",attempt,"ATTEMPT")
            break
        elif no>ui:
            print("NO IS GRATTER THAN-",ui)
        elif no<ui:
            print("NO IS LESS THAN-",ui)
except ValueError:
    print("Please Enter Numeric Value") 