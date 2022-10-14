from house import House


class SMHouse(House):

    def __init__(self, loc="next to the neighbour", neighbour="Joe"):
        super().__init__(loc)
        self.neighbour_name = neighbour

    def separate(self):
        return f"{self.neighbour_name} has a bad taste in music"


new_house = SMHouse(loc="next to Joe's zoo")
print(new_house.enter())
print(new_house.demolish())
print(new_house.show_location())
print(new_house.refurbish())
print(new_house.buy())
print(new_house.separate())
