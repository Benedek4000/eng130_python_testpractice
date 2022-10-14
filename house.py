from accommodation import Accommodation


class House(Accommodation):

    def __init__(self, loc, rooms=6, kitchen_size=8):
        super().__init__(loc=loc)
        self.rooms = rooms
        self.kitchen_size = kitchen_size

    def refurbish(self):
        if self.rooms > 5 and self.kitchen_size > 8:
            return "no refurbishment needed"
        else:
            return "yeah, you might wanna refurbish this house"

    def buy(self):
        return f"you may buy this house for {self.rooms+0.5*self.kitchen_size} giraffes"
