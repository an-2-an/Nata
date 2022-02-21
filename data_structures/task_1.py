# Write a program that reads in a sequence of characters
# and prints them in reverse order, using your implementation of Stack.

class MyStack:
    def __init__(self):
        self._items = []

    def add_items(self):
        print('input character or \nempty string to finish: ')
        while True:
            ch = input()
            if not ch:
                break
            self.push(ch)

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<My Stack>:\n"
        for item in reversed(self._items):
            representation += f"'{item}'\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = MyStack()
    s.add_items()
    print(s)

