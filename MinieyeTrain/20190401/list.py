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
        self.__next = None
        self.__prev = None
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

    def swap(self, other):
        t = self.value
        self.value = other.value
        other.value = t

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, v):
        self.__next = v

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, v):
        self.__prev = v


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

    def append(self, x):
        """
        Add an item to the end of the list. Equivalent to a[len(a):] = [x].
        """
        self.__insertValue(x, self.root.prev)

    def extend(self, iterable):
        """
        Extend the list by appending all the items from the iterable.
        Equivalent to a[len(a):] = iterable.
        """
        for x in iterable:
            self.__insertValue(x, self.root.prev)

    def insert(self, i, x):
        """
        Insert an item at a given position.
        The first argument is the index of the element before which to insert,
        so a.insert(0, x) inserts at the front of the list,
        and a.insert(len(a), x) is equivalent to a.append(x).
        """
        if i < 0 or i > self.len:
            raise IndexError
        if i == 0:
            self.__insertValue(x, self.root)
        elif i == self.len:
            self.__insertValue(x, self.root.prev)
        else:
            idx = 0
            e = self.Front()
            while e is not None:
                if idx == i:
                    self.__insertValue(x, e.Prev())
                e = e.Next()
                idx += 1

    def remove(self, x):
        """
        Remove the first item from the list whose value is equal to x.
        It raises a ValueError if there is no such item.
        """
        e = self.Front()
        while e is not None:
            if e.value == x:
                self.Remove(e)
                return
            e = e.Next()
        raise ValueError

    def pop(self, *args, **kwargs):
        """
        list.pop([i])
        Remove the item at the given position in the list, and return it.
        If no index is specified, a.pop() removes and returns the last item
        in the list.
        Raises IndexError if list is empty or index is out of range.
        """
        if self.len == 0:
            raise IndexError
        if len(args) == 0:
            return self.Remove(self.Back())
        elif len(args) == 1:
            idx = args[0]
            if idx < 0 or idx >= self.len:
                raise IndexError
            i = 0
            e = self.Front()
            while e is not None:
                if i == idx:
                    return self.Remove(e)
                e = e.Next()
                i += 1
        else:
            pass

    def clear(self):
        """
        Remove all items from the list. Equivalent to del a[:].
        """
        self.root = Element()
        self.root.next = self.root
        self.root.prev = self.root
        self.len = 0

    def index(self, *args, **kwargs):
        """
        list.index(x[, start[, end]])
        Return zero-based index in the list of the first item whose value
        is equal to x. Raises a ValueError if there is no such item.

        The optional arguments start and end are interpreted as in the slice
        notation and are used to limit the search to a particular subsequence
        of the list. The returned index is computed relative to the beginning
        of the full sequence rather than the start argument.
        """
        x = None
        start = 0
        end = self.len
        if len(args) == 0:
            return

        if len(args) >= 1:
            x = args[0]

        if len(args) >= 2:
            if type(args[1]) != int:
                raise TypeError
            if args[1] < 0 or args[1] > self.len:
                raise IndexError
            start = args[1]

        if len(args) >= 3:
            if type(args[2]) != int:
                raise TypeError
            if args[2] < 0 or args[2] > self.len:
                raise IndexError
            end = args[2]

        curE = self.Front()
        i = 0
        while i < start:
            curE = curE.Next()
            i += 1
        while i < end:
            if x == curE.value:
                return i
            curE = curE.Next()
            i += 1

        raise ValueError

    def count(self, x):
        """
        Return the number of times x appears in the list.
        """
        result = 0
        e = self.Front()
        while e is not None:
            if e.value == x:
                result += 1
            e = e.Next()
        return result

    def sort(self, key=None, reverse=False):
        """
        Sort the items of the list in place
        """

        if key is None:
            key = lambda x: x

        def cmp(a, b):
            return key(a.value) < key(b.value) if reverse \
                else key(a.value) > key(b.value)

        i = 0
        while i < self.len:
            cur = self.Front()
            j = 0
            while j < self.len - i - 1:
                if cmp(cur, cur.Next()):
                    cur.swap(cur.Next())
                cur = cur.Next()
                j += 1
            i += 1

    def reverse(self):
        """
        Reverse the elements of the list in place.
        """
        leftE = self.Front()
        rightE = self.Back()
        left = 0
        right = self.len - 1
        while left < right:
            leftE.swap(rightE)
            leftE = leftE.Next()
            rightE = rightE.Prev()
            left += 1
            right -= 1

    def copy(self):
        """
        Return a shallow copy of the list. Equivalent to a[:].
        """
        shadowList = List()
        shadowList.PushBackList(self)
        return shadowList

    def Len(self):
        """Len returns the number of elements of list self."""
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
        return self.__insertValue(v, self.root)

    def PushBack(self, v):
        """
        PushBack inserts a new element e with value v at the back of
        list self and returns e.
        """
        return self.__insertValue(v, self.root.prev)

    def InsertBefore(self, v, mark):
        """
        InsertBefore inserts a new element e with value v before mark
        and returns e.
        If mark is not an element of list self, return None.
        The mark must not be None.
        """
        if mark.list != self:
            return None
        return self.__insertValue(v, mark.prev)

    def InsertAfter(self, v, mark):
        """
        InsertBefore inserts a new element e with value v after mark
        and returns e.
        If mark is not an element of list self, return None.
        The mark must not be None.
        """
        if mark.list != self:
            return None
        return self.__insertValue(v, mark)

    def Remove(self, e):
        """
        Remove removes e from list if e is an element of list self.
        It returns the element value e.value.
        The element e must not be None.
        """
        if e.list == self:
            self.__remove(e)
        return e.value

    def MoveToFront(self, e):
        """
        MoveToFront moves element e to the front of list self.
        If e is not an element of self, the list is not modified.
        The element must not be None.
        """
        if e.list != self or self.root.next == e:
            return
        self.__move(e, self.root)

    def MoveToBack(self, e):
        """
        MoveToBack moves element e to the back of list self.
        If e is not an element of self, the list is not modified.
        The element must not be None.
        """
        if e.list != self or self.root.prev == e:
            return
        self.__move(e, self.root.prev)

    def MoveBefore(self, e, mark):
        """
        MoveBefore moves element e to its new position before mark.
        If e or mark is not an element of self, or e == mark, the list
        is not modified.
        The element and mark must not be None.
        """
        if e.list != self or e == mark or mark.list != self:
            return
        self.__move(e, mark.prev)

    def MoveAfter(self, e, mark):
        """
        MoveAfter moves element e to its new position after mark.
        If e or mark is not an element of self, or e == mark, the list
        is not modified.
        The element and mark must not be None.
        """
        if e.list != self or e == mark or mark.list != self:
            return
        self.__move(e, mark)

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
            self.__insertValue(e.value, self.root.prev)
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
            self.__insertValue(e.value, self.root)
            i -= 1
            e = e.Prev()

    def __insert(self, e, at):
        """__insert e after at, increments self.len, return e"""
        n = at.next
        at.next = e
        e.prev = at
        e.next = n
        n.prev = e
        e.list = self
        self.len += 1
        return e

    def __insertValue(self, v, at):
        """
        __insertValue is a convenience wrapper for __insert(Element(v), at)
        """
        return self.__insert(Element(v), at)

    def __remove(self, e):
        """__remove removes e from its list, decrements self.len, return e"""
        e.prev.next = e.next
        e.next.prev = e.prev
        e.next = None
        e.prev = None
        e.list = None
        self.len -= 1
        return e

    def __move(self, e, at):
        """__move moves e to next to at and returns e"""
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

    def __len__(self):
        """support len(obj)"""
        return self.len

    def __iter__(self):
        """support iterable, ex. for i in list:"""
        self.iter.current = self.Front()
        return self.iter

    def __eq__(self, other):
        """support =="""
        if other is None:
            return False
        if self.Len() != other.Len():
            return False
        e1 = self.Front()
        e2 = other.Front()
        while e1 is not None:
            if e1.value != e2.value:
                return False
            e1 = e1.Next()
            e2 = e2.Next()
        return True

    def __ge__(self, other):
        """support >="""
        if other is None:
            return True
        e1 = self.Front()
        e2 = other.Front()
        while e1 is not None and e2 is not None:
            if e1.value > e2.value:
                return True
            e1 = e1.Next()
            e2 = e2.Next()
        if e1 is not None:
            return True
        if e1 is None and e2 is None:
            return True
        return False

    def __gt__(self, other):
        """support >"""
        if other is None:
            return True
        e1 = self.Front()
        e2 = other.Front()
        while e1 is not None and e2 is not None:
            if e1.value > e2.value:
                return True
            e1 = e1.Next()
            e2 = e2.Next()
        if e1 is not None:
            return True
        return False

    def __str__(self):
        """list to string, ex. print(list)"""
        first = True
        result = ""
        e = self.Front()
        while e is not None:
            if not first:
                result += " "
            else:
                first = False
            result += str(e.value)
            e = e.Next()
        return result

    def __getitem__(self, key):
        """support list[key]"""
        if type(key) != int:
            raise TypeError
        if key >= self.len or key < 0:
            raise IndexError()
        i = 0
        e = self.Front()
        while e is not None:
            if i == key:
                return e.value
            e = e.Next()
            i += 1

    def __setitem__(self, key, value):
        """support list[key] = value"""
        if type(key) != int:
            raise TypeError
        if key >= self.len or key < 0:
            raise IndexError()
        i = 0
        e = self.Front()
        while e is not None:
            if i == key:
                e.value = value
                break
            e = e.Next()
            i += 1

    def __delitem__(self, key):
        """support del list[key]"""
        if type(key) != int:
            raise TypeError
        if key >= self.len or key < 0:
            raise IndexError()
        i = 0
        e = self.Front()
        while e is not None:
            if i == key:
                self.Remove(e)
                break
            e = e.Next()
            i += 1
