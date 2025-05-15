def singleton(cls):
    def wrapper():
        if not wrapper.instance:
            wrapper.instance = cls()
        return wrapper.instance
    wrapper.instance = None
    return wrapper

@singleton
class Task5:
    def __init__(self):
        pass