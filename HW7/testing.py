# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:23:52 2019

@author: Nate
"""
import pdb


class Cats():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def addition(self, x, y):
        return(x + y)
        
    def subtraction(self):
        return(self.x - self.y)


dog = Cats(3,4)
dog.cat = 'lets check'


pdb.set_trace()



print(dog.x)

print('testing!: ',dog.cat)

print(dog.addition())



print(dir(dog))


print(dog.__sizeof__())


print(dir(list))

print(list.__iter__)