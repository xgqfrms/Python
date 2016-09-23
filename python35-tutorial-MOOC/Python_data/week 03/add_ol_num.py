# coding: utf8

__author__ = 'xray'

# filename: rev_copy.py
f1 = open('./data/company.txt', 'r')
c_Names = f1.readlines()
for i in range(0, len(c_Names)):
    c_Names[i] = str('<' + str(i + 1) + '> \n') + c_Names[i]
f1.close()

f2 = open('./data/company.txt', 'w')
# f2 = open('./data/num_company.txt', 'w')
f2.writelines(c_Names)
f2.close()







