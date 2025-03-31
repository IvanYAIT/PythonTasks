import time

file_size_in_mb = None
mb_per_second = None

while True:
    try:
        if(file_size_in_mb is None):
            file_size_in_mb = int(input("Укажите размер файла для скачивания: "))
        
        if(file_size_in_mb <= 0):
            file_size_in_mb = None
            print("Размер файла не может быть меньше или равен нулю")
            continue

        if(mb_per_second is None):
            mb_per_second = int(input("Какова скорость вашего соединения? "))

        if(mb_per_second <= 0):
            mb_per_second = None
            print("Скорость интернета не может быть меньше или равен нулю")
            continue

        break
    except:
        print("Некоторые данные введены неправильно")

current_download_size = 0
seconds_passed = 0

while current_download_size < file_size_in_mb:
    seconds_passed += 1
    current_download_size += mb_per_second
    
    if(current_download_size >= file_size_in_mb):
        current_download_size = file_size_in_mb
    
    print(f" Прошло {seconds_passed} сек. Скачано {current_download_size} из {file_size_in_mb} Мб ({int((current_download_size / file_size_in_mb)*100)}%)")
    time.sleep(1)