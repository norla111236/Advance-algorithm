# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:18:27 2020

@author: mimi
"""

import heapq as hq
import time
import sys

job = [[0, 6], [2, 2], [2, 3], [6, 2], [7, 5], [9, 2]]

#%% Subroutine

def cmax(job):
    Cmax = job[0][0] + job[0][1]
    for i in range(1, len(job)):
        if(job[i][0] <= Cmax):
            Cmax += job[i][1]
        else:
            Cmax = job[i][0]
            Cmax += job[i][1]
    return Cmax

#%% Depth First Search

def dfs(seq):
    
    if(len(seq) == 0):
        return []
    if(len(seq) == 1):
        return [seq]
    relst = []
    for i in range(len(seq)):
        head = seq[i]
        
        for p in dfs(seq[:i] + seq[i+1:]):
            relst.append([head] + p)
            
    return relst

#%% Best First Search

#return all branch of head
def without(head, job):
    
    jobc = job.copy()
    if(type(head[0]) == int):
        jobc.remove(head)
        return jobc
    
    for i in head:
        jobc.remove(i)
    
    return jobc

def BestFS(job):

    heaplst = []
    res = []
    for i in job:
        hq.heappush(heaplst, [cmax([i]), [i]])
    
    while(heaplst != []):
        
        head = hq.heappop(heaplst)[1]
        
        for i in without(head, job):
            headc = head.copy()
            headc.append(i)
            hq.heappush(heaplst, [cmax(headc), headc])
            headc = head.copy()
        
        if(len(head) == len(job)):
            res.append(head)              
        if(heaplst == []):
            break
    
    return res

#%% main()

Best = sys.maxsize
s = time.time()
for i in dfs(job):
    if(cmax(i) < Best):
        Best = cmax(i)
        best = i
e = time.time()
print('<<DFS>>')
print('job sequences:',best)
print('Best Cmax complete time:', Best)
print('DFS run time:', e-s)

Best = sys.maxsize
s = time.time()
for i in BestFS(job):
    if(cmax(i) < Best):
        Best = cmax(i)
        best = i 
e = time.time()
print('<<BFS>>')
print('job sequences:',best)
print('Best Cmax complete time:', Best)
print('BFS run time:', e-s)