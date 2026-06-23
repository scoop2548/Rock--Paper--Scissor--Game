import random
'''
1 for rock 
-1 for paper 
0 for scissor
'''
computer = random.choice([-1,0,1])
youstr =input("enter your choice(r/p/s) :")
youDict = { "r":1, "p":-1,"s":0}
reverseDict = { 1:"rock",-1: "paper",0:"scissor"}


you = youDict[youstr]
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if (computer ==you):
    print("its a draw")

elif computer == 1 and you == -1: 
        print("You win!")
elif computer == -1 and you == 1:  
        print("You lose!")

elif computer == 1 and you == 0:   
        print("You lose!")
elif computer == 0 and you == 1:   
        print("You win!")

elif computer == -1 and you == 0: 
        print("You win!")
elif computer == 0 and you == -1: 
        print("You lose!")
else:
    print("oops....something's not right!")