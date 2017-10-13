'''
2で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ
'''
# -*- coding: utf-8 -*-

with open('merge.txt', 'w') as out_file, \
        open('col1.txt') as col1_file, \
        open('col2.txt') as col2_file:
    for col1_line,col2_line in zip(col1_file,col2_file):
        out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')


## rstrip()
# 改行があるので　文字列を結合する際に末尾を消す

## pasteコマンド
#ファイルを水平方向に
