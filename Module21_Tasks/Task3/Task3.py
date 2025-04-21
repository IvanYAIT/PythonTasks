from services.user_input import call_until_valid_input

class Task3:
    @call_until_valid_input
    def get_copy_amount(self):
        amount = int(input("Сколько сайтов: "))

        if(amount <= 0):
            raise ValueError("Количесто сайтов не может быть меньше 0")
        
        return amount
    
    @call_until_valid_input
    def get_poduct_name(self):
        return input("Введите название продукта для нового сайта: ")
    
    def deepcopy(self, data, product_name):
        if not isinstance(data, dict):
            return data.replace("телефон", product_name)

        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                result[self.deepcopy(key, product_name)] = self.deepcopy(value, product_name)
            return result
        return data

    def copy_site(self, site, amount):
        result = []
        for _ in range(amount):
            product_name = self.get_poduct_name()
            new_site = self.deepcopy(site, product_name)
            result.append(new_site)
            print(new_site)
        return result
    
    def main(self):
        site = {
        	'html': {
        		'head': {
        			'title': 'Куплю/продам телефон недорого'
        		},
        		'body': {
        			'h2': 'У нас самая низкая цена на телефон',
        			'div': 'Купить',
        			'p': 'продать'
        		}
        	}
        }
        amount_of_sites = self.get_copy_amount()
        copied_sites = self.copy_site(site, amount_of_sites)
