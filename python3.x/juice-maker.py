
# https://www.sololearn.com/learning/eom-project/1073/357


# class Juice:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity

#     def __str__(self):
#         return (self.name + ' ('+str(self.capacity)+'L)')
#     # 改写 add
#     def __add__(self, other):
#         names = Juice(self.name) + '&' + Juice(other.name)
#         capacity = ' (' + str(Juice(self.capacity + Juice(other.capacity)) + 'L)'
#         return Juice(names + capacity)
#         # return f"{self.name}&{other.name}({self.capacity + other.capacity}L)"

# class Juice:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity

#     def __str__(self):
#         return (self.name + ' ('+str(self.capacity)+'L)')
#     # 改写 add
#     def __add__(self, other):
#         return (Juice(self.name + '&' + other.name + ' (' + str(self.capacity + other.capacity) + 'L)'))
#         # return f"{self.name}&{other.name}({self.capacity + other.capacity}L)"


# ✅ __add__ !== _add__ ❌

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    # 改写 add
    def __add__(self, otherJuice):
        names = (self.name + '&' + otherJuice.name)
        capacities = (self.capacity + otherJuice.capacity)
        # 返回一个新对象
        return Juice(names, capacities);

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

# print(a)
# print(a.name)

# def add(a, b):
#     return f"{a.name}&{b.name}({a.capacity + b.capacity}L)"

# result = add(a, b)
result = a + b
print(result)


"""
python cutsom __add__


https://www.codingem.com/python-__add__-method/


https://stackoverflow.com/questions/46885618/using-add-operator-with-multiple-arguments-in-python



"""
