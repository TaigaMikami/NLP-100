'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
'''
# -*- coding: utf-8 -*-
import random

def Typoglycemia(sentence):
    result = []
    for word in sentence.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0] + ''.join(chr_list) + word[-1])
    return ' '.join(result)

sentence = input('入力>')

result = Typoglycemia(sentence)
print('変換結果' + result)


# list = ["A", "B", "C", "D", "E"]
# slice2 = list[1:-1]    # ["B", "C", "D"]

## join()
# リストを連結して一つの文字列にする

## random.shuffle(list)
# listの中身をランダムに入れ替える
