class Location():
    country = None
    region = None
    city = None

    def __init__(self, country, region, city):
        self.country = country
        self.region = region
        self.city = city

    def printLocation(self):
        print(self.city + ", " + self.region + ", " + self.country)