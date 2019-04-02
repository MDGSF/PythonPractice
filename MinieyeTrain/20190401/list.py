#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Huang Jian
Date: 2019-04-02

Module list implements a double linked list.
"""


class Element:
    """
    Element is an element of linked list.
    """

    def __init__(self, val=None):
        """
        :param next: Points to next element.
        :param prev: Points to previous element.
        :param value: The value stored with this element.
        :param list: The list to which this element belongs.
        """
        self.next = None
        self.prev = None
        self.value = val
        self.list = None

    def Next(self):
        """Next returns the next list element or None."""
        return self.next if self.list is not None and self.next != \
                            self.list.root else None

    def Prev(self):
        """Prev returns the previous list element or None."""
        return self.prev if self.list is not None and self.prev != \
                            self.list.root else None


class List:
    """
    List represents a doubly linked list.
    """

    def __init__(self):
        """
        @param root: sentinel list element
        @param len: current list length excluding (this) sentinel element
        """
        self.root = Element()
        self.root.next = self.root
        self.root.prev = self.root
        self.len = 0

    def Len(self):
        """Len returns the number of elements of list self."""
        return self.len

    def __len__(self):
        return self.len

    def Front(self):
        """Front returns the first element of list or None if list is empty."""
        return None if self.len == 0 else self.root.next

    def Back(self):
        """Back returns the last element of list or None if list is empty."""
        return None if self.len == 0 else self.root.prev

    def PushFront(self, v):
        """
        PushFront inserts a new element e with value v at the front of
        list self and returns e.
        """
        return self.insertValue(v, self.root)

    def PushBack(self, v):
        """
        PushBack inserts a new element e with value v at the back of
        list self and returns e.
        """
        return self.insertValue(v, self.root.prev)

    def InsertBefore(self, v, mark):
        """
        InsertBefore inserts a new element e with value v before mark
        and returns e.
        If mark is not an element of list self, return None.
        The mark must not be None.
        """
        if mark.list != self:
            return None
        return self.insertValue(v, mark.prev)

    def InsertAfter(self, v, mark):
        """
        InsertBefore inserts a new element e with value v after mark
        and returns e.
        If mark is not an element of list self, return None.
        The mark must not be None.
        """
        if mark.list != self:
            return None
        return self.insertValue(v, mark)

    def Remove(self, e):
        """
        Remove removes e from list if e is an element of list self.
        It returns the element value e.value.
        The element e must not be None.
        """
        if e.list == self:
            self.remove(e)
        return e.value

    def MoveToFront(self, e):
        """
        MoveToFront moves element e to the front of list self.
        If e is not an element of self, the list is not modified.
        The element must not be None.
        """
        if e.list != self or self.root.next == e:
            return
        self.move(e, self.root)

    def MoveToBack(self, e):
        """
        MoveToBack moves element e to the back of list self.
        If e is not an element of self, the list is not modified.
        The element must not be None.
        """
        if e.list != self or self.root.prev == e:
            return
        self.move(e, self.root.prev)

    def MoveBefore(self, e, mark):
        """
        MoveBefore moves element e to its new position before mark.
        If e or mark is not an element of self, or e == mark, the list
        is not modified.
        The element and mark must not be None.
        """
        if e.list != self or e == mark or mark.list != self:
            return
        self.move(e, mark.prev)

    def MoveAfter(self, e, mark):
        """
        MoveAfter moves element e to its new position after mark.
        If e or mark is not an element of self, or e == mark, the list
        is not modified.
        The element and mark must not be None.
        """
        if e.list != self or e == mark or mark.list != self:
            return
        self.move(e, mark)

    def PushBackList(self, other):
        """
        PushBackList inserts a copy of an other list at the back of
        list self.
        The list self and other may be the same.
        They must not be None.
        """
        i = other.Len()
        e = other.Front()
        while i > 0:
            self.insertValue(e.value, self.root.prev)
            i -= 1
            e = e.Next()

    def PushFrontList(self, other):
        """
        PushFrontList inserts a copy of an other list at the front of
        list self.
        The list self and other may be the same.
        They must not be None.
        """
        i = other.Len()
        e = other.Front()
        while i > 0:
            self.insertValue(e.value, self.root.prev)
            i -= 1
            e = e.Next()

    def insert(self, e, at):
        """insert e after at, increments self.len, return e"""
        n = at.next
        at.next = e
        e.prev = at
        e.next = n
        n.prev = e
        e.list = self
        self.len += 1
        return e

    def insertValue(self, v, at):
        """insertValue is a convenience wrapper for insert(Element(v), at)"""
        return self.insert(Element(v), at)

    def remove(self, e):
        """remove removes e from its list, decrements self.len, return e"""
        e.prev.next = e.next
        e.next.prev = e.prev
        e.next = None
        e.prev = None
        e.list = None
        self.len -= 1
        return e

    def move(self, e, at):
        """move moves e to next to at and returns e"""
        if e == at:
            return e
        e.prev.next = e.next
        e.next.prev = e.prev

        n = at.next
        at.next = e
        e.prev = at
        e.next = n
        n.prev = e

        return e


def showlist(l):
    print('l.Len() =', l.Len(), end=', ')
    print('len(l) =', len(l), end=', ')
    # print('max(l) =', max(l), end=', ')
    print('list =', end='')
    e = l.Front()
    while e is not None:
        print(e.value, end=' ')
        e = e.Next()
    print()


def test1():
    l = List()
    l.PushBack(4)
    l.PushBack(10)
    l.PushFront(1)
    l.PushFront(999)
    showlist(l)

    f = l.Front()
    l.Remove(f)
    showlist(l)


def main():
    test1()


if __name__ == "__main__":
    main()
