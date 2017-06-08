"""
Classes for evolutionary strategies
"""
from individual import Individual
from ackley import ackley
from random import randint
import helper

class ES:
    
    def __init__(self, dim = 30, pop_size=50, limits=[1.0]*30, func=ackley, uncorrelated=True, one_step_size=True, mutation=True):
        
        # Individual and search parameters
        self.dim = dim
        self.pop_size = pop_size
        self.limits = limits
        self.func = ackley
        self.mutation = mutation
        self.one_step_size = one_step_size
        
        # mutation parameters
        self.uncorrelated = uncorrelated
        self.one_step_size = one_step_size
        self.c = 0.8
        
        # population
        self.population = []
        self.offspring = []
        self.__initialize()

        # set new minimization function
        def set_function(self, func):
            self.func = func

    # start the search
    def search(self, max_iter=2000, min_change=1e-10):
        data = [[], [], [], [], []]
        
        self.__search(0, max_iter, min_change, data)
        
        return data


    def __search(self, count, max_iter, min_change, data):
        
        # stop criteria
        p = 0
        ite = 0
        while count != max_iter:
            if p == 5:
                pop = []
                for x in self.population:
                    pop.append(x[0])

                data[0].append(ite)
                data[1].append(helper.med(pop))
                data[2].append(helper.dev(pop))
                data[3].append(helper.var(pop))
                data[4].append(min(pop, key=lambda x: x.fitness()).fitness())
                p = 0
                
            p += 1
            ite += 1
            # first check if we need to update the sigma
            self.__update_std()
            
            # create offspring
            self.__make_offspring()

            # survival selection
            self.__survival_selection()
            
            count += 1
            
        
    # offspring
    def __make_offspring(self):
        #
        num_child = 200
        self.offspring = []
        for i in range(num_child):
            
            # random select parent
            parent = randint(0, self.dim - 1)
            
            # get parent data
            individual, success, tries = self.population[parent]
            
            new_individual = Individual.mutate(individual)
            
            # check mutate success
            if individual.fitness() < new_individual.fitness():
                success += 1
                
            # update tries
            tries += 1

            # add new child
            self.offspring.append((new_individual, success, tries))

            
    # survival selection
    def __survival_selection(self):
        
        # sorted by fitness
        self.offspring.sort(key=lambda x: x[0].fitness())
        
        # get the first self.dim
        self.population = self.offspring[:self.dim]
         
    def __update_std(self):
        
        for index, pop in enumerate(self.population):
            
            #self.__one_five(index, pop)
            self.__uncorelated_update(index, pop)
                    
                    
    def __one_five(self, index, pop):
        individual, success, tries = pop

        if tries == 5:

            if success/tries > 1/5:
                for idx, s in enumerate(individual.std):
                     individual.std[idx] /= self.c

            elif success/tries <= 1/5:
                for idx, s in enumerate(individual.std):
                    individual.std[idx] *= self.c

            # update
            self.population[index] = individual, 0, 0
    
    
    def __uncorelated_update(self, index, pop):
    
        individual, success, tries = pop
    
        helper.update_step(individual.std)
        

    # initialize population
    def __initialize(self):
        
        # Adicionando uma novo elemente para a população
        for i in range(self.pop_size):
            
            individual = Individual(self.dim, self.func, self.limits)

            el = (individual, 0, 0)

            # append
            self.population.append(el)


