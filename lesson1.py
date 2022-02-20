import _thread
import time
from time import ctime


def threadFunction(t):
	counter = 5
	while counter > 0:
		print(t + " " + ctime(time.time()))
		counter -= 1


try:
	_thread.start_new_thread(threadFunction, ("THREAD 1",))
	_thread.start_new_thread(threadFunction, ("THREAD 2",))
except:
	print("can't start the thread!")

while True:
	pass