#rock paper scissors game
import random
lst=['rock','paper','scissors']
while True:
    p1=random.choice(lst)
    print('**************ROCK,PAPER,SCISSORS GAME!**************')
    p2=input('enter rock,paper or scissors')
    print('player 1 chose ' +p1)
    print('You chose ' +p2)
    if p1=='rock':
       if p2=='rock':
          print('It is tie!')
       elif p2=='paper':
          print('You win!')
       elif p2=='scissors':
          print('You lose!')
       else:
          print('Wrong input')
    elif p1=='paper':
        if p2=='rock':
            print('You lose!')
        elif p2=='paper':
            print('It is tie!')
        elif p2=='scissors':
            print('You win!')
        else:
            print('Wrong input')
    else:
        if p2=='rock':
            print('You win!')
        elif p2=='paper':
            print('You lose!')
        elif p2=='scissors':
            print('It is tie!')
        else:
            print('Wrong input')
    play_again=input('DO YOU WANT TO PLAY AGAIN?(Y/N?)')
    if play_again.upper() == "N":
        print('THANKYOU FOR PLAYING WITH US')
        break

