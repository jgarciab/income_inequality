# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent


class DecileAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, wealth, income, decile):
        super().__init__(unique_id, model)
        self.wealth = wealth
        self.income = income
        self.decile = decile

    def step(self):
        self.move()
        