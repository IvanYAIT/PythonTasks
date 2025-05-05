def call_until_valid_input(func):
    def check(*args, **kwargs):
        while True:
            try:
                number = func(*args, **kwargs)
                break
            except Exception as e:
                if(len(e.args) >=1):
                    print(e.args[0])
                else:
                    print("Введены неверные данные")
        return number
    return check