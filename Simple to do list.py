# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:11:21 2021

@author: user
"""
todolist =['Belajar Pemrograman','Makan Siang', 'Mandi Sore']
def todo():
    x = 1
    print('=======================')
    print('To Do List')
    for a in todolist:
        print(f'{x}. {a}')
        x += 1
    print('=======================')
    n = input('Tekan Enter Untuk Melihat MENU')
    if n == '':
        menu()
def menu():
    a = int(input('''
MENU
1. Tambah To Do List
2. Coret To Do List
3. Keluar
Pilih Menu : '''))
    if a == 1:
        ak = input('Tambah Aktivitas : ')
        todolist.append(ak)
        todo()
    elif a ==2:
        no = int(input('Menghapus Nomor: '))
        todolist.pop(no-1)
        todo()
    elif a == 3:
        exit()
todo()
