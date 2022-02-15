from readFilms import *
from addFilms import *
from updateFilms import *
from deleteFilms import *
from searchFilms import *


def menUOptions():
    options = 0
    # check for the value 0 in the list
    while options not in ["1","2","3","4","5","6"]:
        print("\nMenu Options")
        print("1. Print all film Records")
        print("2. Add a new film")
        print("3. Update film record")
        print("4. Search for a film record")
        print("5. Delete a film record")
        print("6. Exit")
        
        options = input("\nEnter one of the options above: ")
        if options not in ["1","2","3","4","5", "6"]:
            print("Not in the list of options available")
    return options

mainProgram = True

while mainProgram == True:
    
    mainMenu = menUOptions()
    print(mainMenu)

    if mainMenu == "1":
        displayFilms()
    elif mainMenu == "2":
        addFilms()
    elif mainMenu == "3":
        update()
    elif mainMenu == "4":
        searchTitle()
        
    elif mainMenu == "5":
        delRecord()
    else:
        mainProgram = False

input("Press enter to exit")

