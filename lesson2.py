import threading
import time
from time import ctime



def threadFunction(num):
	phrase = "Thread %d: started at %s"
	print(phrase % (num, ctime(time.time())))
	time.sleep(2)
	print(phrase % (num, ctime(time.time())))


for i in range(0, 3):
	print("Creating thread %d at %s" % (i, ctime(time.time())))
	thread = threading.Thread(target=threadFunction, args=(i,))
	print("Starting thread %d at %s" % (i, ctime(time.time())))
	thread.start()
	thread.join()