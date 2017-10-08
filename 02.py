'''
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
# -*- coding: utf-8 -*-

sentence1 = "パトカ−"
sentence2 = "タクシ−"
result = ''
for (tmp1,tmp2) in zip(sentence1,sentence2):
    result += tmp1 + tmp2

print(result)

## zip()
# 複数のイテラブル（リストやタプルなど）から要素を集めたリストを作るとのこと
# 例
# >>> target1 = 'abcde'
# >>> target2 = '12345'
# >>> res_zip = zip(target1, target2)
# >>> list(res_zip)
# [('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')]
