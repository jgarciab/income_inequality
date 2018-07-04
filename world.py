# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 19:08:17 2018

@author: ymamo

Creates the policy environment

"""

import pickle

class World:
    
    #Initiates variables for master equation
    
    def __init__(self, model): 
        self.model = model
        #self.rate_ret = 1.1
        self.sav_rate = self.pickle_open("data_abm/year2saving.dump")
        self.cap_gains = self.pickle_open("data_abm/year2capital_gains.dump")
        #self.growth_rate = 1.1
        self.income_array = self.pickle_open("data_abm/year2income.dump")
        self.wealth_array = self.pickle_open("data_abm/year2wealth.dump")
        
    #Reads in data to update varibales for master equation     
    
    def pickle_open(self, file): 
        
        with open(file, 'rb') as f:
            data = pickle.load(f)
            
        return data
        
        
        