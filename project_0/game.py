#Game - "Guess the number"

import numpy as np

#RUN 
if __name__ == "__main__":
    
    #score_game(predict_random)
    
    number = np.random.randint(1, 101) #think a number

    #Number of try
    count = 0

    while True:
        count+=1
        predict_number = int(input("Guess the number from 1 to 100\n"))
        
        if predict_number > number:
            print("Number should be less!")
        elif predict_number < number:
            print("Number should be greater!")
        else:
            print(f"You find number! It is {number}. You tried {count} times")
            break #game over
        