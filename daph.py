import time

# global variable
my_true_love = input("who is your true love? ")

# main function
def lovers():
   
    # gather input 
    x = (input(f"how much do you love {my_true_love}? "))

    # try if integer
    try:
        x = int(x)
        for i in range(x + 1):
            
            if i > 0:
                print(f"u love {my_true_love} x{i}")
                time.sleep(3/i)
            else:
                print("Guess what")
                time.sleep(2.5)
    
    # if not integer
    except Exception:

        # if string
        if isinstance(x, str):
            print(f"u love {my_true_love} {x}")
        
        # defensive measure, but should never run
        else:
            print("invalid input")
            lovers ()

# main function call
if __name__ == "__main__": lovers()