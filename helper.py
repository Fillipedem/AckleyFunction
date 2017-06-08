"""
Helper Methods
"""
import numpy as np
from statistics import variance, stdev, mean
## Plot Libraries
import matplotlib.pyplot as plt
import numpy as np

def same(population):
    m = []

def med(population):
	"""
	population med
	"""
	m = []

	for c in population:
		m.append(c.fitness())


	return mean(m)


def dev(population):
	"""
	Population standard deviation
	"""
	m = []

	for c in population:
		m.append(c.fitness())


	return stdev(m)

def var(population):
	"""
	variance
	"""
	m = []

	for c in population:
		m.append(c.fitness())

	return variance(m)


def plot(data, title):
    """
	plot results from a ES algorithm
    """
    plt.plot(data[0],  (data[1]), label='Média da População')
    plt.plot(data[0], (data[2]), label='Desvio Padrão')
    plt.plot(data[0], (data[3]), label='Variância')
    plt.plot(data[0], data[4], label="Melhor Individuo")

    plt.xlabel('Número de Interações')
    plt.ylabel('Fitness')

    plt.title(title)

    plt.legend()

    plt.show()


def pertubation(dim, std):
    # media, std
    mu, sigma = 0, 1
    
    pert = np.random.normal(mu, sigma, dim)

    for idx, val in enumerate(pert):
        pert[idx] = val*std
    
    return pert