#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:04:09 2019

@author: austinmccarson
"""

#import 'players.txt'

file = open('players.txt', 'r')
players = file.readlines()


def createField(players):
    
    field = []
    for player in players:
        field.append(player.replace('-','').split())
        
    return field
field = createField(players)
#print(field)

 
def categorize_by_position(field):
    
    positions = dict([('QB', []), ('RB', []), ('WR', []), ('TE', [])])
    
    for position in positions:
        for player in field:
            if position in player[-1]:
                positions[position].append(player)
                
    return positions
positions = categorize_by_position(field)
#print(positions)


def determine_mean_draft(positions):
    
    avg = {'QB':0, 'RB':0, 'WR':0, 'TE':0}
    for key,value in positions.items():
        total = 0
        for player in value:
            total += int(player[0].replace('.', ''))
        avg[key] = total/len(value)
        
    return avg
avg = determine_mean_draft(positions)
#print(avg)


#player search
for key,value in positions.items():
    for player in value:
        #if player[2] == 'Newton':
        #if 24 < int(player[0].replace('.','')) and 'TE' in player[-1]:
            print(player)
            
        
    
    