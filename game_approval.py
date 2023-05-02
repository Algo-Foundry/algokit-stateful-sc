from pyteal import *


def game():
    return Approve()


if __name__ == "__main__":
    game_sc = compileTeal(game(), mode=Mode.Application, version=8)
    with open("./artifacts/game_approval.teal", "w") as f:
        f.write(game_sc)
