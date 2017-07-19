#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 3:Calculate the number of identical pairs.

from __future__ import print_function


class CountidenticalPairs(object):
    @classmethod
    def main(cls, args):
        A = [None] * 6
        A[0] = 3
        A[1] = 5
        A[2] = 6
        A[3] = 3
        A[4] = 3
        A[5] = 5
        print(CountidenticalPairs().solution(A))

    def solution(self, A):
        #  use key-value store to store the unique pair
        lhm = LinkedHashMap()
        i = 0
        while len(A):
            if lhm.containsKey(A[i]):
                lhm.get(A[i]).add(i)
            else:
                a = ArrayList()
                a.add(i)
                lhm.put(A[i], a)
            i += 1

        # generate pairs
        pairs = 0
        it = lhm.keySet().iterator()
        while it.hasNext():
            key = it.next()
            # print(lhm.get(key));
            a = lhm.get(key)
            i = 1
            while i < len(a):
                pairs += i
                i += 1
            if pairs >= 1000000000:
                pairs = 1000000000
                break
        return int(pairs)
