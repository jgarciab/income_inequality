# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent
import random 

class DecileAgent(Agent):
    # Initiaite Each Agent
    def __init__(self, unique_id, model, wealth, decile):
        super().__init__(unique_id, model)
        # initial wealth
        self.wealth = wealth
        # which decile (economic class) agent belongs too
        self.decile = decile
        
    ############################################################################
    #   AGENT FUNCTIONS WHICH OCCUR EACH STEP
    ##############################################################################
    
    def update(self):
        
        #sav_rate = self.model.world.sav_rate[time][self.decile]
        income_yr = self.model.world.income_array[self.model.time][self.decile]
        wealth_yr = self.model.world.wealth_array[self.model.time][self.decile]
        cap_gains = self.model.world.cap_gains[self.model.time][self.decile//33]
        sav_rate = self.model.world.sav_rate[self.model.time][self.decile//33]
        
        self.wealth = (1+cap_gains) * (self.wealth + sav_rate*(income_yr + self.wealth*wealth_yr))
       
        '''
        if random.random() < 0.5 : 
           self.income = 1 + self.income
        else: 
           self.income = change_income + 1 + self.income
        '''   
    
    def step(self):
                
        self.update()
        
        
    
        