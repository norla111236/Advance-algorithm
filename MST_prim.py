# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:27:40 2020

@author: USER
"""
import pandas as pd 
import numpy as np
import xlrd #读取excel的库
resArray=[] #先声明一个空list
total = 0
data = xlrd.open_workbook('C:\\Users\\USER\\data minig\\algo\\MST data.xlsx') #读取文件
table = data.sheet_by_index(0) #按索引获取工作表，0就是工作表1
for i in range(table.nrows): #table.nrows表示总行数
    line=table.row_values(i) #读取每行数据，保存在line里面，line是list
    resArray.append(line) #将line加入到resArray中，resArray是二维list
resArray=np.array(resArray) #将resArray从二维list变成数组
# 刪除第一行
resArray = numpy.delete(resArray,0, axis = 0)
# 刪除第一列
resArray = numpy.delete(resArray,0, axis = 1)
# str to float 型別
resArray = resArray.astype(np.float)
#10 units
array10=[]
for i in range(table.nrows):
    line=table.row_values(i)
    array10.append(line) 
array10=np.array(array10) 
array10 = numpy.delete(array10,0, axis = 0)
array10 = numpy.delete(array10,0, axis = 1)
array10 = array10.astype(np.float)
for i in range (10,50):
    array10 = numpy.delete(array10,[10], axis = 0)
for i in range (10,50):
    array10 = numpy.delete(array10,[10], axis = 1)  
print(array10)
print('')

#20 units
array20=[]
for i in range(table.nrows):
    line=table.row_values(i)
    array20.append(line) 
array20=np.array(array20) 
array20 = numpy.delete(array20,0, axis = 0)
array20 = numpy.delete(array20,0, axis = 1)
array20 = array20.astype(np.float)
for i in range (0,30):
    array20 = numpy.delete(array20,[20], axis = 0)
for i in range (0,30):
    array20 = numpy.delete(array20,[20], axis = 1) 
print(array20)

#30 units
array30=[]
for i in range(table.nrows):
    line=table.row_values(i) 
    array30.append(line) 
array30=np.array(array30) 
array30 = numpy.delete(array30,0, axis = 0)
array30 = numpy.delete(array30,0, axis = 1)
array30 = array30.astype(np.float)
for i in range (0,20):
    array30 = numpy.delete(array30,[30], axis = 0)
for i in range (0,20):
    array30 = numpy.delete(array30,[30], axis = 1) 
print(array30)
#40 units
array40=[]
for i in range(table.nrows): 
    line=table.row_values(i) 
    array40.append(line) 
array40=np.array(array40)
array40 = numpy.delete(array40,0, axis = 0)
array40 = numpy.delete(array40,0, axis = 1)
array40 = array40.astype(np.float)
for i in range (0,10):
    array40 = numpy.delete(array40,[40], axis = 0)
for i in range (0,10):
    array40 = numpy.delete(array40,[40], axis = 1) 
print(array40)

def prim(node,array):
    total = 0
    INF = 9999999
    V = node
    G = array
    selected = [0]*node
    no_edge = 0
    selected[0] = True
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j] and G[i][j])):  
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        total = total+G[x][y]
        print(str(x+1) + "-" + str(y+1) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1
    print("total weight:"+str(total))
print("-----<<<前10點版本>>>-----")
prim(10,array10)
print("-------------------------------")
print("-----<<<前20點版本>>>-----")
prim(20,array20)
print("-------------------------------")
print("-----<<<前30點版本>>>-----")
prim(30,array30)
print("-------------------------------")
print("-----<<<前40點版本>>>-----")
prim(40,array40)
print("-------------------------------")
print("-----<<<完整50點版本>>>-----")
prim(50,resArray)
print("-------------------------------")

