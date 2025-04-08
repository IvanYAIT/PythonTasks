def call_until_valid_input(func):
    def check(*args, **kwargs):
        while True:
            try:
                number = func(*args, **kwargs)
                break
            except:
                print("Введены неверные данные")
        return number
    return check