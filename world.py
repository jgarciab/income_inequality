# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 19:08:17 2018

@author: ymamo

Creates the policy environment

"""

class World:
    
    #Initiates variables for master equation
    
    def __init__(self): 
        self.rate_ret = 1.1
        self.sav_rate = 1.1
        self.cap_gains = 1.1
        self.growth_rate = 1.1
        self.change_income = 2.3
        
    #Reads in data to update varibales for master equation     
    
    def update(self):
        
        self.rate_ret += 1
        self.sav_rate += 1
        self.cap_gains += 1
        self.growth_rate += 1
        self.change_income += 1