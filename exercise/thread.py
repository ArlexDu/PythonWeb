'''
import time, threading

def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n += 1 
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
	print('thread %s is running...' % threading.current_thread().name)
	t = threading.Thread(target = loop,name='LoopThread')
	t.start()
	t.join()
	print('thread %s ended.'%threading.current_thread().name)
'''

import threading

local_school = threading.local()

def process_student():
	std = local_school.student
	print('Hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()

if __name__ =='__main__':
	t1 = threading.Thread(target = process_thread,args=('Happy',),name='Thread-A')
	t2 = threading.Thread(target = process_thread,args=('Arlex',),name='Thread-B')
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	
	