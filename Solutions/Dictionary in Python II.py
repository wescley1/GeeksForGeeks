# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:13:39 2024

@author: wescl
"""

N = 7 
sum = 8 
arr = [1, 2, 3, 3, 5, 5, 5] 

def pair_sum(dict, N, arr, sum):
    
    test = {}
    
    for x in arr:
        for y in arr:
            if (x!=y):
                test[x+y] = 1
        
    if sum in test:
        return True
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    
    
    return False



    
 #   testcase -= 1

a = {}
print(pair_sum(a, N, arr, sum))