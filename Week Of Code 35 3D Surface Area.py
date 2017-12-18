#!/bin/python3

import sys


def surfaceArea(A, H, W):
    # Complete this function
    top_bottom = 2 * H * W
    sides = 0
    shadow = 0
    for i in range(W):
        sides = sides + A[0][i]
    for i in range(H):
        sides = sides + A[i][0]
    for i in range(W):
        sides = sides + A[H - 1][i]
    for i in range(H):
        sides = sides + A[i][W - 1]
    for i in range(H):
        for j in range(W - 1):
            shadow = shadow + abs(A[i][j] - A[i][j + 1])
    for j in range(W):
        for i in range(H - 1):
            shadow = shadow + abs(A[i][j] - A[i + 1][j])

    return top_bottom + sides + shadow


if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A, H, W)
    print(result)
