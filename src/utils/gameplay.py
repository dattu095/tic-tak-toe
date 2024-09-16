import board
import os


class GamePlay:
    player_change = {"PlayerX": "X", "PlayerO": "O"}

    def __init__(self):
        self.board = board.Board()
        self.player = "PlayerX"

    def get_coords(self):
        while True:
            print("give the coords the square picked(x, y):", end=" ")
            coords = input().split(",")
            x, y = int(coords[0]) - 1, int(coords[1]) - 1

            if len(coords) == 2:
                if self.board.coordIsValid(x, y):
                    return x, y
                else:
                    print("Non Valid Coords!")
            else:
                print()
                print("WRONG FORMAT!")

    def gui(self):
        os.system("clear")
        self.board.print_board()

        print()
        print(f"{self.player}'s turn")

        return self.get_coords()

    def turn(self):
        x, y = self.gui()

        self.board.update_board(x, y, self.player_change[self.player]) 
        if isinstance(self.board.checkWin(), int):
            os.system("clear")
            winner = self.board.checkWin()
            if winner == 1:
                print("X won")
            elif winner == -1:
                print("O won")
            elif winner == 0:
                print("Draw")

            return False

        self.player = "PlayerX" if (self.player == "PlayerO") else "PlayerO"
        return True

    def play(self):
        flag = True
        while flag:
            flag = self.turn()


if __name__ == "__main__":
    game = GamePlay()
    game.play()
