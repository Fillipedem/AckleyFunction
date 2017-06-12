"""
Abstract class for optimizations functions
"""


class Optimization:
    def __init__(self, dim, limits, func):
        pass
    
    def search(self, max_iter):
        pass


"""
Cuckoo Search Implementation
"""
from .optimization import Optimization
import random

class CuckooSearch(Optimization):
    
    
    def __init__(self, dim, func, limits, num_nest=50, p=0.25):
        # search space
        self.dim = dim
        
        #
        self.__initialize(self, limits)
        
        # fitness function
        self.func = func
        
        # Cuckoo Search values
        self.nests = []
        
        # Cuckoo Search parameter
        self.num_nest = num_nest
        self.p = p
        
        
    # public methods
    def search(self, max_iter):
        
        # initialize nests
        self.__initialize()
        
        # search ans
        self.__search(max_iter)
        
        # return best solution found
        return self.nests[0]
    
    # class methods
    def __inialize_limits(self, limits):
        
        if not isinstance(limits, tuple):
            raise TypeError("args limits is not a tuple!!")
            
        if len(limits) != 2:
            raise ValueError("Len of limits is not 2!!")
        
        self.lower, self.upper = limits

    
    def __initialize(self):
        """
        Initialize nest
        :return: None
        """
        
        self.nests = []
        
        for _ in range(self.num_nest):
            new_egg = self.__random_solution()
            self.nests.append(new_egg)
        
        
    def __random_solution(self):
        
        solution = []
        
        for _ in range(self.dim):
            solution.append(random.uniform(self.lower, self.upper))
        
        return solution
        
        
    def __search(self, max_iter):
        
        
        # first steps is evaluated all eggs fitness
        nests_fitness = []
        
        for egg in self.nests:
            nests_fitness.append(self.func(egg))

        
        # while max_iter
        while max_iter:
            
            # get a random cuckoo and use levy flights
            
            
            # remove the worst solutions(Nests)
            
            
            # next ite
            max_iter -= 1