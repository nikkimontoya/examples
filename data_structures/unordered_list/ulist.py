from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def is_in_list(self, value):
        found = False
        current = self.head

        while not found and current is not None:
            found = value == current.get_data()
            current = current.get_next()

        return found

    def remove(self, value):
        removed = False

        if self.head.get_data() == value:
            self.head = self.head.get_next()
            removed = True
        else:
            current = self.head


            while not removed and current is not None:
                if value == current.get_next().get_data():
                    current.set_next(current.get_next().get_next())
                    removed = True

                current = current.get_next()

        return removed