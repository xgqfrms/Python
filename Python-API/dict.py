#!/usr/bin/python3

# ✅ 一行 OK
# dict = {'Name': 'xgqfrms', 'Age': 18, 'Class': 'First'}

# ✅ 多行错误
dict = {
  'Name': 'xgqfrms',
  'Age': 18,
  'Class': 'First',
  'Country': 'China 🇨🇳',
}

# 更新 Age
dict['Age'] = 23

# 添加信息
dict['School'] = "Python 教程"

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print ("dict['Country']: ", dict['Country'])
