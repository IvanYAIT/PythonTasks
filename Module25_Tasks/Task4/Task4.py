class Stack():
    data = []
    @property
    def count(self): return len(self.data)

    def append(self, key, item):
        data_to_add = dict()
        data_to_add[key] = item
        for data_item in self.data:
            if data_item.get(key):
                data_item[key] = item
                return
        
        new_data = []
        for index in range(len(self.data)+1):
            if index == 0:
                new_data.append(data_to_add)
            else:
                new_data.append(self.data[index-1])
        self.data = new_data
    
    def next(self):
        if len(self.data) == 0:
            return
        
        result = self.data[0]
        new_data = []
        for index in range(len(self.data)-1):
            new_data.append(self.data[index+1])
        self.data = new_data
        return result
    
    def sort(self, reverse = False):
        self.data = sorted(self.data, key=lambda item : list(item.items())[0][1], reverse=reverse)
    
class TaskManager:
    tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.append(task, priority)
    
    def print_tasks(self):
        self.tasks.sort()
        data = []
        for _ in range(self.tasks.count):
            task = list(self.tasks.next().items())[0]
            data.append(task)

        priority = data[0][1]
        string = ''
        for task in data:
            if task[1] == priority:
                string += f'{task[0]},'
            else:
                print(f'{priority}) {string}')
                priority = task[1]
                string = f'{task[0]},'
            if id(task) == id(data[len(data)-1]):
                print(f'{priority}) {string}')