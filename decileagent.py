# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent
import random 

class DecileAgent(Agent):
    # Initiaite Each Agent
    def __init__(self, unique_id, model, wealth, wealth_2, income, decile):
        super().__init__(unique_id, model)
        # initial wealth
        self.wealth = wealth
        # second wealth parameter to allow for reinvestment
        self.wealth_2 = wealth_2
        # income attribute 
        self.income = income
        # which decile (economic class) agent belongs too
        self.decile = decile
        
    ############################################################################
    #   AGENT FUNCTIONS WHICH OCCUR EACH STEP
    ##############################################################################
    
    def update(self, rate_ret, sav_rate, cap_gains, growth_rate, change_income):
        
       self.wealth = (1+cap_gains) * (self.wealth + sav_rate*(self.income + self.wealth*rate_ret))
       
       if random.random() < 0.5 : 
           self.income = 1 + self.income
       else: 
           self.income = change_income + 1 + self.income
           
    
    def step(self):
        
        '''
        print (self.model.world.rate_ret, self.model.world.sav_rate, self.model.world.cap_gains, \
                    self.model.world.growth_rate, self.model.world.change_income)
        '''
        self.update(self.model.world.rate_ret, self.model.world.sav_rate, self.model.world.cap_gains, \
                    self.model.world.growth_rate, self.model.world.change_income)
        
        
    
        