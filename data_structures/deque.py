class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_to_front(self, item):
        self.items.append(item)

    def add_to_rear(self, item):
        self.items.insert(0, item)

    def remove_from_front(self):
        return self.items.pop()

    def remove_from_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)