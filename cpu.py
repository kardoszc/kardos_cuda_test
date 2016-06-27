#!/usr/bin/env python
#coding: utf-8
import pycuda.autoinit
import pycuda.driver as drv
import numpy
import time
import threading
from pycuda.compiler import SourceModule

def test(i,dest,a,b):
	dest[i] = a[i] * b[i]

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

a = numpy.random.randn(1000*1000).astype(numpy.float32)
b = numpy.random.randn(1000*1000).astype(numpy.float32)

dest = numpy.zeros_like(a)

threadpool=[]

start = time.time()
for i in xrange(1000*1000):
    th = threading.Thread(target= test,args= (i,dest,a,b))
    threadpool.append(th)
print time.time() - start
for th in threadpool:
    th.start()
print time.time() - start
for th in threadpool :
    threading.Thread.join( th )
print time.time() - start
