# Дано слово. Переставить его s-ю букву на место k-й (s > k). При этом k-ю, (k + 1)-ю,
# ..., (s - 1)-ю буквы сдвинуть вправо на одну позицию.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    w = "abcdefgh"
    s = 5
    k = 3
    w = w[:k - 1] + w[s - 1] + w[k:s - 1] + w[k - 1] + w[s:]
    print(w)
w = w[:k] + w[k - 1:s] + w[s + 1:]
print(w)
