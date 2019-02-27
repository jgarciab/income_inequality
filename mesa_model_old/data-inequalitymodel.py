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
import world as world
import numpy as np
import pandas as pd


class InequalityModel(Model):
    
    '''
    Model to create human fractal network formation form first principles
    
    
    '''


    
    def __init__(self):
        ###################################
        #   SET INITIAL NUMBERS
        ###################################
        self.num_agents = 10000
        self.wealth_per = np.loadtxt("data_abm/init_wealth_percentile.txt")
        self.num_decs = int(self.num_agents/100)
        self.decile = self.create_deciles(self.wealth_per)
        ###################################
        #   Create Income and Top Down World
        ######################################
        self.schedule = RandomActivation(self)
        self.rank_list = []
        self.world = world.World(self)
        self.time = 1966
        #####################################
        # Create agent and add to schedule
        ########################################
        for i in range(self.num_agents):
            #get correct decile for agent population
            pos = i//100
            #print (len(self.decile[pos]))
            wealth=self.decile[pos][i%self.num_decs]
            a = da.DecileAgent(i, self, wealth,i)
            self.schedule.add(a)
            self.rank_list.append(a)
        self.datacollector = DataCollector(agent_reporters = {"Wealth" : "wealth", "Rank":"rank"})
        
    
    ##################################################################
    # HELPER FUNCTION FOR INIT
    #################################################################         
    def create_deciles(self, wealth):
        
        wealth_map = wealth
        #account for upper wealth threshold
        wealth_map = np.append(wealth_map, 100000000000.0)
        deciles = []
        income_dics = []
        #income = 0
        #wealth = -962.66
        #wealth_2 = 0
        for i in range(100):
            array_w = list(np.random.uniform(wealth_map[i],wealth_map[i+1], self.num_decs))
            array_w.sort()
            deciles.append(array_w)
       
        #print (len(deciles[0]))
        return deciles
    
    def rerank(self):
        #print (self.rank_list[5000].wealth)
        self.rank_list.sort(key=lambda x: x.wealth)
        for a in self.rank_list:
            a.rank = self.rank_list.index(a)
    ###########################################################################
    #  STEP FUNCTION --- WHAT OCCURS EACH YEAR
    ###########################################################################
    
    def step(self):
        self.rerank()
        self.schedule.step()
        self.time += 1
        self.datacollector.collect(self)
        

###############################################################################
#
#
#                         RUN THE MODEL
#
################################################################################
# Create an instance of the model
test = InequalityModel()

#Range indicate number of steps
for i in range(46):
    print (test.time)
    test.step()
    
results = test.datacollector.get_agent_vars_dataframe()
results.to_csv("results.csv")

