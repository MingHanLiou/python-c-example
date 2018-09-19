from ctypes import *

m = cdll.LoadLibrary("/Users/cswu/PycharmProjects/untitled1/build/lib.macosx-10.7-x86_64-3.6/demo.cpython-36m-darwin.so")
a = m.calc(c_int(3), c_int(2), c_int(4))
print(a)