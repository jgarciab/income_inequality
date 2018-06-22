# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent


class DecileAgent(Agent):
    """ An agent with fixed initial wealth."""
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

    def step(self):
        self.move()
        