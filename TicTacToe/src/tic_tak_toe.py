import os

from .gamemodes import pvc, pvp


def get_gamemode():
    os.system("clear")
    res = ["Pick Gamemode:\n", "1. Player vs Player", "2. Player vs Computer"]
    print("\n".join(res))

    choice = int(input("Your Choice: "))

    if choice != 1 and choice != 2:
        return get_gamemode()

    return "pvp" if choice == 1 else "pvc"


def main():
    game = pvp.PVP() if get_gamemode() == "pvp" else pvc.PVC()
    game.play()


if __name__ == "__main__":
    main()
