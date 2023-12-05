from ..units import Gems, ScrollDescriptor


class GemsBoard:
    gems = Gems()


class GemsBag:
    gems = Gems()  # at the beginning of game, they will be cleaned in the splendor_duel/game/game.py


class CardsBoard:
    def __get__(self):
        pass

    def __set__(self):
        pass


class Board:
    scrolls = ScrollDescriptor(3)
    gems_board = GemsBoard()
    gems_bag = GemsBag()
    cards_board = CardsBoard()
