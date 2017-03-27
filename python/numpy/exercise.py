# -*- coding: utf-8 -*-

import numpy as np
import pprint

pp = pprint.PrettyPrinter(indent=4)


a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print('a = ')
pp.pprint(a)

print('a.flags = ')
print(a.flags)

# 次元数
print('# 次元数')
print('a.ndim = ' + str(a.ndim))
print('a.size = ' + str(a.size))
print('a.shape = ' + str(a.shape))
print('a.itemsize = ' + str(a.itemsize))
print('a.strides = ' + str(a.strides))
print('a.nbytes = ' + str(a.nbytes))
print('a.dtype = ' + str(a.dtype))
