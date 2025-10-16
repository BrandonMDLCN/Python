from sys import path

path.append('..\\modules')
import module

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeros))
print(module.prodl(ones))