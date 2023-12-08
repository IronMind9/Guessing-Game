import random 
Attempts_list = [] 


def show_score() :
    if not Attempts_list :
        print("no score to shows ! ")
    else :
        print(f"The current high score is {min(Attempts_list)} attempts")
        
attempts = 0          
pc_choice = random.randint(1,10)    
player_nam = input("Enter your name : ") 

wanna_play = input("Welcom " + player_nam + " whould you play a guessing game "+" Enter yes or no :")

if wanna_play == "no" : 
    print("That's cool , thanks ")
    exit()
    
else :
    show_score() 
     
while wanna_play == "yes" :
    try:
        guess = int(input("Chose a number between 1 and 10 " ))
        
        if(guess < 1 or guess > 10 ) :
            raise ValueError("please chose a number of the range ") 
        attempts+= 1
         
        if guess == pc_choice :
            print ("Nice guess , You got it ! " ) 
            print(f"it tooks {attempts} attempts to get it  !")
            wanna_play = input("you wanna play again? (yes or no) ")
            Attempts_list.append(attempts)
            
            if wanna_play == "no":
                print("ok see u soon !")
            else :
                attempts = 0 
                pc_choice =random.randint(1 , 10) 
                show_score()
                continue        
            
        elif guess >pc_choice :  
                print("it's lower !! ")
            
        else : 
                print("it's higher !! " ) 
                    
    except ValueError as err :
        print(err) 
            
        
         
    