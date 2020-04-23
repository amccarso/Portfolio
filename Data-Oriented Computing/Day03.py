#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:22:31 2019

@author: austinmccarson
"""
 


d = {}
firstyear = 1880
lastyear = 2016
nyears = lastyear - firstyear + 1
print(nyears)
for file in files[:3]:
    year = int( file[-8:-4] )
    with open(file) as f:
        lines = f.read().split('\n')
    lines = [line for line in lines if len(line)>2]
    for line in lines:
        name, gender, count = line.split(',')
        print(name, gender, count)
        if name not in d:
            #create a new default entry in d for name
            d[name] = { 'F': np.zeros(nyears, dtype=int), 
                        'M': np.zeros(nyears, dtype=int) }
            d[name][gender][year-lastyear] = int(count)
        break
      
d['John'] 


import matplotlib.pyplot as plt
plt.plot(range(firstyear,lastyear+1),d['John']['F'],color = 'skyblue')
plt.plot(range(firstyear,lastyear+1),d['John']['M'],color = 'pink')

mtotal = np.zeros(nyears, dtype=int)
mtotal = np.zeros(nyears, dtype=int)
for name in d:
    ftotal += d[name]['F']
    mtotal += d[name]['M']
ftotal

plt.plot(range(firstyear,lastyear+1),d['John']['F']/ftotal,color = 'skyblue')
plt.plot(range(firstyear,lastyear+1),d['John']['M']/mtotal,color = 'pink')
#list comprehensions
#are great! Build a new list from an existing list
        
l = 'abcd'
[ item*3 for item in l ]
[ blah*3 for blah in l if blah != 'b' ]

#plot female:
#plot male:
plt.plot(range(firstyear, lastyear+1),
         d[name]['F']/d[name]['M'],
         color='green',alpha=0.03)
if i>1000: break
plt.ylabel('F/M')

#linear scales distinguish big and small, but not big, small and very small
salaries = {'minimum wage': 11.10*40*50,
            'Candace Jones': 1.2e6,
            'Elon Musk':513e6}

import altair as alt
alt.renderers.enable('notebook')


import pandas as pd
sdf = pd.DataFrame( salaries.items(), columns=['who','$'])
sdf['log10 $'] = sdf['$'].map( np.log10 )

alt.Chart(sdf).mark_point().encode(x='who',y='$', scale=alt.Scale(type='log',zero=False))

alt.Chart(sdf).mark_point().encode(x='who',y='log10 $')


np.seterr(divide='ignore',invalid='ignore')
for i,name in enumerate(d.keys()):
    plt.plot(range(firstyear, lastyear+1),
    np.log10(d[name]['F']/d[name]['M']),
    color='green', alpha=0.03)
    if i>9000: break
plt.ylabel('F/M')
