#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:47:35 2019

@author: suryanshshukla
"""

"""
Polymorphism in single method
"""


def polm(a,b,c=0):
    z = a + b +c;
    return z
    
print(polm(1,2))
print(polm(1,2,3))