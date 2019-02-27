# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent
import random 

class DecileAgent(Agent):
    # Initiaite Each Agent
    def __init__(self, unique_id, model, wealth, rank):
        super().__init__(unique_id, model)
        # initial wealth
        self.wealth = wealth
        # which decile (economic class) agent belongs too
        self.rank = rank
        
    ############################################################################
    #   AGENT FUNCTIONS WHICH OCCUR EACH STEP
    ##############################################################################
    
    def update(self):
        pos = None
        decile = self.rank//100
                
        if decile < 90: 
            pos = 0
        elif decile >= 90 and decile < 99: 
            pos = 1
        else: 
            pos = 2
        
        
        #90, 9 and 1 split per decile
        #sav_rate = self.model.world.sav_rate[time][self.decile]
        rate_return = self.model.world.rate_ret[self.model.time][decile]
        income_yr = self.model.world.income_array[self.model.time][decile]
        #wealth_yr = self.model.world.wealth_array[self.model.time][self.decile]
        cap_gains = self.model.world.cap_gains[self.model.time][pos]
        sav_rate = self.model.world.sav_rate[self.model.time][pos]
        
        self.wealth = (1+cap_gains) * (self.wealth + sav_rate*(income_yr + self.wealth*rate_return))
       
        '''
        if random.random() < 0.5 : 
           self.income = 1 + self.income
        else: 
           self.income = change_income + 1 + self.income
        '''   
    
    def step(self):
                
        self.update()
        
        
    
        