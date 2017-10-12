'''
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
'''
# -*- coding: utf-8 -*-

fname = 'hightemp.txt'
with open(fname) as data_file, \
        open('col1.txt', mode='w') as col1_file, \
        open('col2.txt', mode='w') as col2_file:
    for line in data_file:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')


## cutコマンド
# テキスト・ファイルの各行から一部分を取り出す
# -f 指定したフィールドだけ取り出す


## diffコマンド
# diff [option] ファイル名　ファイル名
# 差分を出力する
