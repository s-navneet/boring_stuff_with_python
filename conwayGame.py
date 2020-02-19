import random,copy
import time
width=60
height=20
#create a list of the list for the cell
nextCell=[]
for x in range(width):
    column=[]
    for y in range(height):
        if(random.randint(0,1)==0):
            column.append('#') #next cell is a list of column list
        else:
            column.append('')
    nextCell.append(column)
while(True):
    print('\n\n\n\n\n')
    currentCell=copy.deepcopy(nextCell)
    #print current cell on the Screen
    for x in range(height):
        for y in range(width):
            print(currentCell[x][y], end='')
            print(' ')
    #calculate the next step cell based on current step cell
    for x in range(width):
        for y in range(height):
            #get neighbour cordinate
            leftcord=(x-1)%width
            rightcord=(x+1)%width
            abovecord=(y-1)%height
            belowcord=(y+1)%height
            numnbhr=0
            if(currentCell[leftcord][abovecord]=='#'):
                numnbhr+=1
            if(currentCell[x][abovecord]=='#'):
                numnbhr+=1
            if(currentCell[rightcord][abovecord]=='#'):
                numnbhr+=1
            if(currentCell[leftcord][y]=='#'):
                numnbhr+=1
            if(currentCell[rightcord][y]=='#'):
                numnbhr+=1
            if(currentCell[leftcord][belowcord]=='#'):
                numnbhr+=1
            if(currentCell[x][belowcord]=='#'):
                numnbhr+=1
            if(currentCell[rightcord][belowcord]=='#'):
                numnbhr+=1
            if(currentCell[x][y]=='#' and numnbhr == 2 or numnbhr == 3):
                nextCell[x][y]='#'
            elif(currentCell[x][y] == '' and numnbhr == 3):
                nextCell[x][y]='#'
            else:
                nextCell[x][y]=''
time.sleep(1)


