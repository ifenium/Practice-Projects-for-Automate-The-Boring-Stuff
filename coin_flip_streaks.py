from random import randint

numberOfStreaks = 0 
streak = 0
flips = []

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.    
    for i in range(100):
        flips.append(randint(0,1))  

    # Code that checks if there is a streak of 6 heads or tails in a row.   
    for i in range(len(flips)):
        if i == 0:
            pass
        elif flips[i]  == flips[i-1]:
            streak += 1
        else:   
            streak = 0

        if streak == 6:
            numberOfStreaks +=1 
            break

print('Chance of streak: {}%' .format(numberOfStreaks / 10000 * 100))