file1 = open("temp.txt","w")
L = 'this is a text file which is very good in coding. It has good effect' 
  

#file1.write("Hello \n")
file1.writelines(L)
file1.close() 
  
file1 = open("temp.txt","r+") 
  
#print("Output of Read function is ")
#print(file1.read())
text = file1.read()
line = text.split('.')
length = len(line)
i = 0;
for i in range(0,length):
    a = line[i];
    word_list = a.split()
    print(f"word count for line {i} is : {len(word_list)}");

