# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:15:05 2018

@author: ymamo
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import decileagent as da
import numpy as np

class InequalityModel(Model):
    
    '''
    Model to create human fractal network formation form first principles
    
    
    '''
    
    def __init__(self):
        self.num_agents = 10000
        self.num_decs = int(self.num_agents/10)
        # Create agents
        self.decile = self.create_deciles()
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            #get correct decile for agent population
            pos = i//1000 
            #print ((self.decile[pos][1]))
            income = self.decile[pos][0][i%self.num_decs]
            wealth=self.decile[pos][1][i%self.num_decs]
            wealth_2 = self.decile[pos][2][i%self.num_decs]
            a = da.DecileAgent(i, self, wealth, wealth_2, income,pos)
            self.schedule.add(a)

        #self.running = True
        #self.datacollector.collect(self)
        
        
    def create_deciles(self):
        
        deciles = []
        income = 0
        wealth = 10
        wealth_2 = 0
        for i in range(10):
            array_i = list(np.random.uniform(income,income +1, self.num_decs))
            array_w  = list(np.random.uniform(wealth, wealth+10, self.num_decs))
            array_w2 = list(np.random.uniform(wealth_2, wealth_2+1, self.num_decs))
            deciles.append([array_i, array_w, array_w2])
            income += 1
            wealth += 10
            #does the second wealth parameter need to increase or is it common to all deciles? 
            wealth += 1
        #print (len(deciles[0]))
        return deciles

test = InequalityModel()
print (test.schedule.agents[4999].decile)
