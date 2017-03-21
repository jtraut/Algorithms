"""
Assignment Name: HW1 

Author: Jake Traut 

Description: This program sorts n random ints using selection sort and records the run time   

Additional Notes: will be prompted for input of n

Date: 9-8-15
"""
import random
import time

def selection_sort(n = 0, repeat = 1, runtimes = []):
	print 
	if n == 0:
		n = int(input("Enter a number: "))
	nums = []

	print #nicer output 
	
	for i in range(n):
		nums.append(random.randint(0, 10*n +1))
		
	#print "Unsorted list: ", nums 
	#print 
	
	start = time.clock()
	for i in range(n):
		select = nums[i]
		for j in range(i, n): 
			if select >= nums[j]:
				select = nums[j] 
				nums[i], nums[j] = nums[j], nums[i]
	end = time.clock()
	
	runtime = end - start 
			
	#print "Sorted list: ", nums	
	print 
	#print "Selection sort runtime :", runtime 
	
	runtimes.append(runtime)
	
	mintime = min(runtimes)
	maxtime = max(runtimes)	
	avgtime = sum(runtimes)/len(runtimes)
		
	#print runtimes 
	print

	print "Runtime stats on round ", repeat, "for n =", n 
	print "\nMin: ", mintime, " Max: ", maxtime, " Avg: ", avgtime	
	
	
	if repeat <= 9: 
		repeat = repeat + 1
		selection_sort(n, repeat, runtimes)
	
	
selection_sort()

