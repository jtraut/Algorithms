"""
Assignment Name: HW3

Author: Jake Traut 

Description: This program takes a CSV file containing stock quotes as input and
	utilizes the maximum subarray method to compute the optimal buy and sale date 
	pair based on the open price for each day.

Additional Notes: Uses tesla, google and apple historical quotes of last 3 months 

Date: 9-22-15

"""
import math
import numpy as np 

def maxCrossingSubarray(A,low,mid,high):
	left_sum = -100000
	maxsum = 0
	max_left = 0
	max_right = high-1
	i = mid
	for i in range(mid,0,-1):
		maxsum = maxsum + (A[i])
		if maxsum > left_sum:
			left_sum = maxsum
			max_left = i
	right_sum = -100000
	maxsum = 0
	j = mid+1
	for j in range(j, high):
		maxsum = maxsum + (A[j])
		if maxsum > right_sum:
			right_sum = maxsum
			max_right = j
	return (max_left, max_right, left_sum + right_sum)
	
def maxSubarray(A,low,high):
	if high == low:
		return(low,high,(A[low-1])) #base case only one element
	else:
		originalmid = int(math.floor(len(A)/2))
		mid = int(math.floor((low+high)/2))
		#print "mid = ", mid
		(left_low,left_high,left_sum) = maxSubarray(A,low,mid)
		(right_low,right_high,right_sum) = maxSubarray(A,mid+1,high)
		(cross_low, cross_high, cross_sum) = maxCrossingSubarray(A,0,originalmid,len(A))
		if (int(left_sum >= right_sum) & int(left_sum >= cross_sum)):
			return (left_low,left_high,left_sum)
		elif (int(right_sum >= left_sum) & int(right_sum >= cross_sum)):
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)
				
def main(csvfile):
	Dates = np.genfromtxt(csvfile, delimiter=',', usecols=(0), unpack=True, dtype=str)
	B = np.genfromtxt(csvfile, delimiter=',', usecols=(3), unpack=True, dtype=float)
	A = []
	for i in range(1, len(B)-1):
		A.append(float(B[i+1]-B[i]))	
	#print A
	(low, high, max_sum) = maxSubarray(A,1,len(A))
	#print low, high, max_sum
	print csvfile,"Start Date:",Dates[len(Dates)-1],"End Date:",Dates[1],"\nBuy Date:",Dates[high],"End Date:",Dates[low],"Max Profit:", max_sum
	#return csvfile,"Start Date: ",Dates[len(Dates)-1],"End Date: ",Dates[1],"\nBuy Date:",Dates[high],"End Date:",Dates[low],"Max Profit: ", max_sum

main("TSLA.csv")
print
print 
main("GOOGL.csv")
print
print
main("AAPL.csv")


	
			
			
