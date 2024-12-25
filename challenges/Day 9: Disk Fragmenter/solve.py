input_path = 'challenges/Day 9: Disk Fragmenter/input0'
from utils import ProgramBlock, get_linked_lists, first_no_free, next_free_block
numbers = open(input_path, 'r').readline().strip()

def checksum(head):
    current, i, res = head, 0, 0
    while(current):
        for j in range(current.size):
            res += ((i + j) * current.id)
        i += current.size
        current = current.next
    return res

def compact(head, last):
    free = head.next
    to_compact = first_no_free(last)
    while(free != None and free.is_free()):
        if to_compact.next == free: to_compact.next = None; break
        if free.size >= to_compact.size:
            to_compact.before.next = None
            next_program = first_no_free(to_compact.before)
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
            free.next.before = new_to_compact
            free = next_free_block(free)
    return head, to_compact

head, last = get_linked_lists(numbers)
head, last = compact(head, last)

print('Part 1 :', checksum(head))
