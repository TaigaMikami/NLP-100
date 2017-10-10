'''
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
# -*- coding: utf-8 -*-

def n_gram(target, n):
    '''指定されたリストからn-gramを作成

    引数:
    target -- 対象リスト
    n -- n-gramのn値（1ならuni-gram、2ならbi-gram...）
    戻り値:
    gramのリスト
    '''
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

set_X = set(n_gram("paraparaparadise", 2))
print('X:' + str(set_X))
set_Y = set(n_gram("paragraph", 2))
print('Y:' + str(set_Y))

set_AND = set_X & set_Y
set_OR = set_X | set_Y
set_SUB = set_X - set_Y

print('積集合:' + str(set_AND))
print('和集合:' + str(set_OR))
print('差集合:' + str(set_SUB))

if 'se' in set_X:
    print('setXにはseが含まれます')
if 'se' in set_Y:
    print('setYにはseが含まれます')

## set()
# 集合を扱うためのデータ型
# 重複する要素を持たない順序づけられた要素の集まり

## if 'fuga' in 'hogehoge':
# 文字列が含まれているかどうか真理値で返す
