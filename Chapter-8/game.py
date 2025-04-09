import random

#  calculating the High-Score
def gameHighScore():
    score = random.randint(1, 63)
    print("you are playing the game")
    with open("hiscore.txt") as f:
        hiscore =  f.read() 
    if(hiscore != ""): 
       hiscore = int(hiscore)
    else:
       hiscore = 0
    
    print(f"your score : {score}")
    if(score> hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

gameHighScore()