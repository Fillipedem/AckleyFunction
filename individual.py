"""
Class representing one individual(real-vectors)
"""
from ackley import ackley
from random import random, uniform
from helper import perturbation

class Individual:
    
    def __init__(self, dim=30, func=ackley, limits=[1.0]*30):
        
        # individual parameters
        self.dim = dim
        self.limits = limits
        self.func = func
        
        # initialize data
        self.values = []
        self.__initialize()

        self.std = [1.0]*30
        
    def fitness(self):
        return self.func(self.values)
        
    def __initialize(self):
        
        for j in range(self.dim):
            a = random()
            if a > 0.5:
                y = random() * self.limits[j]
            else:
                y = - random() * self.limits[j]

            self.values.append(y)
       
    @staticmethod
    def recombine(first, second):
        new = Individual(first.dim, first.func, first.limits)
        
        for i in range(first.dim):
            new.values[i] = (first.values[i] + second.values[i])/2
            
        return new
        
    @staticmethod
    def mutate(individual):
        # Copy individual
        new = Individual(individual.dim, individual.func, individual.limits)
        new.values = individual.values[:]
        new.std = individual.std[:]

        # generate pertubation
        pert = perturbation(new.dim, new.std)

        # sum
        for idx, val in enumerate(new.values):
            p = pert[idx] + val

            if p > 15:
                p = 15.0

            if p < -15:
                p = -15.0

            new.values[idx] = p

        return new
