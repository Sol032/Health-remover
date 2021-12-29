# program that will remove health from player depending on the user's prefrences
# this program was made just to practice while loops and if statments as well as inputs
import time

playerHealth = 100  

def killplayer_C():
    health = input("What would you like the player health to be?: ")
    try:
        health = int(health)
    except:
        print("please enter a valid number")
        quit()
    damage = input("How much do you want the player to be damaged in each hit?: ")
    try:
        damage = float(damage)
    except:
        print("please enter a valid number")
        quit()
    timeBetweenHits = input("how much time between each hit? (in seconds): ")
    try:
        timeBetweenHits = float(timeBetweenHits)
    except:
        print("please enter a valid number")
        quit() 
    hit = True
    timerStart = time.time()
    while hit == True and health > 0:
        print("Player is getting hit, current health: ", health)
        time.sleep(timeBetweenHits)
        health = health - damage
        if health <= 0:
            print("Player Died, Game over")
            break
    timerEnd = time.time()
    print("It toke ", timerEnd - timerStart," seconds to kill the player")
    time.sleep(0.1)
    print("Thank you for using our tester")
            
    
def killplayer():
    hit = True
    health = playerHealth
    timerStart = time.time()
    while hit == True and health > 0:
        print("Player is getting hit, current health: ", health)
        time.sleep(0.5)
        health = health - 5
        if health == 0:
            print("Player Died, Game over")
            break
    timerEnd = time.time()
    print("It toke ", timerEnd - timerStart, " seconds to kill the player")
    time.sleep(0.1)
    print("Thank you for using our tester")

askS = input("Would you like to customize the input?(Y/N)(Default: Health = 100, damage = 5, time between hit = 0.5): ")\

if askS == "y" or askS == "Y" or askS == "yes":
    killplayer_C()
elif askS == "n" or askS == "N" or askS == "no":
    killplayer()
else:
    print("Please enter a Y (yes) or N (no) answer")
    
