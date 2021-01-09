# $ python3 ./name.py

print("1. before import")
import math

print("2. before functionA")
def functionA():
  print("5. Function A")

print("3. before functionB")
def functionB():
  print("6. Function B {}".format(math.sqrt(100)))

print("4. before __name__ guard")
if __name__ == '__main__':
  functionA()
  functionB()
print("7. after __name__ guard")
