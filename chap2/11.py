'''
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
# -*- coding: utf-8 -*-

fname = 'hightemp.txt'
count = 0

with open(fname) as data_file:
    for line in data_file:
        print(line.replace('\t', ' '), end='')


## replace(a,b)
# aをbに置換する

## end=''
#改行なし
