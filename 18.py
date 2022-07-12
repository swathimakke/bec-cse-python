def factorial(n): 
	if n==1: 
		return 1 
	else: 
		return n*factorial(n-1) 
n=int(input('Enter a value: ')) 
if n<0: 
	print('Factorial is not possible for negative numbers') 
elif n==0: 
	print('Factorial of 0 is: 1') 
else:  
	print('Factorial of', n,'is: ',factorial(n))