class Accommodation:

    def __init__(self, loc, heated=True):
        self.location = loc
        self.heated = heated

    def enter(self):
        if self.heated:
            return "entering this wonderful heated accommodation"
        else:
            return "i might freeze to death tonight"

    def demolish(self):
        if self.heated:
            return "please dont demolish this wonderful heated accommodation"
        else:
            return "here's a hammer. good luck"

    def show_location(self):
        return f"Location: {self.location}"
