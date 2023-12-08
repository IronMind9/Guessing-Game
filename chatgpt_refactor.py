
import random

def show_score(attempts_list):
    print(f"The current high score is {min(attempts_list, default='No score')} attempts")

def play_game():
    attempts_list = []
    
    while input("Welcome! Would you like to play a guessing game? Enter yes or no: ").lower() == "yes":
        pc_choice, attempts = random.randint(1, 10), 0

        while True:
            try:
                guess = int(input("Choose a number between 1 and 10: "))
                if not 1 <= guess <= 10:
                    raise ValueError("Please choose a number within the range.")
                
                attempts += 1

                if guess == pc_choice:
                    print(f"Nice guess! You got it in {attempts} attempts!")
                    attempts_list.append(attempts)
                    show_score(attempts_list)
                    break

                print("It's lower!" if guess > pc_choice else "It's higher!")

            except ValueError as err:
                print(err)

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
