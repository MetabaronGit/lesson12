import json
import csv

# cviceni: cteme sloupce
def get_columns(filename):
    columns = {}
    with open(filename) as f:
        reader = csv.reader(f)

        for r in reader:
            for i, item in enumerate(r):
                columns[i] = columns.get(i, []) + [item]

    return list(columns.values())

# print(get_columns("test.csv"))



# načtení json počasí
import json

# Načtáme JSON soubor

with open('weather1.json') as f:

    data = json.load(f)

# Získáváme požadované informace ze slovníku uloženém v proměné data.

# Pro snažší práci si vyrobíme nový slovník.

weather = data[0].get('weather')

location = data[0].get('address_components').get('short_name')

min_temp = weather.get('temperature').get('min')

max_temp = weather.get('temperature').get('max')

curr_temp = weather.get('temperature').get('current')

wind_direction = weather.get('wind').get('direction')

wind_speed = weather.get('wind').get('speed')

# Nastavujeme řádek s intenzitou deště - pokud neprší = prázný, pokud prší = lomítka.

rain_intensity = ''

if weather.get('rain').get('raining'):

    rain_intensity = weather.get('rain').get('intensity-value')

print(location)

print('{:3}°C | {:3}°C | {:3}°C'.format(min_temp, curr_temp, max_temp))

# Pokud prší rain_intensity není prázdný string - vrací True.

if rain_intensity:

    print(int(rain_intensity)* '/')

print('Směr větru: {}'.format(wind_direction))

print('Rychlost větru: {} m/s'.format(wind_speed))

