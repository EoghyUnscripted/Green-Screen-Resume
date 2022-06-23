from Modules import builder as build, menus as menu, data

string = "Hello! My name is Eoghan. It is nice to meet you!"

data.typewriter(f"Hello! My name is Eoghan. It is nice to meet you!\n"
                + f"Welcome to my interactive resume.")

data.snooze()

interaction = True

while interaction:
    
    try:
        
        data.typewriter(f"Make a selection by typing a number or quit to end program:\n")
    
        menu.printer()
        
        selection = input(f"\n")
        
        int(selection)
        
    except ValueError:
        
        if selection == "quit":
            data.typewriter("Exiting... Goodbye!")
            interaction = False
            break
        
        else:
            print("Sorry, you must enter a number.")
    
    else:

        build.get_function(int(selection))
        continue