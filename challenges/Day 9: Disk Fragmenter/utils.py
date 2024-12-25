class Block:
    size, next, before = 0, None, None
    def __init__(self, size, before): self.before = before; self.size = size
    def set_next(self, next): self.next = next
    def is_free(self): None
    def to_string(self): ''
    def delete(self): self.before.next = self.next; self.next.before = self.before

class FreeBlock(Block):
    def __init__(self, size, before): super().__init__(size, before)
    def is_free(self): return True
    def to_string(self): return 'FreeBlock with size: ', self.size

class ProgramBlock(Block):
    id = None
    def __init__(self, id, size, before):  super().__init__(size, before); self.id = id
    def is_free(self): return False
    def to_string(self): return 'ProgramBlock with id: ', self.id, ' and size: ', self.size

def get_linked_lists(numbers):
    is_block = False; current_block = 0
    head = ProgramBlock(current_block, int(numbers[0]), None)
    current = head
    for n in numbers[1:]:
        next = None
        size = int(n)
        if is_block: current_block += 1; next = ProgramBlock(current_block, size, current)
        else: next = FreeBlock(size, current)
        current.set_next(next)
        current = next
        is_block = not is_block

    return head, current

def next_free_block(free):
    current = free.next
    while(current and (not current.is_free())): current = current.next
    return current

def first_no_free(last):
    current = last
    while(current.is_free()): current = current.before
    return current

def memory(head):
    current = head; _str = ''
    while(current):
        _str += ('.' if current.is_free() else str(current.id)) * current.size
        current = current.next
    return _str