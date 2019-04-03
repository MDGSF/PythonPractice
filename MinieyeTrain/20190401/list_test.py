#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os

try:
    from list import *
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)


def listtest(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f'{func.__name__} [OK]')

    return wrapper


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


def checkPythonInnerList(l, es):
    assert len(l) == len(es)
    i = 0
    while i < len(l):
        assert l[i] == es[i]
        i += 1


def checkListLen(l, len):
    if l.Len() != len:
        print('Error l.Len() = {}, len = {}'.format(l.Len(), len))
        return False
    return True


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


@listtest
def test1():
    l = List()
    l.PushBack(4)
    l.PushBack(10)
    l.PushFront(1)
    l.PushFront(999)
    # showlist(l)
    checkList(l, [999, 1, 4, 10])

    f = l.Front()
    l.Remove(f)
    # showlist(l)
    checkList(l, [1, 4, 10])


@listtest
def testList():
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


@listtest
def testExtending():
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


@listtest
def testRemove():
    l = List()
    e1 = l.PushBack(1)
    e2 = l.PushBack(2)
    checkListPointers(l, [e1, e2])
    e = l.Front()
    l.Remove(e)
    checkListPointers(l, [e2])
    l.Remove(e)
    checkListPointers(l, [e2])


@listtest
def test2():
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


@listtest
def test3():
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


@listtest
def testMove():
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


@listtest
def testZeroList():
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


@listtest
def testInsertBeforeUnknownMark():
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    l.InsertBefore(1, Element())
    checkList(l, [1, 2, 3])


@listtest
def testInsertAfterUnknownMark():
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    l.InsertAfter(1, Element())
    checkList(l, [1, 2, 3])


@listtest
def testMoveUnknownMark():
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


@listtest
def testIter():
    l = List()
    for i in range(10):
        l.PushBack(i)

    k = 0
    for i in l:
        assert i == k
        k += 1


@listtest
def testEqual():
    l1 = List()
    l2 = List()
    l3 = List()

    l1.PushBack(1)
    l1.PushBack(2)
    l1.PushBack(3)

    l2.PushBack(1)
    l2.PushBack(2)
    l2.PushBack(3)

    l3.PushBack(4)
    l3.PushBack(2)
    l3.PushBack(3)

    assert (l1 == l2) == True
    assert (l1 != l2) == False
    assert (l1 > l2) == False
    assert (l3 > l1) == True
    assert (l1 >= l2) == True
    assert (l1 < l2) == False

    assert (l1 == l3) == False
    assert (l1 != l3) == True


@listtest
def testMaxMin():
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    assert max(l) == 3
    assert min(l) == 1


@listtest
def testSort():
    l = List()
    l.PushBack(9)
    l.PushBack(8)
    l.PushBack(7)
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)
    checkList(l, [9, 8, 7, 1, 2, 3])

    newl = sorted(l)
    assert type(newl) == list
    checkPythonInnerList(newl, [1, 2, 3, 7, 8, 9])


@listtest
def testIndex():
    l = List()
    l.PushBack(1)
    l.PushBack(2)
    l.PushBack(3)

    assert l[0] == 1
    assert l[1] == 2
    assert l[2] == 3
    # print('l[3] =', l[3]) # IndexError

    l[0] = 100
    l[1] = 200
    l[2] = 300
    checkList(l, [100, 200, 300])

    del l[1]
    checkList(l, [100, 300])


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
    testEqual()
    testMaxMin()
    testSort()
    testIndex()


if __name__ == "__main__":
    main()
