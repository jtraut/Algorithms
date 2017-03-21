"""
Assignment Name: HW7

Author: Jake Traut 

Description: Cutting cloth problem, 
 optimize the profit of products you can make with a single piece of cloth with X x Y dimension. 

Additional Notes: Program reads two files as input arguments, 
 the input file with the data to examine and
 output file to return max profit P and total number of cuts T along with the individual cuts. 

Date: 10-27-15

"""
import sys

filename = sys.argv[-1]

if (filename == "Traut_Jake_HW7.py"): #recieved no command line input
	filename = "cloth.txt"

values = []

with open(filename,'r') as f:
    for line in f:
        for word in line.split():
           values.append(int(word))

X = values[0] #cloth width 
#print X

Y = values[1] #cloth height
#print Y

n = values[2] #number of products 
#print n

a = [] #product width
b = [] #product height
c = [] #product selling price 

for i in range(1,n+1):
	j = i*3
	a.append(values[j])
	b.append(values[j+1])
	c.append(values[j+2])
#print a, b, c

rect = [[0 for y in range(Y+1)] for x in range(X+1)] #matrix for storing specific cloth product prices of dimension i x j
P = [[0 for y in range(Y+1)] for x in range(X+1)] #matrix for storing max return sales

for i in range(0,n):
	if(rect[a[i]][b[i]] < c[i]):
		rect[a[i]][b[i]] = c[i]	 #filling in cost values for specific rectangles 


def cuttingCloth(i,j): #calculate max return 
	T = 0
	if P[i][j] != 0:
		return P[i][j]
	else:
		for i in range(1,X+1):
			for j in range(1,Y+1):
				
				tempMax1 = P[1][j]+P[i-1][j]
				for a in range(2,i):
					temp = P[a][j]+P[i-a][j]
					if temp > tempMax1:
						tempMax1 = temp
						
				tempMax2 = P[i][j-1]+P[i][1]
				for b in range(2,j):
					temp = P[i][j-b]+P[i][b]
					if temp > tempMax2:
						tempMax2 = temp
							
				P[i][j] = max(tempMax1,tempMax2,rect[i][j]); 
		
		print "Maximal profit: ", P[i][j] 
		return P[i][j]
		
cuttingCloth(X,Y)		
		
	

			
	
			
