#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:13:58 2023

@author: aquilavijayanayagam
"""

import matplotlib.pyplot as plt

data=[[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 6, 5, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 6, 5, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 10, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 10, 10, 9, 9, 1, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 10, 9, 9, 9, 1, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 10, 9, 9, 9, 1, 9, 9, 9, 9, 10, 6, 5, 10],
        [10, 10, 9, 9, 1, 9, 9, 9, 9, 9, 10, 6, 5, 10, 10],
        [10, 6, 10, 10, 9, 9, 9, 9, 10, 10, 6, 5, 5, 10, 10],
        [10, 5, 6, 10, 10, 10, 10, 10, 10, 6, 5, 5, 10, 10, 10],
        [10, 10, 5, 6, 6, 6, 6, 6, 6, 5, 5, 10, 10, 10, 10],
        [10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
      
plt.imshow(data,cmap='hot')
     