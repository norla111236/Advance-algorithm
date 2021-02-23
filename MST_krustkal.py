import pandas as pd 
import heapq as hq

def kruskal(nodes,edges):
    MSTsets=set({})
    nodeSets=[]
    edgeHeap=[]
    for node in nodes:
        nodeSets.append({node})
    for i in edges:
        hq.heappush(edgeHeap,i)
    # print('nodeSet',nodeSets,'\n')  
    while len(edgeHeap)>0:
        currEdge=hq.heappop(edgeHeap)
        for i in range(len(nodeSets)):
            if currEdge[1][0] in nodeSets[i] and (not currEdge[1][1] in nodeSets[i]):
                MSTsets.add((currEdge[0],tuple(currEdge[1])))
                print('add edge',currEdge)
                # print('nodeSet before add',nodeSets)
                nodeSetLen=len(nodeSets)
                for j in range(nodeSetLen):
                    if currEdge[1][1] in nodeSets[j]:
                        nodeSets[i]=nodeSets[i].union(nodeSets[j])#{currEdge[1][1]}
                        nodeSets.remove(nodeSets[j])
                        nodeSetLen-=1
                        break
                # print('nodeSet',nodeSets,'\n')
                break
    return MSTsets


def runKruskal(number):
    weights=pd.read_excel('MST data.xlsx', engine='openpyxl')#.drop(index=0).reset_index(drop=True)
    weights.drop(weights.columns[0], axis=1, inplace=True)  
    weights=weights.iloc[0:number,0:number].values.tolist()
    edgeList=[]
    for i in range(number):
        for j in range(i,number):
            if not i==j:
                edgeList.append([weights[i][j],[i+1,j+1]])
    totalweight=0
    for i in kruskal(list(range(1,number+1)),edgeList):
        print(i[1][0],'--',i[1][1],'==',i[0])
        totalweight+=i[0]
    print('total weight: ',totalweight)
    return  #kruskal(list(range(number)),edgeList)


runKruskal(10)
runKruskal(20)
runKruskal(30)
runKruskal(40)
runKruskal(50)

