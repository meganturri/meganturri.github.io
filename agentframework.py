# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:28:52 2021

@author: Megan
"""
import random

def distance_between (self, agent):
        return (((self.x - agent.x)**2)((self.y - agent.y)**2))**0.5

class Agent():
    
    def __init__(self, envrionment, agents):
        self.y = random.randint(0, 99)
        self.x = random.randint(0, 99)
        self.environment = envrionment
        self.store = 0  
        self.agents = agents
        self.store = 0
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y+1)%100
        else:
            self.y = (self.y-1)%100       
        if random.random() < 0.5:
            self.x = (self.x+1)%100
        else:
            self.x = (self.x-1)%100
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
    #print ("sharing" + str(dist) +" " + str(ave))