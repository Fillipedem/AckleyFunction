"""
Run and plot the ES results for Ackley
"""
from es import ES
import helper


total_data = None
for h in range(30):
    print(h)
    es = ES(limits=[15.0]*30)
    
    # search 30 times and get med
    data = es.search(1000, 1e-5)
    
    if not total_data:
        total_data = [[], [],[],[], []]
        total_data[0] = data[0]
        total_data[1] = data[1]
        total_data[2] = data[2]
        total_data[3] = data[3]
        total_data[4] = data[4]
    else:
        for i in range(len(total_data[0])):
            total_data[1][i] += data[1][i]
            total_data[2][i] += data[2][i]
            total_data[3][i] += data[3][i]
            total_data[4][i] += data[4][i]

for i in range(len(total_data[0])):
    total_data[1][i] /= 30
    total_data[2][i] /= 30
    total_data[3][i] /= 30
    total_data[4][i] /= 30

 # plot
#helper.plot(data, "ES - Ackley")

helper.plot2(total_data, "ES - Ackley")

    

    
