import requests
import json
import unicodedata
import sqlite3
from config import URL_BASE


class StationData:
    def __init__(self, data):
        self.station_id = data["id_stacji"]
        self.station_name = data["stacja"]
        self.weather = data["pogoda"]
        self.date = data["data_pomiaru"]
        self.time = data["godzina_pomiaru"]
        self.temperature = data["temperatura"]
        self.wind_speed = data["predkosc_wiatru"]
        self.wind_direction = data["kierunek_wiatru"]
        self.relative_humidity = data["wilgotnosc_wzgledna"]
        self.precipitation = data["suma_opadu"]
        self.pressure = data["cisnienie"]

    def get_station_id(self):
        return self.station_id

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_temperature(self):
        return self.temperature

    def get_station_name(self):
        return self.station_name

    def get_weather(self):
        return self.weather

    def get_wind_speed(self):
        return self.wind_speed

    def get_wind_direction(self):
        return self.wind_direction

    def get_relative_humidity(self):
        return self.relative_humidity

    def get_precipitation(self):
        return self.precipitation

    def get_pressure(self):
        return self.pressure

    def __repr__(self):
        return f" StationData(station_id={self.station_id!r},\n station_name={self.station_name!r},\n date={self.date!r},\n time={self.time!r},\n temperature={self.temperature!r},\n wind_speed={self.wind_speed!r},\n wind_direction={self.wind_direction!r},\n relative_humidity={self.relative_humidity!r},\n precipitation={self.precipitation!r},\n pressure={self.pressure!r}"


def normalize(txt):
    txt = txt.lower()
    txt = unicodedata.normalize("NFKD", txt)
    txt = "".join(c for c in txt if not unicodedata.combining(c))
    return txt


def get_station_data(station_name):
    station = normalize(station_name)
    station = station.lower()
    url = f"{URL_BASE}/{station}"

    response = requests.get(url)
    data = response.json()

    return StationData(data)