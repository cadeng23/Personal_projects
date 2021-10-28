
board =     [['R','N','B','Q','K','B','N','R'],
                  ['P','P','P','P','P','P','P','P'],
                  ['-','-','-','-','-','-','-','-'],
                  ['-','-','-','-','-','-','-','-'],
                  ['-','-','-','-','-','-','-','-'],
                  ['-','-','-','-','-','-','-','-'],
                  ['p','p','p','p','p','p','p','p'],
                  ['r','n','b','k','q','b','n','r']]

print(board)
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

def pieces():
    Piece_color = [
                        '''
                        {\W-Pawn}
                        ''',
                        '''
                        |W-Rook|
                        ''',
                        '''
                        $W-Knight$
                        ''',
                        '''
                        &W-Bishop&
                        ''',
                        '''
                        **W-Queen**
                        ''',
                        '''
                        #_W-King_#
                        ''',
                        '''
                        {\B-Pawn}
                        ''',
                        '''
                        |B-Rook|
                        ''',
                        '''
                        $B-Knight$
                        ''',
                        '''
                        &B-Bishop&
                        ''',
                        '''
                        **B-Queen**
                        ''',
                        '''
                        #_B-King_#
                        '''
                 ]
    return Piece_color
def layout():
    Pieces = pieces()
    #for x in StartArray:
    print(board)
       # for y in StartArray:
            #if StartArray[x[y]] == 'Wrook1':
               # print(Pieces[2])

#def main():
#    layout()
#main()

#if "__name__" == '__main__':
#    main()

