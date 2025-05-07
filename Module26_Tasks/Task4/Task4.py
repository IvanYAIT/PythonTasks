class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    head = Node(None)
    last_element = head

    def __init__(self, *args):
        self.lenght = len(args)
        self.head = Node(args[0]) if self.lenght > 0 else None
        self.last_element = self.head 
        for i in range(1, self.lenght): 
            self.last_element.next = Node(args[i]) 
            self.last_element = self.last_element.next 

    def __iter__(self):
        current = self.head
        for _ in range(self.lenght-1):
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        return self.lenght

    def append(self, value):
        self.lenght +=1
        if not self.head:
            self.head.value = value
            return
        
        new = Node(value)
        self.last_element.next = new
        self.last_element = self.last_element.next

    def get(self, index : int) -> Node:
        if 0 > index > self.lenght:
            print('No such index')
            return

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, index : int):
        if 0 > index > self.lenght:
            print('No such index')
            return
        
        if index == 0:
            self.head = self.head.next

        previous = self.head
        for _ in range(index-1):
            previous = previous.next
        previous.next = previous.next.next