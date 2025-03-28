PERCENTAGE_AMPLITUDE_ATTENUATION = 8.4 / 100

amplitude = None
stopAmplitude = None

while True:
    try:
        if(amplitude is None):
            amplitude = float(input("Введите начальную амплитуду: "))

        if(amplitude <= 0):
            amplitude = None
            print("Амплитуда должна быть больше 0")
            continue

        if(stopAmplitude is None):
            stopAmplitude = float(input("Введите амплитуду остановки: "))

        if(stopAmplitude <= 0):
            stopAmplitude = None
            print("Амплитуда должна быть больше 0")
            continue

        break
    except:
        print("Это не число")

cycles = 0
while amplitude > stopAmplitude:
    cycles += 1
    amplitude -= amplitude * PERCENTAGE_AMPLITUDE_ATTENUATION

print(f"Маятник считается остановившимся через {cycles} колебаний")