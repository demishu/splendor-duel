from ..players import Player
from ..board import Board
from ..units import Gems
player1 = Player()
player2 = Player()
board = Board()

# at the beginning, all the gems are on the board
for color in ['black', 'white', 'green', 'blue', 'red', 'gold', 'pearl']:
    setattr(player1.gems, color, 0)
    setattr(player2.gems, color, 0)
    setattr(board.gems_board.gems, color, getattr(Gems, color).value)
    setattr(board.gems_bag.gems, color, getattr(Gems, color).value)


# 玩家可以从场地上收集宝石，然后放入他们的袋子里
def collect_gem(player, colors):
    for color in colors:
        if color:   # if None will be passed.
            if getattr(board.gems, color) > 0:
                setattr(board.gems, color, getattr(board.gems, color) - 1)
                setattr(player.gems, color, getattr(player.gems, color) + 1)
            else:
                print("No more", color, "gems available on the board.")


# 玩家可以把他们袋子里的宝石放回到场地上
def return_gem_to_bag(player, color):
    if getattr(player.gems, color) > 0:
        setattr(player.gems, color, getattr(player.gems, color) - 1)
        setattr(board.gems_bag.gems, color, getattr(board.gems_bag.gems, color) + 1)
    else:
        print("No more", color, "gems available in the bag.")


# 玩家可以清空他们的袋子，把所有的宝石放回到场地上
def empty_bag():
    for color in ['black', 'white', 'green', 'blue', 'red', 'gold', 'pearl']:
        setattr(board.gems, color, getattr(board.gems, color) + getattr(board.gems_bag.gems, color))
        setattr(board.gems_bag.gems, color, 0)

