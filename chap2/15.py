'''
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
'''
# -*- coding: utf-8 -*-

fname = 'hightemp.txt'
n = int(input('N--> '))

if n > 0:
    with open(fname) as data_file:
        lines = data_file.readlines()

    for line in lines[-n:]:
        print(l1.rstrip())

## readlines()
# 行毎のリストデータを作成する

## lines[-n:]
# リストの最後からn番目から最後まで
