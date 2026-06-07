 async is keyword in python is used to define asynchronous functions which allow task to run without blocking the execution of other code.

It is commonly used for handling task   like network requests, database operations or file I/O
Where waiting for one task to finish would normally slow down the entire program.

Async relies on await because an async function does not execute asynchronously on its own, it needs await to actually pause and resume task.

Eg 
	Import asyncio
	
	async def func()
		Print("Hello")
		await.asyncio.sleep(2)
		Print("geek for geeks)
	asyncio.run(fun())
	
	Await - pause execution until awaited fun complete
	
	
Running Multiple task simultaneously
	With the help of async , multiple task can run without waiting for one to finish 
	
	Import asyncio 
	Async def task1()
		Print("Task 1 started")
		Await asyncio.sleep(3)
		Print("task 1 finished")
	Async def task2()
		Print("task 2 started")
		Await asyncio.sleep(1)
		Print("task 2 finished")
Async def main()
	Await asyncio.gather(task1(),task2())
	
Asyncio.run(main())

		  
		
		  
