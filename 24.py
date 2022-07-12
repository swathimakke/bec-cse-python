from collections import Counter 
a=list() 
b=list() 
n=int(input("Enter size of 1st list: ")) 
for i in range(n): 
	c=input("Enter strings: ") 
	a.append(c) 
n1=int(input("Enter size of 2nd list: ")) 
for i in range(n1): 
	c=input("Enter strings: ") 
	b.append(c) 
Counter1=Counter(a) 
print(Counter1) 
Counter2=Counter(b) 
print(Counter2) 
print('The difference between first list and second list is : ', 
list(Counter1-Counter2)) 
print('The difference between second list and first list is : ', 
list(Counter2-Counter1))