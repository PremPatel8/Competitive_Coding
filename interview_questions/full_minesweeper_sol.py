import random

class Minesweeper:
    def __init__(self, rows=9, cols=9, num_mines=10):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        
        # Initialize boards
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visible = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        
        # Place mines and calculate numbers
        self._place_mines()
        self._calculate_numbers()
        
        self.game_over = False
        self.won = False
        
    def _place_mines(self):
        """Randomly place mines on the board."""
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            
            if self.board[row][col] != -1:  # -1 represents a mine
                self.board[row][col] = -1
                mines_placed += 1
    
    def _calculate_numbers(self):
        """Calculate numbers for cells adjacent to mines."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue
                
                # Count adjacent mines
                mine_count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.board[nr][nc] == -1:
                                mine_count += 1
                
                self.board[row][col] = mine_count
    
    def _get_neighbors(self, row, col):
        """Get valid neighbor coordinates."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))
        
        return neighbors
    
    def _reveal_cells(self, row, col):
        """Recursively reveal cells using flood-fill algorithm."""
        # Base cases
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        if self.visible[row][col] or self.flagged[row][col]:
            return
        
        # Reveal current cell
        self.visible[row][col] = True
        
        # If it's a mine or numbered cell, stop here
        if self.board[row][col] != 0:
            return
        
        # If it's empty (0), recursively reveal neighbors
        for nr, nc in self._get_neighbors(row, col):
            self._reveal_cells(nr, nc)
    
    def reveal(self, row, col):
        """Reveal a cell at the given position."""
        if self.game_over:
            return False
        
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print("Invalid position!")
            return True
        
        if self.visible[row][col] or self.flagged[row][col]:
            print("Cell already revealed or flagged!")
            return True
        
        # Check if it's a mine
        if self.board[row][col] == -1:
            self.visible[row][col] = True
            self.game_over = True
            return False
        
        # Reveal cell(s)
        self._reveal_cells(row, col)
        
        # Check win condition
        if self._check_win():
            self.won = True
            self.game_over = True
        
        return True
    
    def toggle_flag(self, row, col):
        """Toggle flag on a cell."""
        if self.game_over:
            return
        
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print("Invalid position!")
            return
        
        if self.visible[row][col]:
            print("Cannot flag a revealed cell!")
            return
        
        self.flagged[row][col] = not self.flagged[row][col]
    
    def _check_win(self):
        """Check if the player has won."""
        for row in range(self.rows):
            for col in range(self.cols):
                # If a non-mine cell is not visible, game is not won
                if self.board[row][col] != -1 and not self.visible[row][col]:
                    return False
        return True
    
    def display(self, reveal_all=False):
        """Display the current board state."""
        
        print("\n   ", end="")
        # Prints the column indexes 0  1  2  3  4  5  6  7  8
        for col in range(self.cols):
            # {col:2} formats column number with 2-character width for alignment
            # end=" " prevents newline after each print
            print(f"{col:2}", end=" ")
        
        print("\n   " + "---" * self.cols)
        
        for row in range(self.rows):
            # Prints row number left-aligned with 2-character width and a pipe char after it (|) e.g - 2|
            print(f"{row:2}|", end=" ")
            
            # Prints each cell for this row
            for col in range(self.cols):
                if reveal_all or self.visible[row][col]:
                    cell = self.board[row][col]
                    if cell == -1:
                        # mine
                        print(" *", end=" ")
                    elif cell == 0:
                        # empty cell
                        print(" .", end=" ")
                    else:
                        print(f"{cell:2}", end=" ")
                elif self.flagged[row][col]:
                    print(" F", end=" ")
                else:
                    # hidden
                    print(" #", end=" ")
            print()
        print()


def main():
    print("=== MINESWEEPER ===\n")
    
    # Get board size and mine count
    try:
        rows = int(input("Enter number of rows (default 9): ") or "9")
        cols = int(input("Enter number of columns (default 9): ") or "9")
        mines = int(input("Enter number of mines (default 10): ") or "10")
    except ValueError:
        print("Invalid input. Using default values.")
        rows, cols, mines = 9, 9, 10
    
    game = Minesweeper(rows, cols, mines)
    
    print("\nCommands:")
    print("  r <row> <col> - Reveal cell")
    print("  f <row> <col> - Toggle flag")
    print("  q - Quit\n")
    
    while not game.game_over:
        game.display()
        
        try:
            command = input("Enter command: ").strip().lower().split()
            
            if not command:
                continue
            
            if command[0] == 'q':
                print("Thanks for playing!")
                break
            
            if len(command) != 3:
                print("Invalid command format!")
                continue
            
            action = command[0]
            row = int(command[1])
            col = int(command[2])
            
            if action == 'r':
                if not game.reveal(row, col):
                    game.display(reveal_all=True)
                    print("💥 GAME OVER! You hit a mine!")
                    break
            elif action == 'f':
                game.toggle_flag(row, col)
            else:
                print("Invalid command! Use 'r' to reveal or 'f' to flag.")
        
        except (ValueError, IndexError):
            print("Invalid input! Use format: r <row> <col> or f <row> <col>")
    
    if game.won:
        game.display()
        print("🎉 CONGRATULATIONS! You won!")


"""
To run this script either 
1 - Click the drop down next to the run button and click "Run Python file in dedicated terminal"
OR
2 - Open terminal, wait for the venv activation script to execute and type python D:\GitHub\Competitive_Coding\interview_questions\full_minesweeper_sol.py
"""
if __name__ == '__main__':
    main()