from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")


class Navigator(Generic[T]):

    def __init__(self, list: List[T]):
        self.index = 0
        self.list = list

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            the_next = self.list[self.index]
            self.index += 1
            return the_next
        raise StopIteration()

    def __len__(self) -> int:
        return len(self.list)

    def has_next(self):
        return self.index < self.__len__()

    def prev(self):
        self.index = self.index - 1

    def reset(self):
        self.index = 0

    def get_index(self) -> int:
        return self.index

    def get_curr(self) -> T:
        return self.list[self.index - 1]

    def get_prev(self) -> Optional[T]:
        if self.index >= 2:
            return self.list[self.index - 2]
        return None

    def get_remaining(self) -> int:
        return self.__len__() - self.index

    def get_absolute_index(self) -> int:
        index = 0
        for i in range(self.index):
            index = index + 1
        return index
