class Task3:
    def connect_data(data):
        result = []
        for data_key in data.keys():
            result.append(data_key + data[data_key])
        return result

    @classmethod
    def main(cls):
        players = {
            ("Ivan", "Volkin"): (10, 5, 13),
            ("Bob", "Robbin"): (7, 5, 14),
            ("Rob", "Bobbin"): (12, 8, 2)
        }
        new_data = cls.connect_data(players)
        print(new_data)