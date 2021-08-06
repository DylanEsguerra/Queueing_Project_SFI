#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt


# In[20]:
np.random.seed(1)

def simulation(arrival_rate, total_events):
    time = np.zeros(total_events)
    queue_size = np.zeros(total_events)
    q_sum = 0
    q_avg = np.zeros(total_events)
    wait = np.zeros(total_events)
    for i in range(1,total_events):
        time[i] = time[i-1] + np.random.exponential(1./(1.+arrival_rate))
        wait[i] = time[i] - time[i-1]
        queue_size[i] = max(0, queue_size[i-1]+[1,-1][np.random.random()<1./(1.+arrival_rate)])
        q_sum = q_sum + queue_size[i]
        q_avg[i] = (q_sum/i)
    queue_size = queue_size.astype(int)
    lengths = np.arange(np.amax(queue_size)+1)
    total = np.bincount(queue_size, weights=wait)
    mean = np.mean(queue_size)
    print(mean)
    prob = total/total.sum()
    #savetxt('mm1.csv', queue_size, delimiter=',')
    #savetxt('mm1_avg.csv', q_avg, delimiter=',')
    return time,queue_size,q_avg,lengths,prob


# In[21]:


arr_rate = float(input("arrival rate: "))
time,queue_size,q_avg,lengths,prob = simulation(arr_rate, 1000000)
plt.plot(time,q_avg)
plt.ylabel("average queue size")
plt.xlabel("time")
plt.show()

plt.plot(lengths,prob)
plt.scatter(lengths, prob)
plt.ylabel("proability")
plt.yscale('log')
plt.xlabel("queue length")
plt.show()

plt.plot(time,queue_size)
plt.ylabel("queue size")
#plt.yscale('log')
plt.xlabel("time")
plt.show()
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




