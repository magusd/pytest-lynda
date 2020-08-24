
class Point():
    def __init__(self, name, latitude, longitude):
        if not type(name) is str:
            # if isinstance(name, str)
            raise ValueError('City name must be a string')
        self.name = name
        if not (-90 <= latitude <= 90) or not(-90 <= longitude <= 90):
            raise ValueError("Invalid latitude and longitude combination")
        self.latitude = latitude
        self.longitude = longitude

    def get_lat_long(self):
        return (self.latitude, self.longitude)
