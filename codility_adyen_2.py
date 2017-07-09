#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 2: Check whether an array can be sorted by performing just one swap operation.


def solution(a):
    N = len(a)
    print a
    D = sorted(a)
    print D
    d = 0
    for i in range(0, N):
        if a[i] != D[i]:
            d += 1
    if d == 2:
        return True
    return False


if __name__ == '__main__':
    assert solution([1, 5, 3, 3, 7]) == True
    assert solution([1, 3, 5, 3, 4]) == False
    assert solution([1, 3, 5]) == True
    assert solution([1, 6, 5, 3, 3, 4, 7]) == False
    assert solution([1, 6, 3, 4, 3, 7]) == True
    assert solution([6, 3, 4, 2, 7]) == True
