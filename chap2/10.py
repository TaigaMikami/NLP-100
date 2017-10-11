'''
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
# -*- coding: utf-8 -*-

fname = 'hightemp.txt'
count = 0

with open(fname) as data_file:
    print (data_file.read().count('\n'))
    # for line in data_file:

## with open
# ファイルクローズまでやってくれる
