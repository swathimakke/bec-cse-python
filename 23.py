a=list() 
n=int(input('Enter how many numbers: ')) 
for i in range(n): 
	b=input('Enter character: ') 
	a.append(b) 
print(a) 
def list_slice(S,step): 
	return[S[i::step]for i in range(step)] 
c=int(input('Enter the spling point: ')) 
print(list_slice(a,c)) 