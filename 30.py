from collections import Counter 
f1=open("1.txt","w") 
f1.write(input("Enter some text: ")) 
f1.close() 
f2=open("1.txt","r") 
t=f2.read().split() 
print("The words in the file are: ",t) 
print("The most common word is: ") 
print(Counter(t).most_common(1))