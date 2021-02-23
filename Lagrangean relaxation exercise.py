#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:14:24 2020

@author: 209706024 & 20970640
"""
from gurobipy import *
import numpy as np
import sys
import time

largest = 0
lowest = 50
x=[]
test = input('請輸入u的數字測試上界：')
test = int(test)
pro_u=np.array(range(1,test)).tolist()
check = input('是否加入分數測試:(0表no/1表yes)')
check = int(check)
if (check == 1):
    u = 1
    for i in range(4):
        u = u/2
        pro_u.append(u)

#%%           


for u in pro_u:
    u_list=[]
    try:
        m = Model("lagrangean")
        
        x1=m.addVar(vtype=GRB.BINARY,name="x1")
        x2=m.addVar(vtype=GRB.BINARY,name="x2")
        x3=m.addVar(vtype=GRB.BINARY,name="x3")
        x4=m.addVar(vtype=GRB.BINARY,name="x4")
        
        m.update()
        
        m.setObjective((16-8*u)*x1+(10-2*u)*x2+(0-u)*x3+(4-4*u)*x4 + 10*u,GRB.MAXIMIZE)      
        m.addConstr(x1+x2<=1,"m1")       
        m.addConstr(x3+x4<=1,"m0")
        
        m.setParam(GRB.Param.PoolSolutions, 5)   
        m.setParam(GRB.Param.PoolSearchMode, 2) 
        
        starttime = time.time()
        m.optimize()
        endtime = time.time()

        nSolution = m.SolCount
        for solution in range (nSolution):
            m.setParam(GRB.Param.SolutionNumber, solution)
            if m.PoolObjVal >= m.objVal:
                x.append([u,m.Xn,m.PoolObjVal])      
                u_list = m.Xn   
                if 8*u_list[0] + 2*u_list[1] + u_list[2] + 4*u_list[3] <=10 and u_list[0] + u_list[1] <= 1 and u_list[2] +u_list[3]<=1:
                    ori_z = 16*u_list[0] + 10* u_list[1] + 4*u_list[3]
                    if lowest >= m.objVal and ori_z > largest:
                        largest = ori_z
                        lowest = m.objVal
                        best_u = u
                        best_x = [u_list[0] ,u_list[1], u_list[2], u_list[3]]
    except GurobiError:
        print('Encountered a Gurobi error')
    
    except AttributeError:
        print('Encountered an attribute error')
print("--------------------------------------------------------------------")
print("result of the define range of u:")
print("Total :",endtime-starttime)
print("best of u:",best_u)
print("best of X:",best_x)
print("lowest Zu we can find:",lowest)
print("largest z:",largest)


for i , v in enumerate(x):
    if 8*v[1][0] + 2*v[1][1] + v[1][2] + 4*v[1][3] <=10 and v[1][0] + v[1][1] <= 1 and v[1][2] +v[1][3]<=1:
        x[i].append(16*v[1][0] + 10* v[1][1] + 4*v[1][3])
    else:
        x[i].append('error')
print("--------------------------------------------------------------------")
print("answer testing with original problem:")
print("(error represent not exist)")
print(x)