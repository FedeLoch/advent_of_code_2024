input_path = 'challenges/Day 9: Disk Fragmenter/input0'
from utils import ProgramBlock, get_linked_lists, first_no_free, next_free_block
numbers = open(input_path, 'r').readline().strip()

def checksum(head):
    current, i, res = head, 0, 0
    while(current):
        if current.is_free(): continue
        res += sum(map(lambda x: (x + i) * current.id, range(current.size)))
        i += current.size
        current = current.next
    return res

def compact(head, last):
    free = next_free_block(head)
    to_compact = first_no_free(last)
    while(free != None and free.is_free()):
        if to_compact.next == free: to_compact.next = None; break
        if free.size >= to_compact.size:
            next_program = first_no_free(to_compact.before)
            to_compact.before.next = None
            free.before.next = to_compact
            to_compact.before = free.before
            if free.size > to_compact.size:
                free.size -= to_compact.size
                free.before = to_compact
                to_compact.next = free
            else:
                to_compact.next = free.next
                if free.next: free.next.before = to_compact
                free = next_free_block(free)
            to_compact = next_program
        else:
            new_to_compact = ProgramBlock(to_compact.id, free.size, free.before)
            to_compact.size -= free.size
            new_to_compact.next = free.next
            free.before.next = new_to_compact
            if free.next: free.next.before = new_to_compact
            free = next_free_block(new_to_compact)
    return head

def get_free_space(head, target):
    free = next_free_block(head)
    while(free and free.size < target.size):
        free = next_free_block(free)
    return free

def replace_with(free, target):
    target.before.next = target.next
    if target.next: target.next.before = target.before
    free.before.next = target
    target.before = free.before
    if free.size > target.size:
        free.size -= target.size
        free.before = target
        target.next = free
    else:
        free.next.before = target
        target.next = free.next

def compact2(head, last):
    current, seen = first_no_free(last), []
    while(current != head):
        next = first_no_free(current.before)
        if not current.id in seen:
            free = get_free_space(head, current)
            if free: replace_with(free, current)
            seen.append(current.id)
        current = next
    
    return head

head, last = get_linked_lists(numbers)

head = compact2(head, last)
print('Part 1 :', checksum(compact(head, last)))
print('Part 2 :',checksum(compact2(head, last)))