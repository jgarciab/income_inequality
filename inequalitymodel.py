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
        self.num_decs = int(self.num_agents/10)
        self.decile = self.create_deciles()
        ###################################
        #   Create Income and Top Down World
        ######################################
        self.schedule = RandomActivation(self)
        self.world = world.World()
        #####################################
        # Create agent and add to schedule
        ########################################
        for i in range(self.num_agents):
            #get correct decile for agent population
            pos = i//1000 
            #print ((self.decile[pos][1]))
            income = self.decile[pos][0][i%self.num_decs]
            wealth=self.decile[pos][1][i%self.num_decs]
            wealth_2 = self.decile[pos][2][i%self.num_decs]
            a = da.DecileAgent(i, self, wealth, wealth_2, income,pos)
            self.schedule.add(a)
    
    ##################################################################
    # HELPER FUNCTION FOR INIT
    #################################################################         
    def create_deciles(self):
        
        decile_map = [6560, 15010, 23000, 37610, 46126, 58222, \
                      75067, 108033, 300800, 75000000000]
        wealth_map = [-962.66, 4798.06, 18753.84, 49132, 97225, 165550, 279594, 599263, \
                      1182390, 10000000 ]
        deciles = []
        income = 0
        wealth = -962.66
        wealth_2 = 0
        for i in range(10):
            array_i = list(np.random.uniform(income,decile_map[i], self.num_decs))
            array_w  = list(np.random.uniform(wealth, wealth_map[i] , self.num_decs))
            array_w2 = list(np.random.uniform(wealth_2, wealth_2+1, self.num_decs))
            deciles.append([array_i, array_w, array_w2])
            income = decile_map[i] 
            wealth += wealth_map[i]
            #does the second wealth parameter need to increase or is it common to all deciles? 
            
        #print (len(deciles[0]))
        return deciles
    
    ###########################################################################
    #  STEP FUNCTION --- WHAT OCCURS EACH YEAR
    ###########################################################################
    
    def step(self):
        self.world.update()
        self.schedule.step()

###############################################################################
#
#
#                         RUN THE MODEL
#
################################################################################
# Create an instance of the model
test = InequalityModel()

#Range indicate number of steps
for i in range(30):
    test.step()
    print (test.schedule.agents[3400].decile, test.schedule.agents[3400].wealth)
