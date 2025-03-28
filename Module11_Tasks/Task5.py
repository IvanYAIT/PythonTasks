import math

EARTH_VOLUME = 1.08321 * 10 ** 12

while True:
    try:
        planetRadius = float(input("Введите радиус случайной планеты: "))

        if(planetRadius > 0):
            break
        
        print("Радиус должна быть больше 0")
    except:
        print("Это не число")

planetVolume = (4/3) * math.pi * planetRadius ** 3

if(planetVolume > EARTH_VOLUME):
    print(f"Объём планеты Земля больше в {round(planetVolume / EARTH_VOLUME, 3)} раз")
elif(planetVolume < EARTH_VOLUME):
    print(f"Объём планеты Земля меньше в {round(EARTH_VOLUME / planetVolume, 3)}")
else:
    print("Объем планеты равен объему Земли")