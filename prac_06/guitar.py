class Guitar:

    def __init__(self, name, year, cost):
        self.name = ""
        self.year = 0
        self.cost = 0

    def __str__(self):
        return "{}, ({}), : , {}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
