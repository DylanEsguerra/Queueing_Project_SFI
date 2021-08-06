#!/usr/bin/env python
# coding: utf-8

# In[55]:


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
    
    for i in range(1,total_events):# make items 
        z = np.random.random()
        L = (arrival_rate/(1-arrival_rate))
        r = (service_rate+L)
        T = (1-(r*z-service_rate)/L)
        n = np.log(T)/np.log(arrival_rate)
        n = math.ceil(n)
        if n <= 0: 
            items[i] = max(0,items[i-1]-1)
        if n > 0:
            items[i] = items[i-1]+n
        time[i] = time[i-1] + np.random.exponential(1/r)
        wait[i] = time[i] - time[i-1]
        q_sum = q_sum + items[i]
        q_avg[i] = (q_sum/i)
        
    mean = np.mean(items)
    print(mean)
    items = items.astype(int)
    num_items = np.arange(np.amax(items)+1)
    total = np.bincount(items, weights=wait)
    prob = total/total.sum()
    print(prob)
    #savetxt('items.csv', items, delimiter=',')
    return time,items,q_avg,num_items,prob




arr_rate = float(input("arrival rate: "))
serv_rate = float(input("service rate: "))
time,items,q_avg,num_items,prob = simulation(arr_rate, serv_rate,10000)
plt.plot(time,q_avg)
#plt.plot(time,items)
plt.ylabel("average items in queue")
plt.xlabel("time")
plt.show()

#plt.scatter(range(1000),items)
#plt.ylabel("items in queue")
#plt.xlabel("time")
#plt.show()


plt.plot(num_items,prob)
plt.scatter(num_items,prob)
plt.ylabel("proability")
plt.yscale('log')
plt.xlabel("items in queue")
plt.show()


plt.plot(time,items)
plt.ylabel("items")
#plt.yscale('log')
plt.xlabel("time")
plt.show()

