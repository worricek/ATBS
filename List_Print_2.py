grid=[['.','.','.','.','.','.'],
          ['.','0','0','.','.','.'],
          ['0','0','0','0','.','.'],
          ['0','0','0','0','0','.'],
          ['.','0','0','0','0','0'],
          ['0','0','0','0','0','.'],
          ['0','0','0','0','.','.'],
          ['.','0','0','.','.','.'],
          ['.','.','.','.','.','.']]
 
y=0 
i=0
while True:
    while True:
        row=grid[y][i]
        #print(y, i)
        print(*row, end="", sep=".")
        if y==8:
            y=0
            break
        y+=1
    if i==5:
        break
    i+=1
    print()

#column=0
#place=grid[0][0]
#print(place)
#i=0
#i=grid[1, 0]
#print(i)
#print(*grid, sep=",\n")
