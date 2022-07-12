f1=open("1.txt","r")
t=f1.readlines() 
print("The content in 1st file:",t) 
f2=open("data2.txt","r") 
t1=f2.readlines() 
print("The content in 2nd file:",t1) 
print("Combining each line:") 
for i,j in zip(t,t1): 
	print((i+j).replace("\n"," "))