#Size
Caden = [0,0]
Mitchell = [0,0]
Izzy = [0,0]
MasonG = [0,0]
Sanges = [0,0]
#Stamina
Nick = [0,0]
Tanner = [0,0]
Mason = [0,0]
Silva = [0,0]
Chaison = [0,0]

#All Players
Players = [Caden,Mitchell,Izzy,MasonG,Sanges,Nick,Tanner,Mason,Silva,Chaison]
#print(Players)
#divisions
divSize = [Mitchell, MasonG,Sanges, Caden, Izzy]
divStamina =  [Nick, Tanner, Mason, Silva, Chaison]

#Matchups
Week_1 = [['Caden','Mitchell'],['Izzy','Mason'],['Sanges','MasonG'],['Silva','Nick'],['Tanner','Chaison']]
Week_2 = [['Sanges','Mitchell'],['Tanner','Mason'],['Caden','Silva'],['Izzy','MasonG'],['Chaison','Nick']]
Week_3 = [['Caden','Izzy'],['Mitchell','MasonG'],['Silva','Mason'],['Chaison','Sanges'],['Tanner','Nick']]
Week_4 = [['Caden','Chaison'],['Mason','Mitchell'],['MasonG','Nick'],['Izzy','Silva'],['Tanner','Sanges']]
Week_5 = [['Caden','Tanner'],['Silva','Mitchell'],['MasonG','Mason'],['Sanges','Nick'],['Izzy','Chaison']]
Week_6 = [['Caden','Sanges'],['Izzy','Mitchell'],['Mason','Nick'],['Tanner','MasonG'],['Chaison','Silva']]
Week_7 = [['Caden','MasonG'],['Nick','Mitchell'],['Chaison','Mason'],['Tanner','Silva'],['Izzy','Sanges']]
Week_8 = [['Caden','Mitchell'],['Mason','Nick'],['Sanges','MasonG'],['Chaison','Silva'],['Izzy','Tanner']]
Week_9 = [['Caden','Mason'],['Tanner','Mitchell'],['Chaison','MasonG'],['Sanges','Silva'],['Izzy','Nick']]
Week_10 = [['Caden','Nick'],['Chaison','Mitchell'],['Sanges','Mason'],['Silva','MasonG'],['Izzy','Tanner']]
Week_11 = [['Chaison','Caden'],['Sanges','Mitchell'],['Tanner','Mason'],['Izzy','MasonG'],['Silva','Nick']]
Week_12 = [['Caden','Izzy'],['MasonG','Mitchell'],['Chaison','Mason'],['Sanges','Silva'],['Tanner','Nick']]
Week_13 = [['Caden','Sanges'],['Izzy','Mitchell'],['MasonG','Mason'],['Tanner','Silva'],['Chaison','Nick']]
Week_14 = [['Caden','MasonG'],['Nick','Mitchell'],['Silva','Mason'],['Izzy','Sanges'],['Tanner','Chaison']]

Week1 = [[Caden,Mitchell],[Izzy,Mason],[Sanges,MasonG],[Silva,Nick],[Tanner,Chaison]]
Week2 = [[Sanges,Mitchell],[Tanner,Mason],[Caden,Silva],[Izzy,MasonG],[Chaison,Nick]]
Week3 = [[Caden,Izzy],[Mitchell,MasonG],[Silva,Mason],[Chaison,Sanges],[Tanner,Nick]]
Week4 = [[Caden,Chaison],[Mason,Mitchell],[MasonG,Nick],[Izzy,Silva],[Tanner,Sanges]]
Week5 = [[Caden,Tanner],[Silva,Mitchell],[MasonG,Mason],[Sanges,Nick],[Izzy,Chaison]]
Week6 = [[Caden,Sanges],[Izzy,Mitchell],[Mason,Nick],[Tanner,MasonG],[Chaison,Silva]]
Week7 = [[Caden,MasonG],[Nick,Mitchell],[Chaison,Mason],[Tanner,Silva],[Izzy,Sanges]]
Week8 = [[Caden,Mitchell],[Mason,Nick],[Sanges,MasonG],[Chaison,Silva],[Izzy,Tanner]]
Week9 = [[Caden,Mason],[Tanner,Mitchell],[Chaison,MasonG],[Sanges,Silva],[Izzy,Nick]]
Week10 = [[Caden,Nick],[Chaison,Mitchell],[Sanges,Mason],[Silva,MasonG],[Izzy,Tanner]]
Week11 = [[Chaison,Caden],[Sanges,Mitchell],[Tanner,Mason],[Izzy,MasonG],[Silva,Nick]]
Week12 = [[Caden,Izzy],[MasonG,Mitchell],[Chaison,Mason],[Sanges,Silva],[Tanner,Nick]]
Week13 = [[Caden,Sanges],[Izzy,Mitchell],[MasonG,Mason],[Tanner,Silva],[Chaison,Nick]]
Week14 = [[Caden,MasonG],[Nick,Mitchell],[Silva,Mason],[Izzy,Sanges],[Tanner,Chaison]]

#Matchup Array
WeeklyNames = [Week_1,Week_2,Week_3,Week_4,Week_5,Week_6,Week_7,Week_8,Week_9,Week_10,Week_11,Week_12,
Week_13,Week_14]

WeekRec = [Week1,Week2,Week3,Week4,Week5,Week6,Week7,Week8,Week9,Week10,Week11,Week12,
Week13,Week14]

#print(WeeklyMatches)
d = '          '
#Cases each week
def checkWk(Players,Wk):
    print('---------------------------------------------------')
    print('What happened this week?: ')
    
    print('Case 1:')
    print('\n')
    print(Wk[0][0],': W', end = d)
    print(Wk[1][0],': W')
    #print(Wk[0][1],': L', end = d)
    #print(Wk[1][1],': L')
    print('\n')
    print(Wk[2][0],': W',end = d)
    print(Wk[3][0], ': W')
    #print(Wk[2][1],': L', end = d)
    #print(Wk[3][1],': L')
    print('\n')
    print(Wk[4][0],': W')
    #print(Wk[4][1],': L')
    


def main():
    for x in WeeklyNames:
        Wk = x
        checkWk(Players, Wk)

main()