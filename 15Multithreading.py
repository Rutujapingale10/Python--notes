Multithreading is a process of achieving parallelism by dividing process in multiple threads.
It is a way of achieving multitasking

Thread - Thread is nothing but subset of process 


Steps of multithreading

	- Import thread module
		○ Import threading
	- Create a Thread
		○ To create thread we create object of thread class. It takes target and args as parameter 
		○ Target - is a function to be executed 
		○ Args - argument pass to function 
		○ 
	- T1 = threading.Thread(target,args)
	- T2 = threading.Thread(target,args)
	- Start thread 
	- T1.start()
	- T2.start()
	- End the thread execution
	- T1.join()
	- T2.join()   
