from services.user_input import call_until_valid_input

class Task3:
    @call_until_valid_input
    def get_gpu_amount():
        user_number = int(input("Количество видеокарт: "))

        if(user_number <= 0):
            raise ValueError
        
        return user_number
    
    @call_until_valid_input
    def fill_gpu_storage(gpu_amount):
        storage = []
        for index in range(1, gpu_amount+1):
            gpu_number = int(input(f"{index} Видеокарта: "))

            if(gpu_number <= 0):
                raise ValueError
        
            storage.append(gpu_number)
        return storage
    
    def remove_newest_gpu(storage):
        result = []
        newest_gpu = storage[0]
        for gpu in storage:
            result.append(gpu)
            if(gpu > newest_gpu):
                newest_gpu = gpu
        
        for gpu in storage:
            if(gpu == newest_gpu):
                result.remove(gpu)
        return result

    @classmethod
    def main(cls):
        gpu_amount = cls.get_gpu_amount()
        storage_befor_selling = cls.fill_gpu_storage(gpu_amount)
        storage_after_selling = cls.remove_newest_gpu(storage_befor_selling)
        print(f"Старый список видеокарт: {storage_befor_selling}")
        print(f"Новый список видеокарт: {storage_after_selling}")
