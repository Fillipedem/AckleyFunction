"""
Class representing one individual(real-vectors)
"""
from ackley import ackley
from random import random, uniform
from helper import pertubation

class Individual:
    
    def __init__(self, dim=30, func=ackley, limits=[1.0]*30):
        
        # individual parameters
        self.dim = dim
        self.limits = limits
        self.func = func
        
        # initialize data
        self.values = []
        self.__initialize()
        
        
    def fitness(self):
        return self.func(self.values)
        
    def __initialize(self):
        
        for j in range(self.dim):
            y = random() * self.limits[j]
        
            self.values.append(y)
       
    @staticmethod
    def mutate(individual, std):
        # Copy individual
        new = Individual(individual.dim, individual.func, individual.limits)
        new.values = individual.values[:]
        
        # generate pertubation
        pert = pertubation(new.dim, std)
        
        # sum
        for idx, val in enumerate(new.values):
            new.values[idx] += pert[idx]
        
        return new