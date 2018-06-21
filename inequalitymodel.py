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
        # Create agents
        self.decile = self.create_deciles()
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            #get correct decile for agent population
            pos = i//1000 
            #print ((self.decile[pos][1]))
            income = self.decile[pos][0][i%1000]
            wealth=self.decile[pos][1][i%1000]
            a = da.DecileAgent(i, self, wealth, income,pos)
            self.schedule.add(a)

        #self.running = True
        #self.datacollector.collect(self)
        
        
    def create_deciles(self):
        
        deciles = []
        income = 0
        wealth = 10
        for i in range(10):
            array_i = list(np.random.uniform(income,income +1, 1000))
            array_w  = list(np.random.uniform(wealth, wealth+10, 1000))
            deciles.append([array_i, array_w])
            income += 1
            wealth += 10
        #print (len(deciles[0]))
        return deciles

test = InequalityModel()
print (test.schedule.agents[4999].decile)
