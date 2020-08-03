class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = list()
        self.index_on_deck = 0

    def append(self, item):
        #if the length of items is less than capacity
        if len(self.items) < self.capacity:
            #append item
            self.items.append(item)
        #otherwise we need to pop the first(oldest) and replace with new
        else:
            #pop
            self.items.pop(self.index_on_deck)
            #add new in place
            self.items.insert(self.index_on_deck, item)
            if self.index_on_deck == self.capacity -1:
                self.index_on_deck = 0
            else:
                self.index_on_deck += 1

    def get(self):
        #list comprehension
        return [b for b in self.items]

#does it work - YES!!!!
buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get()) #gives me ['a', 'b', 'c']
buffer.append('d')
print(buffer.get()) #prints ['d', 'b', 'c']
buffer.append('e')
buffer.append('f')
print(buffer.get()) #prints ['d', 'e', 'f']