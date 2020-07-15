import math
import string

#Priority Queue using Heaps
class PriorityQueue():
	def __init__(self):
		self.data = []

	def swap(self, present, parent):
		temp = self.data[present]
		self.data[present] = self.data[parent]
		self.data[parent] = temp


	def isEmpty(self):
		return len(self.data) == 0

	def enqueue(self,Pid, At, Bt):
		self.data.append({'Pid': Pid , 'At': At, 'Bt': Bt})
		self.bubbleUp()

	def dequeue(self):
		self.swap(0, len(self.data)-1)
		popped = self.data.pop()
		self.sinkDown()
		return popped

	def bubbleUp(self):
		present = (len(self.data))-1
		parent = int(math.floor((present-1)/2))

		if(parent < 0):
			return


		while self.data[parent]["At"] > self.data[present]["At"]:
			self.swap(present, parent)
			present = parent
			parent = int(math.floor((present-1)/2))
			if parent < 0:
				break






	def sinkDown(self):
		minimum = 0
		present = 0

		if len(self.data) < 2:
			return

		if len(self.data) == 2:
			if self.data[0]["At"] > self.data[1]["At"]:
				self.swap(0,1)
			return

		
		left = (2 * present) + 1
		right = (2 * present) + 2

		while self.data[present]["At"] > self.data[left]["At"] or self.data[present]["At"] > self.data[right]["At"]:
			if self.data[left]["At"] == min(self.data[left]["At"], self.data[right]["At"]):
				minimum = left
			else:
				minimum = right

			self.swap(present, minimum)

			present = minimum
			left = (2 * present) + 1
			right = (2 * present) + 2

			if left >= len(self.data):
				return

			if right >= len(self.data):
				if self.data[present]["At"] > self.data[left]["At"]:
					self.swap(present, left)
				return


def getCompletionTimes(processes):
    pQueue = PriorityQueue()
    for process in processes:
        pQueue.enqueue(**process)
    
    #Creating final Processes array
    length = len(processes)
    finalArray = []
    for i in range(length):
        finalArray.append(None)

    CompletionTime = 0

    while not pQueue.isEmpty():
        popped = pQueue.dequeue()
        CompletionTime += popped['Bt']
        newProcess = popped.copy()
        newProcess['Ct'] = CompletionTime
		newProcess['Tat'] = CompletionTime - newProcess['At']
        newProcess['Wt'] =  CompletionTime - newProcess['At'] - newProcess['At']
        finalArray[newProcess['Pid']] = newProcess
    
    return finalArray


print("enter the number of processes")
number = int(input())
processes = []
for i in range(number):
    pid, at, bt = [int(x) for x in input("Enter pid, at, bt: ").split()]
    processes.append({'Pid': int(pid), 'At':int(at), 'Bt': int(bt)})

print(getCompletionTimes(processes))


    

