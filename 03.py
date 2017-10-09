'''
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ
'''
# -*- coding: utf-8 -*-

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = []

words = sentence.split(' ')
for word in words:
    result.append(len(word) - word.count(',') - word.count('.'));

print(result)

## リストオブジェクト.count(オブジェクト)
# 指定の値を持つ要素の数をカウントする

## リストオブジェクト.append(オブジェクト)
# リストの最後に引数に指定したオブジェクトを追加する。
