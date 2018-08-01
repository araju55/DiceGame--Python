def gameOver(scores)
      i =0
    while i<len(scores) and scores[i]<100:
        i+=1
    return i<len(scores)

def castDice(dice)
    import random
    die1 = random.randint(1,6)
    die2= random.randint(1,6)
    points=0
    print("die 1-->", die1, "Die2 -->", die2)
    if die1==1 and die2==1:
        points=-1
    elif die1!=1 and die2!=1:
        points = die1+die2
    return points


def displayWinner(scores)
    winPos = 0
    highestScore = scores[0]
    for i in range(len(scores)):
        if scores[i] > highestScore:
            winPos=i
            highestScore = scores[i]
    
    print("The winner is player: ", winPos+1 ," score", highestScore)



def updateScore(scores, points)
    if points !=-1:
        score +=points
    else:
        score=0
    return score

score1 = 0
score2 = 0
n = int (input ("Number of players"))

scores = [0]*n

while not gameOver(scores)
      for pos in range(len(scores)):
        print("player ", pos ,": score : ", scores[pos])
        points = castDice()
        scores[pos] = updateScore(scores[pos], points)
 
        print("player ", pos+1 ,": score : ", scores[pos])

displayWinner(scores)





              

