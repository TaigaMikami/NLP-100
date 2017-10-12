#!/bin/sh

# マージ
paste col1.txt col2.txt > merge_test.txt


## pasteコマンド
# ファイルを水平方向に連結する

diff --report-identical-files merge.txt merge_test.txt
