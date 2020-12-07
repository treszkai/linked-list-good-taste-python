from unittest import TestCase

from .linked_list import IntList, IntListItem

N = 5
ITEMS = [IntListItem(i, None) for i in range(N)]


class TestLinkedListInsert(TestCase):
    def setUp(self):
        self.linked_list = IntList(None)
        self.assertEqual(0, len(self.linked_list))
        self.assertEqual([], list(self.linked_list))

    def test_insert_beginning(self):
        for item in ITEMS:
            self.linked_list.insert_before(self.linked_list.head, item)
        self.assertEqual(N, len(self.linked_list))
        self.assertEqual(list(range(N - 1, -1, -1)), list(self.linked_list))

    def test_insert_end(self):
        for item in ITEMS:
            self.linked_list.insert_before(None, item)
        self.assertEqual(N, len(self.linked_list))
        self.assertEqual(list(range(0, N)), list(self.linked_list))


class TestLinkedListRemove(TestCase):
    def setUp(self):
        self.linked_list = IntList(None)
        for item in ITEMS:
            self.linked_list.insert_before(None, item)

    def test_remove_cs101_middle(self):
        self.linked_list.remove_cs101(self.linked_list.head.next_item)
        self.assertEqual([0, 2, 3, 4], list(self.linked_list))

    def test_remove_cs101_end(self):
        self.linked_list.remove_cs101(
            self.linked_list.head.next_item.next_item.next_item.next_item
        )
        self.assertEqual([0, 1, 2, 3], list(self.linked_list))

    def test_remove_cs101_head(self):
        for i in range(N):
            self.linked_list.remove_cs101(self.linked_list.head)
            self.assertEqual(list(range(i + 1, N)), list(self.linked_list))

        self.assertEqual(0, len(self.linked_list))

    def test_remove_elegant_middle(self):
        self.linked_list.remove_elegant(self.linked_list.head.next_item)
        self.assertEqual([0, 2, 3, 4], list(self.linked_list))

    def test_remove_elegant_end(self):
        self.linked_list.remove_elegant(
            self.linked_list.head.next_item.next_item.next_item.next_item
        )
        self.assertEqual([0, 1, 2, 3], list(self.linked_list))

    def test_remove_elegant_head(self):
        for i in range(N):
            self.linked_list.remove_elegant(self.linked_list.head)
            self.assertEqual(list(range(i + 1, N)), list(self.linked_list))

        self.assertEqual(0, len(self.linked_list))
