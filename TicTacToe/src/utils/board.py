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

    def make_move(self, x_coords, y_coords, character):
        self.board[x_coords][y_coords] = character

    def isFilled(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

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
            [(0, 2), (1, 1), (2, 0)],
        ]

        for pattern in PATTERNS:
            if (
                self.board[pattern[0][0]][pattern[0][1]] != " "
                and self.board[pattern[0][0]][pattern[0][1]]
                == self.board[pattern[1][0]][pattern[1][1]]
                == self.board[pattern[2][0]][pattern[2][1]]
            ):
                return 1 if self.board[pattern[0][0]][pattern[0][1]] == "X" else -1

        if self.isFilled():
            return 0
        else:
            return None


if __name__ == "__main__":
    board = Board()
    board.print_board()
