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


class ListIter:
    """
    ListIter is iterater for List.
    """

    def __init__(self, l):
        self.list = l
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.list is None \
                or self.current is None \
                or self.current == self.list.root:
            raise StopIteration
        else:
            v = self.current.value
            self.current = self.current.Next()
            return v


class List:
    """
    List represents a doubly linked list.
    """

    def __init__(self):
        """
        @param root: sentinel list element
        @param len: current list length excluding (this) sentinel element
        @param iter: points to list iterator.
        """
        self.root = Element()
        self.root.next = self.root
        self.root.prev = self.root
        self.len = 0
        self.iter = ListIter(self)

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
        e = other.Back()
        while i > 0:
            self.insertValue(e.value, self.root)
            i -= 1
            e = e.Prev()

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

    def __iter__(self):
        self.iter.current = self.Front()
        return self.iter


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


def checkListLen(l, len):
    if l.Len() != len:
        print('Error l.Len() = {}, len = {}'.format(l.Len(), len))
        return False
    return True


def checkListPointers(l, es):
    root = l.root

    if not checkListLen(l, len(es)):
        return

    if len(es) == 0:
        if l.root.next != root or l.root.prev != root:
            print('Error, root, root.next, root.prev =',
                  root, l.root.next, l.root.prev)
        return

    for i, e in enumerate(es):
        prev = root
        Prev = None
        if i > 0:
            prev = es[i - 1]
            Prev = prev
        if e.prev != prev:
            print(f'elt[{i}]({e}).prev = {e.prev}, want {prev}')
        if e.Prev() != Prev:
            print(f'elt[{i}]({e}).Prev() = {e.Prev()}, want {Prev}')

        next = root
        Next = None
        if i < len(es) - 1:
            next = es[i + 1]
            Next = next
        if e.next != next:
            print(f'elt[{i}]({e}).next = {e.next}, want {next}')
        if e.Next() != Next:
            print(f'elt[{i}]({e}).Next() = {e.Next}, want {Next}')


def test1():
    print('\ntest1')

    l = List()
    l.PushBack(4)
    l.PushBack(10)
    l.PushFront(1)
    l.PushFront(999)
    showlist(l)

    f = l.Front()
    l.Remove(f)
    showlist(l)


def testList():
    print('\ntestList')

    l = List()
    checkListPointers(l, [])

    e = l.PushFront("a")
    checkListPointers(l, [e])
    l.MoveToFront(e)
    checkListPointers(l, [e])
    l.MoveToBack(e)
    checkListPointers(l, [e])
    l.Remove(e)
    checkListPointers(l, [])

    e2 = l.PushFront(2)
    e1 = l.PushFront(1)
    e3 = l.PushBack(3)
    e4 = l.PushBack("banana")
    checkListPointers(l, [e1, e2, e3, e4])

    l.Remove(e2)
    checkListPointers(l, [e1, e3, e4])

    l.MoveToFront(e3)
    checkListPointers(l, [e3, e1, e4])

    l.MoveToFront(e1)
    l.MoveToBack(e3)
    checkListPointers(l, [e1, e4, e3])

    l.MoveToFront(e3)
    checkListPointers(l, [e3, e1, e4])
    l.MoveToFront(e3)
    checkListPointers(l, [e3, e1, e4])

    l.MoveToBack(e3)
    checkListPointers(l, [e1, e4, e3])
    l.MoveToBack(e3)
    checkListPointers(l, [e1, e4, e3])

    e2 = l.InsertBefore(2, e1)
    checkListPointers(l, [e2, e1, e4, e3])
    l.Remove(e2)
    e2 = l.InsertBefore(2, e4)
    checkListPointers(l, [e1, e2, e4, e3])
    l.Remove(e2)
    e2 = l.InsertBefore(2, e3)
    checkListPointers(l, [e1, e4, e2, e3])
    l.Remove(e2)

    e2 = l.InsertAfter(2, e1)
    checkListPointers(l, [e1, e2, e4, e3])
    l.Remove(e2)
    e2 = l.InsertAfter(2, e4)
    checkListPointers(l, [e1, e4, e2, e3])
    l.Remove(e2)
    e2 = l.InsertAfter(2, e3)
    checkListPointers(l, [e1, e4, e3, e2])
    l.Remove(e2)

    sum = 0
    e = l.Front()
    while e is not None:
        if type(e.value) == int:
            sum += e.value
        e = e.Next()
    if sum != 4:
        print('Error, sum =', sum)

    next = None
    e = l.Front()
    while e is not None:
        next = e.Next()
        l.Remove(e)
        e = next
    checkListPointers(l, [])


def checkList(l, es):
    if not checkListLen(l, len(es)):
        return

    i = 0
    e = l.Front()
    while e is not None:
        if e.value != es[i]:
            print(f'elt[{i}].value = {e.value}, want {es[i]}')
        e = e.Next()
        i += 1


def testExtending():
    print('testExtending')

    l1 = List()
    l2 = List()

    l1.PushBack(1)
    l1.PushBack(2)
    l1.PushBack(3)

    l2.PushBack(4)
    l2.PushBack(5)

    l3 = List()
    l3.PushBackList(l1)
    checkList(l3, [1, 2, 3])

    l3 = List()
    l3.PushFrontList(l2)
    checkList(l3, [4, 5])
    l3.PushFrontList(l1)
    checkList(l3, [1, 2, 3, 4, 5])

    checkList(l1, [1, 2, 3])
    checkList(l2, [4, 5])

    l3 = List()
    l3.PushBackList(l1)
    checkList(l3, [1, 2, 3])
    l3.PushBackList(l3)
    checkList(l3, [1, 2, 3, 1, 2, 3])

    l3 = List()
    l3.PushFrontList(l1)
    checkList(l3, [1, 2, 3])
    l3.PushFrontList(l3)
    checkList(l3, [1, 2, 3, 1, 2, 3])

    l3 = List()
    l1.PushBackList(l3)
    checkList(l1, [1, 2, 3])
    l1.PushFrontList(l3)
    checkList(l1, [1, 2, 3])


def testRemove():
    print('testRemove')

    l = List()
    e1 = l.PushBack(1)
    e2 = l.PushBack(2)
    checkListPointers(l, [e1, e2])
    e = l.Front()
    l.Remove(e)
    checkListPointers(l, [e2])
    l.Remove(e)
    checkListPointers(l, [e2])


def test2():
    print('test2')

    l1 = List()
    l1.PushBack(1)
    l1.PushBack(2)

    l2 = List()
    l2.PushBack(3)
    l2.PushBack(4)

    e = l1.Front()
    l2.Remove(e)
    if l2.Len() != 2:
        print('Error, l2.Len() =', l2.Len())

    l1.InsertBefore(8, e)
    if len(l1) != 3:
        print('Error, l1.Len() =', l1.Len())


def test3():
    print('test3')

    l = List()
    l.PushBack(1)
    l.PushBack(2)

    e = l.Front()
    l.Remove(e)
    if e.value != 1:
        print('Error, e.value =', e.value)
    if e.next is not None:
        print('Error, e.next =', e.next)
    if e.prev is not None:
        print('Error, e.prev = ', e.prev)


def testMove():
    print('testMove')

    l = List()
    e1 = l.PushBack(1)
    e2 = l.PushBack(2)
    e3 = l.PushBack(3)
    e4 = l.PushBack(4)

    l.MoveAfter(e3, e3)
    checkListPointers(l, [e1, e2, e3, e4])
    l.MoveBefore(e2, e2)
    checkListPointers(l, [e1, e2, e3, e4])

    l.MoveAfter(e3, e2)
    checkListPointers(l, [e1, e2, e3, e4])
    l.MoveBefore(e2, e3)
    checkListPointers(l, [e1, e2, e3, e4])

    l.MoveBefore(e2, e4)
    checkListPointers(l, [e1, e3, e2, e4])
    e2, e3 = e3, e2

    l.MoveBefore(e4, e1)
    checkListPointers(l, [e4, e1, e2, e3])
    e1, e2, e3, e4 = e4, e1, e2, e3

    l.MoveAfter(e4, e1)
    checkListPointers(l, [e1, e4, e2, e3])
    e2, e3, e4 = e4, e2, e3

    l.MoveAfter(e2, e3)
    checkListPointers(l, [e1, e3, e2, e4])


def testZeroList():
    print('testZeroList')
    l1 = List()
    l1.PushFront(1)
    checkList(l1, [1])

    l2 = List()
    l2.PushBack(1)
    checkList(l2, [1])

    l3 = List()
    l3.PushFrontList(l1)
    checkList(l3, [1])

    l4 = List()
    l4.PushBackList(l2)
    checkList(l4, [1])


def testInsertBeforeUnknownMark():
    print('testInsertBeforeUnknownMark')
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    l.InsertBefore(1, Element())
    checkList(l, [1, 2, 3])


def testInsertAfterUnknownMark():
    print('testInsertAfterUnknownMark')
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    l.InsertAfter(1, Element())
    checkList(l, [1, 2, 3])


def testMoveUnknownMark():
    print('testMoveUnknownMark')
    l1 = List()
    e1 = l1.PushBack(1)

    l2 = List()
    e2 = l2.PushBack(2)

    l1.MoveAfter(e1, e2)
    checkList(l1, [1])
    checkList(l2, [2])

    l1.MoveBefore(e1, e2)
    checkList(l1, [1])
    checkList(l2, [2])


def testIter():
    print('\ntestIter')
    l = List()
    for i in range(10):
        l.PushBack(i)
    showlist(l)
    for i in l:
        print(i, end=' ')
    print()


def main():
    test1()
    testList()
    testExtending()
    testRemove()
    test2()
    test3()
    testMove()
    testZeroList()
    testInsertBeforeUnknownMark()
    testInsertAfterUnknownMark()
    testMoveUnknownMark()
    testIter()


if __name__ == "__main__":
    main()