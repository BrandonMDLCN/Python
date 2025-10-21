from sys import path

path.append('C:\\Users\\brandon.delacruz\\source\\repos\\Python\\Python-Essentials-2\\M1-Modules-packages-and-PIP\\1.3-Section-3-Modules-and-Packages\\first-module\\modules')
print(path)
import module

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeros))
print(module.prodl(ones))