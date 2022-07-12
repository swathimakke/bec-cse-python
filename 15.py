def python(): 
	a=list() 
	n=int(input('How many numbers you want: ')) 
	for i in range(n): 
	 b=int(input('Enter number: ')) 
	 a.append(b) 
	print("The list is: ",a) 
	max=a[0] 
	min=a[0] 
	for i in a: 
		if i>max: 
			max=i 
		if i<min: 
			min=i 
	print('The maximum number is: ',max) 
	print('The minimum number is: ',min) 
python() 