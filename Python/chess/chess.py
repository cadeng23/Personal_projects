
StartArray =     [['Wrook1','Wknight1','Wbishop1','Wqueen','Wking' ,'Wbishop2','Wknight3','Wrook2'],
                  ['Wpawn1','Wpawn2'  ,'Wpawn3'  ,'Wpawn4','Wpawn5','Wpawn6'  ,'Wpawn7'  ,'Wpawn8'],
                  [''      ,''        ,''        ,''      ,''      ,''        ,''        ,''      ],
                  [''      ,''        ,''        ,''      ,''      ,''        ,''        ,''      ],
                  [''      ,''        ,''        ,''      ,''      ,''        ,''        ,''      ],
                  [''      ,''        ,''        ,''      ,''      ,''        ,''        ,''      ],
                  ['Bpawn1','Bpawn2'  ,'Bpawn3'  ,'Bpawn4','Bpawn5','Bpawn6'  ,'Bpawn7'  ,'Bpawn8'],
                  ['Brook1','Bknight1','Bbishop1','Bking' ,'Bqueen','Bbishop2','Bknight3','Brook2']]


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
    print(StartArray)
       # for y in StartArray:
            #if StartArray[x[y]] == 'Wrook1':
               # print(Pieces[2])

def main():
    layout()
main()

if "__name__" == '__main__':
    main()

