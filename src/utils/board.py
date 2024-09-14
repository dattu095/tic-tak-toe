class Board:
    def __init__(self):
        self.board = [[" ", " ", " "] for i in range(3)]

    def print_board(self):
        print("x\\y 1   2   3  ")
        print("   -------------")
        print("   |   |   |   |")
        print(
            f" 1 | {self.board[0][0]} | {
                self.board[0][1]} | {self.board[0][2]} |"
        )
        print("   |   |   |   |")
        print("   -------------")
        print("   |   |   |   |")
        print(
            f" 2 | {self.board[1][0]} | {
                self.board[1][1]} | {self.board[1][2]} |"
        )
        print("   |   |   |   |")
        print("   -------------")
        print("   |   |   |   |")
        print(
            f" 3 | {self.board[2][0]} | {
                self.board[2][1]} | {self.board[2][2]} |"
        )
        print("   |   |   |   |")
        print("   -------------")

    def coordIsValid(self, x, y):
        if (0 <= x <= 2) and (0 <= y <= 2):
            if self.board[x][y] == " ":
                return True
        return False

    def update_board(self, x_coords, y_coords, character):
        self.board[x_coords][y_coords] = character

    def checkWin(self):
        PATTERNS = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],

            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        
        pass


if __name__ == "__main__":
    board = Board()
    board.print_board()
