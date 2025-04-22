from services.user_input import call_until_valid_input

class Task2:
    @call_until_valid_input
    def get_user_key(self):
        return input("Введите искомый ключ: ").lower()
    
    @call_until_valid_input
    def get_command(self):
        command = input("Хотите ввести максимальную глубину? Y/N: ").lower()

        if(command != "y" and command != "n"):
            raise ValueError("Такой комманды нет")
        
        return command
    
    @call_until_valid_input
    def get_depth(self):
        depth = int(input("Введите максимальную глубину: "))

        if(depth <= 0):
            raise ValueError("Глубина должны быть больше 0")
        
        return depth
        
    def get_value_by_key(self, data, key, depth):
        if(depth > 0):
            depth -= 1
        try:
            for data_key in data.keys():
                    if(data_key.lower() == key):
                        return data[data_key]
                    else:
                        if(depth == 0):
                            return None
                        value = self.get_value_by_key(data[data_key], key, depth)
                        if(value is not None):
                            return value
        except:
            return
        return None

    def main(self):
        site = {
        	'html': {
        		'head': {
        			'title': 'Мой сайт'
        		},
        		'body': {
        			'h2': 'Здесь будет мой заголовок',
        			'div': 'Тут, наверное, какой-то блок',
        			'p': 'А вот здесь новый абзац',
                    'data' : {'data' : 'data'}
        		}
        	}
        }
        key = self.get_user_key()
        command = self.get_command()
        depth = -1
        if(command == "y"):
            depth = self.get_depth()
        value = self.get_value_by_key(site, key, depth)
        print(f"Значение ключа: {value}")