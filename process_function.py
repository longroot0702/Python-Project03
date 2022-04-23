'''
- File Name: process_function.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 23] File Version 1.0
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
    print("----------------------------------------------\n")
    print("   [Collect particular character's dialogue]\n")
    charname = input('Please enter character\'s name: ')

    f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
    script101 = f.readlines()
    f.close()

    Line = []
    for item in script101:
        if re.match(charname + ':.+', item):
            Line += re.match(charname + ':.+', item).group()

    dialogue = ''
    for item in Line:
        dialogue += item

    if len(dialogue) == 0:
        print('\nError: Dialogue or Character is not exist...')
    else:
        f = codecs.open(charname + '.txt', 'w', encoding = 'utf-8')
        f.write(dialogue)
        f.close()
        print('\nText file is created!')
    
    print("----------------------------------------------\n")

# Make a list of characters
def makeListOfChar():
    print("----------------------------------------------\n")
    print("          [Make a list of characters]\n")
    f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
    script101 = f.read()
    f.close()

    char = list(set(re.findall(r'[A-Z][a-z]+:', script101)))

    if len(char) == 0:
        print('\nError: Dialogue or Character is not exist...')
    else:
        f = codecs.open('character.txt', 'w', encoding = 'utf-8')
        f.write('*** Warning: Please exclude particular word(Ex. All, note, ..., etc) ***\n\n')
        for item in char:
            f.write(item[:-1])
            f.write('\n')
        f.close()
        print('Text file is created!')
    
    print("----------------------------------------------\n")

# Collect stage directions
def collectStageDia():
    print("----------------------------------------------\n")
    print("          [Collect stage directions]\n")

    f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
    script101 = f.read()
    f.close()

    stage_direction = re.findall(r'\([A-Za-z].+?\)', script101)

    if len(stage_direction) == 0:
        print('\nError: Dialogue or stage_direction is not exist...')
    else:
        f = codecs.open('stage_direction.txt', 'w', encoding = 'utf-8')
        for item in stage_direction:
            f.write(item)
            f.write('\n')
        f.close()
        print('Text file is created!')
    
    print("----------------------------------------------\n")

# Collect dialogue included particular word
def collectDiaPartiWord():
    print("----------------------------------------------\n")
    print("  [Collect dialogue included particular word]\n")
    word = input('Please enter a word: ')

    f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
    script101 = f.readlines()
    f.close()

    Lines = []

    for item in script101:
        if re.match(r'[A-Z][a-z]+:', item):
            Lines += [item]

    dialogue = ''
    for item in Lines:
        if re.search(word, item):
            dialogue += item

    if len(dialogue) == 0:
        print('\nError: Dialogue or word is not exist...')
    else:
        f = codecs.open(word + '.txt', 'w', encoding = 'utf-8')
        f.write(dialogue)
        f.close()
        print('\nText file is created!')
    
    print("----------------------------------------------\n")