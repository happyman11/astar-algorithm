import algorithm as AL
def main():
   ''' In grid the representation are as follows
       1 -> the blocked paths
       0 -> the avalable path
       9->  the selected path
   
   '''
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    StartNode = (0, 0)
    
    EndNode = (0, 9)
    print("Running...")
    layout = AL.algorithm(grid, StartNode, EndNode)
    path=grid
    for i in range(0,9):
        for j in range(0,9):
            pass
    print(layout)


if __name__ == '__main__':
    main()
