#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt
import math 

#np.random.seed(1)



def simulation(arrival_rate, service_rate, total_events):
    time = np.zeros(total_events)
    q_sum = 0
    q_avg = np.zeros(total_events)
    items = np.zeros(total_events)
    wait = np.zeros(total_events)
    ns = np.zeros(total_events)
    zs = np.zeros(total_events)
    for i in range(1,total_events):# make items 
        z = np.random.random()
        L = (arrival_rate/(1-arrival_rate))
        r = (service_rate+L)
        T = (1-(r*z-service_rate)/L)
        n = np.log(T)/np.log(arrival_rate)
        n = math.ceil(n)
        ns[i] = n
        #zs[i] = z
        if n <= 0: 
            items[i] = max(0,items[i-1]-1)
        if n > 0:
            items[i] = items[i-1]+n
        time[i] = time[i-1] + np.random.exponential(1/r)
        wait[i] = time[i] - time[i-1]
        q_sum = q_sum + items[i]
        q_avg[i] = (q_sum/i)
        
    mean = np.mean(items)
    items = items.astype(int)
    num_items = np.arange(np.amax(items)+1)
    total = np.bincount(items, weights=wait)
    prob = total/total.sum()
    #print(prob)
    return mean






arrival_rate = 0.8
serv_rate = 30
means = np.zeros(52)
amean = np.zeros(52)
L = (arrival_rate/(1-arrival_rate))
for i in range(52):
    mean = simulation(arrival_rate, serv_rate,100000)
    means[i] = mean
    p_0 = ((1-((L+arrival_rate*serv_rate)/serv_rate))/(1-arrival_rate))
    gamma = ((L+arrival_rate*serv_rate)/serv_rate)
    amean[i] = (p_0*(gamma - arrival_rate)/((gamma - 1)**2))
    serv_rate = serv_rate - 0.2


plt.plot(range(50),amean[:-2], color = 'orange')
plt.scatter(range(50),means[:-2])
plt.yscale('log')
#plt.xscale('log')
plt.xlabel("service approaches lower bound")
plt.ylabel("items in queue")
plt.show()




plt.plot(range(52),amean, color = 'orange')
plt.scatter(range(52),means)
plt.yscale('log')
#plt.xscale('log')
plt.xlabel("service approaches lower bound")
plt.ylabel("items in queue")
plt.show()



