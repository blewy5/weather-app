from core import StationData


def run():
    station = input("Podaj nazwe miasta: ")
    station_data = get_station_data(station)
    print(station_data)