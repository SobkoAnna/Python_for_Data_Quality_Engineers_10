import math
import pyodbc

class Geodatabase:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQLite3 ODBC Driver};'
                                   'Direct = True;'
                                   'Database=coordinates.db;'
                                   'String Types = Unicode')
        self.cur = self.conn.cursor()
    def read_database(self, city):
        self.cur.execute(f"SELECT latitude, longitude  FROM coordinates WHERE city='{city}'")
        result = self.cur.fetchone()
        return result

    def write_database(self, city):
        print(f"City {city} not found")
        latitude = input('Please provide latitude: ')
        longitude = input('Please provide longitude: ')
        self.cur.execute(f"INSERT INTO coordinates VALUES('{city}', '{latitude}', '{longitude}')")
        self.cur.commit()
        print('information added')
        return latitude, longitude

    def distance(self, lon1, lat1, lon2, lat2):
        R = 6371.0
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        print(distance)
        return distance
    def executor(self):
        city_1 = input("Please provide city_1: ")
        if not self.read_database(city_1):
            self.write_database(city_1)
        coordinate_city_1 = self.read_database(city_1)
        lat1 = coordinate_city_1[0]
        lon1 = coordinate_city_1[1]

        city_2 = input("Please provide city_2: ")
        if not self.read_database(city_2):
            self.write_database(city_2)
        coordinate_city_2 = self.read_database(city_2)
        lat2 = coordinate_city_2[0]
        lon2 = coordinate_city_2[1]
        self.distance(float(lon1), float(lat1), float(lon2), float(lat2))

geo=Geodatabase()
Geodatabase.executor(geo)