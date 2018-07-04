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
        self.world = world.World(self)
        self.time = 1966
        #####################################
        # Create agent and add to schedule
        ########################################
        for i in range(self.num_agents):
            #get correct decile for agent population
            pos = i//1000 
            #print (len(self.decile[pos]))
            wealth=self.decile[pos][i%self.num_decs]
            a = da.DecileAgent(i, self, wealth,pos)
            self.schedule.add(a)
    
    ##################################################################
    # HELPER FUNCTION FOR INIT
    #################################################################         
    def create_deciles(self, wealth):
        
        wealth_map = wealth
        
        deciles = []
        income_dics = []
        #income = 0
        #wealth = -962.66
        #wealth_2 = 0
        for i in range(99):
            array_w = list(np.random.uniform(wealth_map[i],wealth_map[i+1], self.num_decs))
            deciles.append(array_w)
       
        #print (len(deciles[0]))
        return deciles
    
    ###########################################################################
    #  STEP FUNCTION --- WHAT OCCURS EACH YEAR
    ###########################################################################
    
    def step(self):
        self.schedule.step()
        self.time += 1

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
    test.step()
    print (test.schedule.agents[3400].unique_id, test.schedule.agents[3400].wealth )
