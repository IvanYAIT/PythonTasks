import math

EARTH_VOLUME = 1.08321 * 10 ** 12

while True:
    try:
        planet_radius = float(input("Введите радиус случайной планеты: "))

        if(planet_radius > 0):
            break
        
        print("Радиус должна быть больше 0")
    except:
        print("Это не число")

planet_volume = (4/3) * math.pi * planet_radius ** 3

if(planet_volume > EARTH_VOLUME):
    print(f"Объём планеты Земля больше в {round(planet_volume / EARTH_VOLUME, 3)} раз")
elif(planet_volume < EARTH_VOLUME):
    print(f"Объём планеты Земля меньше в {round(EARTH_VOLUME / planet_volume, 3)}")
else:
    print("Объем планеты равен объему Земли")