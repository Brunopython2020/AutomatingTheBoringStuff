import random, time, copy



width = 60
height  = 20

#create a list of list for cells

next_cells = []

for x in range(width):
    column = [] #create a new column

    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') #add a living cell
        else:
            column.append(' ') #add a dead cell
        
    next_cells.append(column) #next_cells is a list of column lists.


while True: #Main program loop
    print('\n\n\n\n\n') #separate each steps with new lines
    current_cells = copy.deepcopy(next_cells)

    #Print current cells on the screen

    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end='') #print  the # or ' '.
        print() # print a new line at the end of the row.

    #Calculates the next step's cells based on the current step's cells:

    for x in range(width):
        for y in range(height):
            #get neighboring coordinates:
            # '% width' ensures leftcoord is always between 0 and width - 1
            left_coord = (x - 1) % width
            right_coord = (x + 1) % width
            above_coord = (y + 1) % height
            below_coord = (y - 1) % height

            #count the number of living neighbors
            num_neighbors = 0
            
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1 #top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1 #top neighbor is alive
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1 #top right neighbor is alive
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1 #left neighbor is alive
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1 #right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 # Bottom-left neighbor is alive.
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1 #bottom neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 #bottom-right neighbor is alive


            #set cell based on Conway's game rule

            if current_cells[x][y] == '#' and (num_neighbors == 3 or num_neighbors == 2):
                #living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and (num_neighbors == 3):
                #dead cells with 3 neighbors become alive
                next_cells[x][y] = '#'
            else:
                #everything else dies or stays dead
                next_cells[x][y] = ' '

    time.sleep(1) #pause to reduce flickering
          
