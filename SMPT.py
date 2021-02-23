import pyexcel
import math
import string
import time

'''create heap structure, and its function methods
   set the index of heap root, 1.
   minHeap is the array to store the heap. 
   meanHeap[0] stores nothing, minHeap[1:len(minHeap)-1] stores the heap.
   heapSize is len(minHeap)-1.
'''


class MyHeap:
    minHeap = [0]  # minHeap[1:] stores the heap #heapSize

    # def minHeapify(self,index):
    def delMin(self):
        if (len(self.minHeap) > 2):  # (len(minHeap)!=1) and (len(minHeap)!=2)
            self.minHeap[1] = self.minHeap[len(self.minHeap)-1]
            del self.minHeap[len(self.minHeap)-1]
            self.adjustTree(1)
        elif len(self.minHeap) == 2:
            del self.minHeap[1]
        else:
            return  # do nothing

    def adjustTree(self, i):  # recursive function
        # the node at index i being the root,
        # adjust the tree to be a min heap
        temp = self.minHeap[i]
        left = 2*i
        right = 2*i+1
        if (left <= len(self.minHeap)-1) and (self.minHeap[i][1] > self.minHeap[left][1]):
            smallest = left
        else:
            smallest = i
        if (right <= len(self.minHeap)-1) and (self.minHeap[smallest][1] > self.minHeap[right][1]):
            smallest = right
        if (smallest != i):
            self.minHeap[i] = self.minHeap[smallest]
            self.minHeap[smallest] = temp
            self.adjustTree(smallest)
        else:
            return  # the BT is already a min heap

    def insertKey(self, key):
        self.minHeap.append(key)
        index = len(self.minHeap)-1
        # print('insertKeyIndex: ',index)
        if len(self.minHeap) > 2:
            self.adjustUpward(index)

    def adjustUpward(self, i):  # recursive function
        if(i < 2):
            if (i == 0):
                raise Exception(
                    'Index in array index 0. Error. Heap starts from element 1.')
            else:  # index i ==1
                return  # at root, don't have to do adjustments
        else:  # index i >=2
            # doesn't matter whether the newly inserted key is at left or right child, because the origin arraay is a sorted minheap
            # the newly inserted heap only have to do comparison and swap with its parent, if swap is needed
            temp = self.minHeap[i]
            # print('insertKeyIndex: ',i)
            parentIndex = math.floor(i/2)
            # print('insertKeyParentIndex: ',parentIndex)
            # smallest is at index i, do swap, and continue recursion
            if (self.minHeap[parentIndex][1] > self.minHeap[i][1]):
                self.minHeap[i] = self.minHeap[parentIndex]
                self.minHeap[parentIndex] = temp
                self.adjustUpward(parentIndex)
            else:  # smallest is at index i/2, no swap, and recursion stop
                return


def nameJob(index):
    job_name = ''
    tens = math.floor(index/26)
    units = index % 26
    mapping = dict(zip(range(1, 26), string.ascii_uppercase))
    mapping[0] = 'Z'
    if (tens > 0):
        job_name += mapping.get(tens)
    job_name += mapping.get(units)
    return job_name


def runSMPT(number):
    '''read data from xlsx excel file, and store it in the pattern => job[job i,Pi,Ri]
    Pi: job process time,
    Ri: job arrive time
    '''
    data = pyexcel.get_sheet(file_name="test instance.xlsx")
    del data.column[0]

    jobs = list(data.columns())
    for job in jobs:
        # print(jobs.index(job))
        job_index = int(jobs.index(job))+1
        job_name = nameJob(job_index+1)
        job.insert(0, job_name)  # add an index for every job
    '''print(jobs, '\n')'''

    # jobs = [[1, 8, 0], [2, 10, 5], [3, 5, 12], [4, 20, 15], [5, 7, 20]]
    jobs = jobs[0:number]
    currTime = 0
    objValue = 0
    jobHeap = MyHeap()
    '''
    print('jobs\n', jobs)
    print('jobHeap\n', jobHeap.minHeap)
    print('currTime: ', currTime, '\n')
    '''
    start_time = time.time()
    if len(jobs) != 0:
        currTime = jobs[0][2]
        jobHeap.insertKey([jobs[0][0], jobs[0][1]])
        '''
        print('\nJump to time', currTime)
        print('Job ', jobs[0][0], 'arrive at time', currTime, '.')
        print('Insert job ', jobs[0][0], ' into jobHeap.')
        '''
        del jobs[0]
    else:
        raise Exception("There's no job info in xlsx file.")
    '''
    print('jobs\n', jobs)
    print('jobHeap\n', jobHeap.minHeap)
    print('currTime: ', currTime, '\n')
    '''
    while len(jobs) != 0:
        if (jobs[0][2] == currTime):
            jobHeap.insertKey([jobs[0][0], jobs[0][1]])
            '''
            print(jobs[0][0], 'arrive at time', currTime, '.')
            print('Insert job ', jobs[0][0], ' into jobHeap.\n\n')
            '''
            del jobs[0]
        # put the most recent job that haven't enter the heap into jobHeap, if needed.
        elif (jobs[0][2] > currTime):
            if len(jobHeap.minHeap) != 1:  # no need to send job into heap
                jobHeap.minHeap[1][1] -= 1
                currTime += 1
                if(jobHeap.minHeap[1][1] == 0):
                    '''
                    print("Job ", jobHeap.minHeap[1][0],
                        " complete. Delete it from jobHeap.\n\n")
                    '''
                    objValue += currTime
                    jobHeap.delMin()
            else:  # send a job into jobHeap.
                currTime = jobs[0][2]
                jobHeap.insertKey([jobs[0][0], jobs[0][1]])
                '''
                print('Jump to time', currTime)
                print('Job ', jobs[0][0], 'arrive at time', currTime, '.')
                print('Insert job ', jobs[0][0], ' into jobHeap.\n\n')
                print('currTime: ', currTime, '\n')
                '''
                del jobs[0]
        else:  # jobs[0][2]<currTime, logic error
            raise Exception(
                'Logic error. Job[0] in jobList has an arriving time that is earlier than currTime.')
        '''
        print('jobs\n', jobs)
        print('jobHeap\n', jobHeap.minHeap)
        print('currTime: ', currTime, '\n')
        '''

    while len(jobHeap.minHeap) != 1:  # no need to send job into heap
        jobHeap.minHeap[1][1] -= 1
        currTime += 1
        if(jobHeap.minHeap[1][1] == 0):
            '''
            print("Job ", jobHeap.minHeap[1][0],
                " complete. Delete it from jobHeap.\n\n")
            '''
            objValue += currTime
            jobHeap.delMin()
        '''
        print('jobs\n', jobs)
        print('jobHeap\n', jobHeap.minHeap)
        print('currTime: ', currTime, '\n')
        '''
    elapsed_time = time.time()-start_time

    print('\nNumber of jobs: ', number)
    print('The elapsed run time is ', elapsed_time)
    print("The minimum value of total processing time is ", currTime)
    print("The objective value is ", objValue)


# run different numbers of jobs'''
runSMPT(20)
runSMPT(40)
runSMPT(60)
runSMPT(80)
runSMPT(100)
