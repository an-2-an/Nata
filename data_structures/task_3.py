# Extend the Stack to include a method
# called get_from_stack that searches
# and returns an element e from a stack.
# Any other element must remain on the stack
# respecting their order. Consider the case in
# which the element is not found -
# raise ValueError with proper info Message

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

    def get_from_stack(self, e):
        for item in reversed(self._items):
            if item == e:
                return self._items.pop(self._items.index(e))
        raise ValueError('No Such Element!!!')


if __name__ == "__main__":
    s = MyStack()
    s.add_items()
    print(s)
    e = input('element value: ')
    try:
        value = s.get_from_stack(e)
        print(f'found element: {value}')
    except Exception as ex:
        print(ex)
    print(s)