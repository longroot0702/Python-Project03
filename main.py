'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 22] File Version 0.1
'''

import os, re, codecs

# Print Menu
def menu():
    print("---------------------Menu---------------------\n")
    print("1. Collect particular character's dialogue")
    print("2. Make a list of characters")
    print("3. Collect stage directions")
    print("4. Collect dialogue included particular word")
    print("5. Exit")
    print("----------------------------------------------")

# Collect particular character's dialogue
def collectPartiCharDia():
    pass

# Make a list of characters
def makeListOfChar():
    pass

# Collect stage directions
def collectStageDia():
    pass

# Collect dialogue included particular word
def collectDiaPartiWord():
    pass

while True:
    menu()

    try:
        choice = int(input("\nSelect the menu: "))
    except ValueError:
        print("\nError: Illegal Selection..\n")
    else:
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            exit()
        else:
            print("\nError: Illegal Selection..\n")