#!/usr/bin/env python
#coding: utf-8
import numpy
class Matrix(object):
    '''
    数字矩阵类
    '''
    # _row_number = None
    # _column_number = None
    def __init__(self, array_list=[[]]):
        self.array = numpy.array(array_list)
        self.array_list = array_list

    @property
    def row_number(self):
        '''
        行数，m
        '''
        return self.array.shape[0]
    
    @property
    def column_number(self):
        '''
        列数, n
        '''
        return self.array.shape[1] if len(self.array.shape) == 2 else 0
    
    