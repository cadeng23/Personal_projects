

def choose_color():
    picked = input("Please select white or black pieces (w/b): ").upper()
    if picked == 'B':
        print('black pieces selected')
    if picked == 'W':
        print('white pieces selected')
    else:
        print("Not recognized please try again.")
        choose_color()
    return picked