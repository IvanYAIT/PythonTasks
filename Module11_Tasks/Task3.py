import time

fileSizeInMB = None
MBPerSecond = None

while True:
    try:
        if(fileSizeInMB is None):
            fileSizeInMB = int(input("Укажите размер файла для скачивания: "))
        
        if(fileSizeInMB <= 0):
            fileSizeInMB = None
            print("Размер файла не может быть меньше или равен нулю")
            continue

        if(MBPerSecond is None):
            MBPerSecond = int(input("Какова скорость вашего соединения? "))

        if(MBPerSecond <= 0):
            MBPerSecond = None
            print("Скорость интернета не может быть меньше или равен нулю")
            continue

        break
    except:
        print("Некоторые данные введены неправильно")

currentDownloadSize = 0
secondsPassed = 0

while currentDownloadSize < fileSizeInMB:
    secondsPassed += 1
    currentDownloadSize += MBPerSecond
    
    if(currentDownloadSize >= fileSizeInMB):
        currentDownloadSize = fileSizeInMB
    
    print(f" Прошло {secondsPassed} сек. Скачано {currentDownloadSize} из {fileSizeInMB} Мб ({int((currentDownloadSize / fileSizeInMB)*100)}%)")
    time.sleep(1)