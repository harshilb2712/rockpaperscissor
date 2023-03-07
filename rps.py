import random
x = 1
score1 = 0
score2 = 0
lis = ['rock','paper','scissor']
print("<---------WELCOME TO THE GAME--------->")
user1_name = (input("Enter your name user1: "))
user2_name = 'Computer'
print(user1_name,"V/S",user2_name)
print("Choose from the options (Rock,Paper,Scissor)")
while(x):
    user1_in = input("Choose your option user1: ").lower()
    user2_in = random.choice(lis).lower()
    print(user_name, "chose", user2_in)
    if(user1_in not in lis or user2_in not in lis):
        print("Invalid input start again")
    else:
        if(user1_in == user2_in):
            print("Its",user1_in,"v/s",user2_in)
            print("Its a tie, score remains the same")
        elif(user1_in == 'rock' and user2_in == 'paper' ):
            print("Its rock v/s paper")
            score2 +=1
            print("winner is = ",user2_name)
        elif(user1_in == 'rock' and user2_in == 'scissor' ):
            print("Its rock v/s scissor")
            print("winner is = ",user1_name)
            score1 +=1
        elif(user1_in == 'paper' and user2_in == 'rock' ):
            print("Its paper v/s rock")
            print("winner is = ",user1_name)
            score1 +=1
        elif(user1_in == 'paper' and user2_in == 'scissor' ):
            print("Its paper v/s scissor")
            print("winner is = ",user2_name)
            score2 +=1
        elif(user1_in == 'scissor' and user2_in == 'rock' ):
            print("Its scissor v/s rock")
            print("winner is = ",user2_name)
            score2 +=1
        elif(user1_in == 'scissor' and user2_in == 'paper' ):
            print("Its scissor v/s paper")
            print("winner is = ",user1_name)
            score1 +=1
        else:
            print("There is an error ")
        print("<---------------------------------------------->")
        x = int(input("Do you want to play again? if yes then press 1 or else 0: "))
        
print("THANK YOU I HOPE YOU ENJOYED")
print("The final scores are-->")
print(user1_name," = ",score1)
print(user2_name," = ",score2)
if(score1>score2):
    print("Winner is: ",user1_name)
elif(score1 == score2):
    print("Its a tie you both played well")
else:
    print("Winner is: ",user2_name)
