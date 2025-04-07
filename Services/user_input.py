def check_input(func):
    def check():
        while True:
            try:
                number = func()
                break
            except:
                print("Введены неверные данные")
        return number
    return check