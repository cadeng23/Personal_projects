import random
#TODO: look into NUMpy and see if that can help with the mass data analysis

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
plyrName = ['Caden','Mitchell','Izzy','MasonG','Sanges','Nick','Tanner','Mason','Silva','Chaison']
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
def checkWk(Players,Wk, current,plyrName):
    print('---------------------------------------------------')
    print('Who won week ', current, '?:')
    print('0. Caden')
    print('1. Mitchell')
    print('2. Nick')
    print('3. Silva')
    print('4. Sanges')
    print('5. Mason Green')
    print('6. Chaison')
    print('7. Izzy')
    print('8. Mason Gilgen')
    print('9. Tanner')
    winners = []
    a,b,c,d,e = input('Winners this week:').split()
    print('---------------------------------------------------')
    winners.append(a)
    winners.append(b)
    winners.append(c)
    winners.append(d)
    winners.append(e)
    for i in winners:
        if int(i) == 0:
            Players[0][0] += 1
        if int(i) == 1:
            Players[1][0] += 1
        if int(i) == 2:
            Players[5][0] += 1
        if int(i) == 3:
            Players[8][0] += 1
        if int(i) == 4:
            Players[4][0] += 1
        if int(i) == 5:
            Players[3][0] += 1
        if int(i) == 6:
            Players[9][0] += 1
        if int(i) == 7:
            Players[2][0] += 1
        if int(i) == 8:
            Players[7][0] += 1
        if int(i) == 9:
            Players[6][0] += 1
    for p in range(0,10):
        if Players[p][0] + Players[p][1] != current:
            Players[p][1] += 1
    d = 0
    for f in Players:
        print(plyrName[d], end = ' = ')
        print(f[0],end = '-')
        print(f[1])
        d += 1
    return Players
    

def runProbs(Players, current):
    left = (current - 1) * 32
    left = 448 - left
    print(left)
    #predict = Players
    for x in WeekRec:
        if x >= current:
            thisWk = WeekRec[x]
            for a in thisWk:
                put = random(1,2)
                if put == 1:
                    thisWk[0][0] += 1
                    thisWk[1][1] += 1
                if put == 2:
                    thisWk[0][1] += 1
                    thisWk[1][0] += 1
                print(thisWk[0], end = '-')
                print(thisWk[1])
                

def main():
    current = 1
    for x in WeeklyNames:
        Wk = x
        plyr = checkWk(Players, Wk, current, plyrName)
        current += 1
        print('Is week',current,'the current week?(y/n)',end = ' ')
        inp = input().upper()
        if inp == 'Y':
            runProbs(plyr,current)
            quit()
        if inp == 'N':
            continue
        #current += 1
        

main()