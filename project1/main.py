# niech graja ze soba dwa kompy
# Rózne strategie: 1: Losowo , Druga : pierwsza odp losowo potem caly czas to samo 3: Pierwsza losowo a kada nastepna inna odp porzedniej

import random


def who_wins(answer1, answer2):
    if answer1 == 's' and answer2 == 'p':
        return 1

    if answer1 =='p' and answer2 == 's':
        return 2

    if answer1 =='s' and answer2 == 'r':
        return 2

    if answer1 =='r' and answer2 == 's':
        return 1

    if answer1 =='r' and answer2 == 'p':
        return 2

    if answer1 =='p' and answer2 == 'r':
        return 1

    if answer1 =='r' and answer2 == 'r':
        return 0

    if answer1 =='p' and answer2 == 'p':
        return 0

    if answer1 =='s' and answer2 == 's':
        return 0

    return -1 


def main():

    answers = ['s', 'p', 'r']
    user_points = 0
    computer_points = 0

    while user_points != 3 and computer_points != 3:
        print (f'Users points: {user_points} \nComputer points: {computer_points}')
        user = input("Type s,p,r for 'scissor' 'paper' 'rock'")
        computer = random.choice(answers)
        print(f'Computer choice is {computer}')
        winner =  who_wins(user,computer)
        if winner == 1:
            user_points += 1
        elif winner == 2:
            computer_points += 1
        elif winner == 0:
            print('Draw!')
        else:
            print('Please insert r, p, c')

    if user_points > computer_points:
        print(f'User Wins the game! {user_points}:{computer_points}')
    else:
        print(f'Computer Wins the game! {computer_points}:{user_points}')




if __name__ == '__main__':
    main()






