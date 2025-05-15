class Task1:
    @classmethod
    def main(cls):
        floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
        names: list[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
        numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

        floats_new = [round(num**3, 3) for num in floats]
        names_new = [name for name in names if len(name) > 5]
        result = 1
        for num in numbers:
            result *= num
        print(floats_new)
        print(names_new)
        print(result)