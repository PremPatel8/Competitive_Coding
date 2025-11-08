
"""
board = 3 * 3
number, mine
number - no. bmbs in adjacent squares
row, col 
bomb - -1
tile value - 1,2,3,4
bomb - 1, 3
"""
class Play:
    def __init__(self):
        self.boardActual = [[1,-1, 1],
                            [0, 1, 0],
                            [0, 0, 0]]
                        
        self.boardHidden = [['*','*','*'],
                            ['*','*','*'],
                            ['*','*','*']]
                            
    def revealNeighbors(self, row, col):
        # update the current empty cell
        self.boardHidden[row][col] = self.boardActual[row][col]
    
        neigbor_coordinates = [(row-1, col-1),(row-1, col),(row-1, col+1),(row, col+1),(row, col-1),(row+1,col+1),(row+1, col),(row+1, col-1),(row, col-1)]
        
        for row, col in neigbor_coordinates:
            if 0 <= row < len(self.boardHidden) and 0 <= col < len(self.boardHidden):
                cell_value = self.boardActual[row][col]
                
                if cell_value > 0:
                    self.boardHidden[row][col] = self.boardActual[row][col]
                    return
                if cell_value < 0:
                    return
                else:
                    self.revealNeighbors(row, col)
    
    
    def checkPosition(self, row, col):
        # Empty cell
        if self.boardActual[row][col] == 0:
            self.revealNeighbors(row, col)
            return True
        
        # Mine cell
        if self.boardActual[row][col] == -1:
            self.boardHidden[row][col] = self.boardActual[row][col]
            return False
            
        # Number cell
        if self.boardActual[row][col] > 0:
            self.boardHidden[row][col] = self.boardActual[row][col]
            return True
            
        
    def displayUpdatedBoard(self):
        for row in range(len(self.boardHidden)):
            print("\n")
            for col in range(len(self.boardHidden)):
                print(self.boardHidden[row][col], end=" ")
        
        print("\n")
        


def main():
    obj = Play()
    state = True
    obj.displayUpdatedBoard()
    
    while state:
        row = input("Enter row:\n")
        col = input("Enter col:\n")
        
        state = obj.checkPosition(int(row), int(col))
        
        if state == False:
            print("\n!!!GAME OVER!!!")
        
        obj.displayUpdatedBoard()
    
    
if __name__ == '__main__':
    main()