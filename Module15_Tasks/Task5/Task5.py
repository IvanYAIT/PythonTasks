from services.user_input import call_until_valid_input

class Task5:
    @call_until_valid_input
    def get_container_amount():
        container_amount = int(input("Количество контейнеров: "))

        if(container_amount <= 0):
            raise ValueError
        
        return container_amount
    
    @call_until_valid_input
    def fill_container_storage(container_amount):
        storage = []
        for _ in range(1, container_amount+1):
            container_weight = int(input("Введите вес контейнера: "))

            if(container_weight <= 0 or container_weight >= 200):
                raise ValueError
        
            storage.append(container_weight)

        storage = sorted(storage, reverse=True)
        return storage
    
    @call_until_valid_input
    def add_container(storage):
        result = []
        new_container_weight = int(input("Введите вес нового контейнера: "))

        if(new_container_weight <= 0 or new_container_weight >= 200):
            raise ValueError
        
        isAdded = False
        for index in range(len(storage)):
            if(not isAdded):
                if(storage[index] >= new_container_weight):
                    result.append(storage[index])
                else:
                    result.append(new_container_weight)
                    isAdded = True
                    print(f"Номер, который получит новый контейнер: {index+1}")
            
            if(isAdded):
                result.append(storage[index])
        
        return result

    @classmethod
    def main(cls):
        container_amount = cls.get_container_amount()
        storage = cls.fill_container_storage(container_amount)
        new_storage = cls.add_container(storage)
        