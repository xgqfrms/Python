# coding: utf8

__author__ = 'xray'


'''
请完成以下文件综合编程迷你项目（提示：可以利用list的insert函数）。

(1) 创建一个文件Blowing in the wind.txt，其内容是：

(2) 在文件头部插入歌名 "Blowin' in the wind"

(3) 在歌名后插入歌手名 "Bob Dylan"

(4) 在文件末尾加上字符串

(5) 在屏幕上打印文件内容
'''
file_open = open('wind.txt', 'r+')
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
lines = file_open.readlines()

lines[0].insert("Blowin\' in the wind")
lines[1].insert("Bob Dylan")
lines.append("1962 by Warner Bros. Inc.")

for line in lines:
    print(line)
file_open.close()







