import random


'''
snake = 1
water = -1
gun = 0

'''

computer  = random.choice([1, -1, 0]) 
gameDict = {"s" : 1, "w": -1, "g" : 0} 
compDict = {1: "snake", -1 : "water", 0 : "gun"}

yourStr = input("Enter your Choice : ")

you = gameDict[yourStr]



if (computer == 1 and you ==1):
    print("Match draw!")
elif(computer == 1 and you == -1):
    print("you lose!")
elif(computer == 1 and you == 0):
    print("you win!")
elif(computer == -1 and you == 0):
    print("you lose!")
elif(computer == -1 and you == -1):
    print("Match draw!")
elif(computer == -1 and you == 1):
    print("you win!")
elif(computer == 0 and you == 0):
    print("Match draw!")
elif(computer == 0 and you == -1):
    print("you win!")
elif(computer == 0 and you == 1):
    print("you lose!")
else : print("something went wrong!")