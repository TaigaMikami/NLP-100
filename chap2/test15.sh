#!/bin/sh

echo -n "n--> "
read n

# 切り出し
tail -n $n hightemp.txt


## tailコマンド
# ファイルの末尾を表示する

# echo -n
# -n は出力文字の最後を改行しない
