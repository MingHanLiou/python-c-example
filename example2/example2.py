from ctypes import cdll, c_double, c_size_t
from numpy.ctypeslib import ndpointer
import numpy as np

m = cdll.LoadLibrary(r".\c_function.dll")
m.foo.restype = None
m.foo.argtypes = [ndpointer(c_double, flags="C_CONTIGUOUS"),
                  c_size_t,
                  ndpointer(c_double, flags="C_CONTIGUOUS")]



if __name__ == '__main__':

    a = np.array([1., 2., 3.])
    b = np.ndarray((3,))

    m.foo(a, a.size, b)

    print(b)
