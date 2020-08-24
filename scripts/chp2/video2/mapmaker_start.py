class Point():
    def __init__(self, city, lat, lon):
        self._city = city
        self._lat = lat
        self._lon = lon

    def get_lat_long(self):
        return (self._lat, self._lon)
