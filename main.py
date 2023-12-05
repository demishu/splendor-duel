import splendor_duel as sd
board = sd.Board()
Gems = sd.Gems
gems1 = Gems()
gems2 = Gems()

for i, color in enumerate(['black', 'white', 'green', 'blue', 'red', 'gold', 'pearl'], 0):
    setattr(gems1, color, i)
    setattr(gems2, color, 0)
print(gems1 - gems2)
