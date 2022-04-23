'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 23] File Version 1.0
'''

import process_function

while True:
    process_function.menu()

    try:
        choice = int(input("\nSelect the menu: "))
    except ValueError:
        print("\nError: Illegal Selection..\n")
    else:
        if choice == 1:
            process_function.collectPartiCharDia()
        elif choice == 2:
            process_function.makeListOfChar()
        elif choice == 3:
            process_function.collectStageDia()
        elif choice == 4:
            process_function.collectDiaPartiWord()
        elif choice == 5:
            exit()
        else:
            print("\nError: Illegal Selection..\n")