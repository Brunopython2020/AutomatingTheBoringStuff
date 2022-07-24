import random


number_of_streaks = 0
numbers_of_experiments = 10000

for experimentNumber in range(numbers_of_experiments):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips= []
    for i in range(100):
        if random.randint(0,1)== 0:
            flips.append('H')
        else:
            flips.append('T')
        

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(len(flips)-5):
        streak_list = []
        for k in range(6):
            streak_list.append(flips[j+k])
        
        for l in range(len(streak_list)):
            if streak_list[l] == streak_list[l-1] and l > 0:
                check_streak = True
            elif streak_list[l] != streak_list[l-1] and l > 0:
                check_streak = False
                break
        if check_streak == True:
            number_of_streaks += 1


print('Chance of streak: %s%%' % ((number_of_streaks / (numbers_of_experiments*100))*100))
print(number_of_streaks)

