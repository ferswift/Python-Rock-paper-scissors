from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''Your options:
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors''')
player = int(input('Chose your move: '))
if player >=3:
    print('\033[4;31minvalid Number!!Try again.\033[m')
    exit()
print('Jo...')
sleep(1.0)
print('Ken...')
sleep(1.3)
print('Po!!!')
print('-='* 12)
print(f'Robot played: {items[computer]}!')
print(f'Human played: {items[player]} !')
print('-='* 12)
if computer == 0: #Computer played Rock
    if player ==0:
        print('Tie !')
    elif player ==1:
        print('Player wins !')
    elif player ==2:
        print('Robot wins !')          
elif computer ==1: #Computer Played Paper
    if player ==0:
        print('Robot Wins !')
    elif player ==1:
        print('Tie !')
    elif player ==2:
        print('Player Wins !')      
elif computer ==2: #Computer player scissiors
    if player ==0:
        print('Player Wins !')
    elif player ==1:
        print('Robot Wins !')
    elif player ==2:
        print('Tie !')
             