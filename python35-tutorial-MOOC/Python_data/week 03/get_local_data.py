# coding: utf8

__author__ = 'xray'

fp = open('./data/data.txt')
lines = []
for line in fp:
    lines.append(line)
    print(line)
print(len(lines))
fp.close()






