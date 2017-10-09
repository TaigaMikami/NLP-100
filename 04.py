'''
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''
# -*- coding: utf-8 -*-


num_first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
result = {}

words = sentence.split(' ')
for (i, word) in enumerate(words,1):
    if i in num_first_only:
        result[word[0:1]] = i
    else:
        result[word[0:2]] = i

print(result);




## enumerate()
# ループする際にインデックスつきで要素を得ることができる
# 第二引数の0は開始番号 デフォルトで0
'''
>>> list1 = ['a', 'b', 'c']
>>> for (i, x) in enumerate(list1,0):
...   print i,x
...
0 a
1 b
2 c
'''

## if a in b:
# if 「検索する文字列」 in 「検索される文字列」:
