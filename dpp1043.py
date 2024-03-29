# This problem was asked by Google.

# Given an iterator with methods next() and hasNext(), 
# create a wrapper iterator, PeekableInterface, which also implements peek(). 
# peek shows the next element that would be returned on next()

# in order to create a object/class as an iterator you have to implement the methods __iter__() and __next__() to the object.
from typing import Iterable, Any

class PeekableInterface(object):
    def __init__(self, iterator: Iterable[Any]) -> None:
        self.iterator = iterator
        try:
            self.next_val = next(self.iterator)
            self.has_next = True
        except StopIteration:
            self.next_val = None
            self.has_next = False


    def peek(self) -> Any:
        return self.next_val

    def next(self) -> Any:
        if self.has_next:
            curr_elem = self.next_val
            try:
                self.next_val = next(self.iterator)
            except StopIteration:
                self.next_val = None
                self.has_next = False
            return curr_elem
        return None


    def hasNext(self) -> bool:
        return self.has_next


if __name__ == "__main__":
    sample_list = [1,2,3,4,5]
    iterator = iter(sample_list)
    peekable = PeekableInterface(iterator)

    print(peekable.peek())
    print(peekable.hasNext())

    print(peekable.next())
    print(peekable.next())
    print(peekable.next())

    print(peekable.peek())
    print(peekable.hasNext())

    print(peekable.next())
    print(peekable.hasNext())
    print(peekable.peek())
    print(peekable.next())

    print(peekable.hasNext())
    print(peekable.peek())

    print()

    sample_list = []
    iterator = iter(sample_list)
    peekable = PeekableInterface(iterator)

    print(peekable.peek())
    print(peekable.hasNext())


