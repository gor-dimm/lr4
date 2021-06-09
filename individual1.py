#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано название футбольного клуба. Напечатать его на экране «столбиком».

if __name__ == '__main__':
    a = input("Введите название футбольной команды: ")
    for counter in range(len(a)):
     print(a[counter],end = '\n')
