class LRU_Cache():
    CACHE_LIMIT = 3

    data = {}

    @property
    def cache(self):
        return self.data

    @cache.setter
    def cache(self, new_elem):
        self.data[new_elem[0]] = new_elem[1]
        if len(self.data) > self.CACHE_LIMIT:
            key = next(iter(self.data))
            self.data.pop(key)

    def get(self, elem):
        result = self.data.pop(elem)
        self.data[elem] = result
        return result

    def __str__(self):
        string = ''
        for item in self.data.items():
            string += f'{item[0]}: {item[1]}\n'
        return string