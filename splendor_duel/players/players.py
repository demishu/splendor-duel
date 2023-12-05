from ..units import Gems, ScrollDescriptor

class Player:
    own_gems = Gems()   # at the beginning of game, they will be cleaned in the splendor_duel/game/game.py
    own_cards = Gems()  # at the beginning of game, they will be cleaned in the splendor_duel/game/game.py
    own_scrolls = ScrollDescriptor(0)
