import random

choices = ['rock','paper','sccissors']
score=0

# best of 3 gameloop
#  removes any leading (spaces at the beginning) and trailing (spaces at the end) characters 
# lower() method returns a string where all characters are lower case
for i in range(3):
    choice =input('Lets play rock, paper, scissors! What do you choose?').lower().strip('')
    
    # get the computers choice
    computer_choice = random.choice(choices)
    print('computer chose: '+ computer_choice)
    
    # determine the outcome
    if(choice == computer_choice):
     print('This round was a draw!')
    
    elif((choice=='rock' and computer_choice=='scissors')
         or(choice == 'paper' and computer_choice=='rock')or(choice =='scissors'and computer_choice=='paper')):
      print('you won this round!')
      score += 1
      
    else:
        print('you lost this round!')
        
    print()
    
print('you won' + str(score)+ '/3 games.')          