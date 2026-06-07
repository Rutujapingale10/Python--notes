File handling is needed to access(read,write,edit) external files .

	- Steps of file handling
	- Opening file
	- Performing some operations on file
	- Closing file
	-  
	

We can  do read write and append in file 

F = ope('file.txt','r')
f.read()
f.close()  --It is necessary to close file otherwise it leads to data corruption. 


With open('myfile.txt','a')
f.write("hey I am inside with")   //no need to close file explicitly
