import random
total = 0
while total < 20:
    heads_needed = 10
    heads = 0
    tries = 0
    while heads_needed != heads:
        toss = random.randint(0,1)
        if toss == 1:
            heads +=1
        else:
            heads = 0
        tries +=1
    print("It took " + str(tries) + " to get 10 heads in a row")
    total += 1     
