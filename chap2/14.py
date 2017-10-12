'''
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''
# -*- coding: utf-8 -*-

fname = 'hightemp.txt'
n = int(input('n--> '))

with open(fname) as data_file:
    for i, line in enumerate(data_file):
        if  i >= n:
            break
        else:
            print(line.rstrip())



## enumrate()
# イテレーション付きタプルを返す。（インデックスつき）
