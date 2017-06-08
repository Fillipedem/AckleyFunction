"""
Run and plot the ES results for Ackley
"""
from es import ES
import helper

es = ES(limits=[15.0]*30)

# search 30 times and get med
data = es.search(1000, 1e-5)

# plot
helper.plot(data, "ES - Ackley")
