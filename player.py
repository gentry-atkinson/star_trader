
class Player:
    def __init__(self) -> None:
        self.money = 0
        self.star_date = 2276.0
        self.cur_planet = "Earth"
        self.cur_screen = None
        self.running = True

    def copy(self):
        p = Player()
        p.money = self.money
        p.star_date = self.star_date
        p.cur_planet = self.cur_planet
        p.cur_screen = self.cur_screen
        return p