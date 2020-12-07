from dataclasses import dataclass
from typing import Optional


@dataclass
class IntListItem:
    value: int
    next_item: Optional["IntListItem"]


@dataclass
class IntList:
    head: Optional[IntListItem]

    def remove_cs101(self, target: IntListItem) -> None:
        cur = self.head
        prev = None

        while cur is not target:
            prev, cur = cur, cur.next_item

        if prev is not None:
            prev.next_item = cur.next_item
        else:
            self.head = cur.next_item

    def insert_before(self, before: Optional[IntListItem], new_item: IntListItem) -> None:
        """Insert an item into the list.

        Inserts an item `item` into the list `l`, before the item identified
        by `before`. Runtime is O(n) where n refers to the distance of before from
        the list head.

        Undefined behavior if `before` is not in the list.

        :param l: A list of integers
        :param before: The item before which the new item should be inserted.
               If `before` is the list head, the new item will be
               inserted at the beginning; if `before` is None,
               the item will be appended to the end of the list.
        :param new_item: The item to insert
        """
        item_attr = self, 'head'

        while (item := getattr(*item_attr)) is not None and item is not before:
            item_attr = item, 'next_item'
        setattr(*item_attr, new_item)

        getattr(*item_attr).next_item = before


    def __len__(self):
        k = 0
        cur = self.head

        while cur is not None:
            cur = cur.next_item
            k += 1

        return k

    def __iter__(self):
        item = self.head
        while item:
            yield item.value
            item = item.next_item
