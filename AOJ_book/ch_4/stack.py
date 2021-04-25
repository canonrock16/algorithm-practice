import sys


class stack:
    def __init__(self, MAX=10):
        self.MAX = MAX
        self.S = []

    def __isEmpty__(self,):
        return len(self.S) == 0

    def __isFull__(self,):
        return len(self.S) >= self.MAX - 1

    def push(self, x):
        if self.__isFull__():
            sys.exit("overflow")
        self.S.append(x)

    def pop(self):
        if self.__isEmpty__():
            sys.exit("underflow")
        return self.S.pop()


input_list = [1, 2, "+", 3, 4, "-", "*"]
s = stack(100)
for x in input_list:
    if str(x).isdecimal():
        s.push(x)
    else:
        b = s.pop()
        a = s.pop()
        if x == "+":
            s.push(a + b)
        elif x == "-":
            s.push(a - b)
        elif x == "*":
            s.push(a * b)
print(s.pop())
