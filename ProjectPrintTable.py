#! /usr/bin/python3

tableData	=	[['apples',	'oranges',	'cherries',	'banana'],
                    ['Alice',	'Bob',	'Carol',	'David'],
					['dogs',	'cats',	'moose',	'goose']]

colWidths	=	[0]	*	len(tableData)


def printTable(tableStuff, rightAlignment):
    y=0
    x=0
    while True:
        if x==len(tableStuff):
            break
        while True:
            if y==len(tableStuff[x])-1:
                y=0
                break
            row=tableStuff[y][x]
 #           print(*row, end="", sep=".")
            print(*row.rjust(rightAlignment[y]), end=" ", sep="")
            y+=1
        print('\n')
        x+=1

j=0
for list in tableData:
    i=0
    for number in list:
        if len(number) > i:
            i=len(number)
    colWidths[j]=i
    j+=1

printTable(tableData, colWidths)
    
    
