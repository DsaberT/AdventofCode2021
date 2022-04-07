#Creat a matrix for the OctoCave reading text file
def CaveMatrix(txtfile):
    matrix = []
    textdata =  open(txtfile)
    text = textdata.read()

    for line in text.split('\n'):
        row = []
        for character in line:
            if character != ('\n'):
                row.append(int(character))
        matrix.append(row)
    return matrix


def ValidationCheck(matrix,NextXpos, NextYpos):
    # Makes sure that we don't move in negative direction in a matrix
    # We don't overwrite a 0 to make sure its there the entire loop
    # Also makes sure that we are not looking at position outside the matrix
    if (NextXpos >= 0 and NextYpos >= 0 and NextXpos < (len(matrix)) and NextYpos < (len(matrix[NextXpos]))):
           if matrix[NextXpos][NextYpos] != 0:
               return True
    return False
    #We don't overwrite a 0 to make sure its there the entire loop




#Increment one step in each direction from position
def FlashCasacade(matrix, Xposition, Yposition):
    for x in [-1, 0 ,1]:
        for y in [-1, 0, 1]:
            nextXposition = Xposition + x
            nextYposition = Yposition + y
            if ValidationCheck(matrix,nextXposition,nextYposition):        # Checks syntax problems
                matrix[nextXposition][nextYposition] +=1
    return matrix


#Increment each octopus with 1 energy point
def NextStep(matrix):
    for RowCounter in range(len(matrix)):
        for ColumnCounter in range(len(matrix[RowCounter])):
            matrix[RowCounter][ColumnCounter] +=1
    return Flashing(matrix)

def Flashing(matrix):
    NumFlashes = 0
    FlashList = []
    for RowCounter in range(len(matrix)):
        for ColumnCounter in range(len(matrix[RowCounter])):
            if matrix[RowCounter][ColumnCounter] >9:
                NumFlashes += 1                                     # Count flashes
                matrix[RowCounter][ColumnCounter] = 0               # RESET
                FlashList.append((RowCounter,ColumnCounter))        # Add all octopus that are flashing
    if FlashList != []:                                             # looks if there was any flashing this loop
        for (X,Y) in FlashList:
            FlashCasacade(matrix,X,Y)                               # Sends in the list with all flashing positions
        return (NumFlashes + Flashing(matrix))
    return NumFlashes

def main():
    NumFlashes = 0
    matrix = CaveMatrix("AdventofcodeCave.txt")
    for i in range(100):                        #Runs X loops
        NumFlashes += NextStep(matrix)
    print("Total number of Falshes for "+ str(i+1)+" steps is "+str(NumFlashes))

main()
