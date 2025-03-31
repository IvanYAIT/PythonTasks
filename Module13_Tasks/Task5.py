PERCENTAGE_AMPLITUDE_ATTENUATION = 8.4 / 100

amplitude = None
stop_amplitude = None

while True:
    try:
        if(amplitude is None):
            amplitude = float(input("Введите начальную амплитуду: "))

        if(amplitude <= 0):
            amplitude = None
            print("Амплитуда должна быть больше 0")
            continue

        if(stop_amplitude is None):
            stop_amplitude = float(input("Введите амплитуду остановки: "))

        if(stop_amplitude <= 0):
            stop_amplitude = None
            print("Амплитуда должна быть больше 0")
            continue

        break
    except:
        print("Это не число")

cycles = 0
while amplitude > stop_amplitude:
    cycles += 1
    amplitude -= amplitude * PERCENTAGE_AMPLITUDE_ATTENUATION

print(f"Маятник считается остановившимся через {cycles} колебаний")