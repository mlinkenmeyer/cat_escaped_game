import time


def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
    print()


def start_game():
    while True:
        print("""
        You’re winding down for the night, and realize you haven’t 
        seen your cat since you got home earlier. You look all over 
        and conclude she must have escaped when you last opened your door!
            
        What’s your first step to find your cat? 
            
            1. Make “missing cat” posters to hang up around your neighborhood.

            2. Go outside to look for her near your home. 
        
        Type 1 or 2 to choose your first step.""")

        try:
            main_menu_choice = int(input('>>> '))
            if main_menu_choice == 1:
                print_slowly(
                    """
        There's no time to make posters right now. 
                    
        Your cat could still be close by!
                    
        Try again...""")
                time.sleep(1)
            elif main_menu_choice == 2:
                print_slowly(
                    """
        Good choice! Let's check outside...""")
                time.sleep(1)
                look_outside()
        except ValueError:
            print("Please enter a valid number (1 or 2).")


def look_outside():
    while True:
        print("""
        Outside, you have many options to look for your cat. 
        Choose wisely or you'll lose time to find her!
            
        Where do you look first? 
            
            1. At your neighbor's home.
            
            2. Under the stairs leading to your front door.  
            
            3. In the landscaping shrubs. 
            
            4. Under the vehicles in the driveway.
        
        Type 1, 2, 3, or 4 to choose your first step.
            
            """)

        try:
            look_outside_choice = int(input('>>> '))
            if look_outside_choice == 1:
                print_slowly("""
        Your neighbors don't have her!
            
        Try again...""")
                time.sleep(1)
            elif look_outside_choice == 2:
                print_slowly("""
        There she is!""")
                time.sleep(1)
                under_the_stairs()
            elif look_outside_choice == 3:
                print_slowly("""
        She's not in the landscaping!
                             
        Try again...""")
                time.sleep(1)
            elif look_outside_choice == 4:
                print_slowly("""
        She's not under any of vehicles!
                             
        Try again...""")
                time.sleep(1)
            else:
                print_slowly("Please enter a valid number (1, 2, 3, or 4).")
        except ValueError:
            print_slowly("Please enter a valid number (1, 2, 3, or 4).")


def under_the_stairs():
    while True:
        print("""
        Your cat didn't go far from her home after all. 
              
        How do you get your cat out from under the stairs?
            
            1. Use treats. 
            2. Use her favorite toy.""")

        try:
            under_the_stairs = int(input('>>> '))
            if under_the_stairs == 1:
                print_slowly(
                    """
        Good pick...your cat is obsessed with treats. 
            
        You grab your cat as soon as she's close enough and take her back inside. 
            
        You've beat the game - congrats!""")
                exit()
            elif under_the_stairs == 2:
                print_slowly("""
        She's too scared to play with her favorite toy.
                      
        Try again...""")
            time.sleep(1)
        except ValueError:
            print_slowly("Please enter a valid number (1 or 2).")


if __name__ == "__main__":
    start_game()
