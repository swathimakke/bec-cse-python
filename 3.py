count=0
words=[]
maxcount=0
file=open("data2.txt","r")
for line in file:
    string=line.lower().replace(',',").replace('.',").split(" ");
    for s in string:
     words.append(s);
for i in range(0,len(words)):
   count=1;
   for j in range(i+1,len(words)):
       if(words[i]==words[j]):
          count=count+1; 
   if(count>maxcount):
        maxcount=count;
        word=words[i];
print("most repetaed word:"+word);
file.close();