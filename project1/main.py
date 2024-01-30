# papier kamien nozyce
# user i komputer gramy do 3
# wypisac zwyciezce i wynik 
# jesli wpisze niepoprawny input to ogarnąć
import random



# def main():
        
answers = ['s', 'p', 'r']
user_points = 0
computer_points = 0


while user_points < 3 or computer_points < 3:
    print (f'Users points: {user_points} \nComputer points: {computer_points}')
    user = input("Type s,p,r for 'scissor' 'paper' 'rock'")
    computer = random.choice(answers)
    print(f'Computer choice is {computer}')
    if user == 's' and computer == 'p':
        print('Users wins!')
        user_points += 1
    elif user =='p' and computer == 's':
        print('Computer Wins!')
        computer_points += 1    
    elif user =='s' and computer == 'r':
        print('Computer Wins!')
        computer_points += 1
    elif user =='r' and computer == 's':
        print('User Wins!')
        user_points += 1
    elif user =='r' and computer == 'p':
        print('Computer Wins!')
        computer_points += 1
    elif user =='p' and computer == 'r':
        print('User Wins!')
        user_points += 1
    elif user =='r' and computer == 'r':
        print('Draw!')
    elif user =='p' and computer == 'p':
        print('Draw!')
    elif user =='s' and computer == 's':
        print('Draw!')
    else:
        print('Please insert s, r ,c')

    if user_points == 3 and computer_points < 3:
        print (f'Users wins whole match with {user_points} points  \nComputer points: {computer_points}')
        break
    elif user_points < 3 and computer_points == 3:           
        print (f'Computer wins whole match with {computer_points} points  \nUser points: {user_points}')
        break

# return 
    


        



            





# if __name__ == '__main__':
#     main()






