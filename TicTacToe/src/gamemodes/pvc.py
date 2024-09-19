import os

from .pvp import PVP
from ..utils.minimax import get_best_move


class PVC(PVP):
    def __init__(self):
        super().__init__()
        self.player_choice = self.get_choice()

    def get_choice(self):
        os.system("clear")

        res = ["Pick Option:\n", "1. PlayerX", "2. PlayerO"]

        print("\n".join(res))

        choice = int(input("Your Choice: "))

        if choice != 1 and choice != 2:
            return self.get_choice()

        return "PlayerX" if choice == 2 else "PlayerO"

    def gui_pvc(self):
        os.system("clear")
        self.board.print_board()

        print()
        print("Calculating next move...")

        return get_best_move(self.board, self.player_change[self.player])

    def comp_turn(self):
        coords = self.gui_pvc()
        x, y = coords[0], coords[1]
        return self.makeMove(x, y)

    def play(self):
        flag = True
        while flag:
            if self.player != self.player_choice:
                flag = self.player_turn()
            else:
                flag = self.comp_turn()


if __name__ == "__main__":
    game = PVC()
    game.play()
