class GemDescriptor:
    def __init__(self, initial):
        self.value = initial

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            print("Gem count cannot be negative. Set to 0.")
            self.value = 0
        elif value > 5:
            print('pay attention if there are cards, otherwise you are making mistakes.')
        self.value = value


class Gems:
    black = GemDescriptor(4)
    white = GemDescriptor(4)
    green = GemDescriptor(4)
    blue = GemDescriptor(4)
    red = GemDescriptor(4)
    gold = GemDescriptor(3)
    pearl = GemDescriptor(2)

    def __add__(self, other):
        result = Gems()
        for color in ['black', 'white', 'green', 'blue', 'red', 'gold', 'pearl']:
            setattr(result, color, getattr(self, color) + getattr(other, color))
        return result

    def __sub__(self, other):
        result = Gems()
        for color in ['black', 'white', 'green', 'blue', 'red', 'gold', 'pearl']:
            setattr(result, color, getattr(self, color) - getattr(other, color))
        return result

    def __repr__(self):
        return f"""black: {self.black}\nwhite: {self.white}\ngreen: {self.green}
blue: {self.blue}\nred: {self.red}\ngold: {self.gold}\npearl: {self.pearl}\n"""

    def __str__(self):
        return self.__repr__()
