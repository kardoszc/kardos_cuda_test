#!/usr/bin/env python
#coding: utf-8
import pycuda.autoinit
import pycuda.driver as drv
import numpy
import time
from pycuda.compiler import SourceModule
mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
  int n = 0;
  for(n=0;n<=9999;n+=1) 
  {
  const int i = threadIdx.x + n * 1000;
  dest[i] = a[i] * b[i];
  }
}
""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(1000*10000).astype(numpy.float32)
b = numpy.random.randn(1000*10000).astype(numpy.float32)

dest = numpy.zeros_like(a)


# cuda计算
start = time.time()
multiply_them(
        drv.Out(dest), drv.In(a), drv.In(b),
        block=(1000,1,1), grid=(1,1))
print time.time() - start

for i in dest - a*b:
    if i != 0:
    	print i 

# for i in range(len(a)):
# 	dest[i] = a[i] * b[i]

# print time.time() - start
