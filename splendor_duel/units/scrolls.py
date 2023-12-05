class ScrollDescriptor:
    def __init__(self, initial=3):
        self.value = initial

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Scroll count cannot be negative.")
        self.value = value
