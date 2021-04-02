#!/usr/bin/python
n=int(input("enter number:"))
#print n
prev=1
cur=1
i=0
sum=0
if(n==1):
	print(prev)
	exit()
elif(n==2):
	print(cur)
	exit()
while i != n-2 :
	sum=prev+cur
	prev=cur
	cur=sum
	i+=1
print(sum)
