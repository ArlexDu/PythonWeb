import time,random,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
	pass

if __name__ == '__main__':
	QueueManager.register('get_task_queue',callable=lambda:task_queue)
	QueueManager.register('get_result_queue',callable=lambda:result_queue)

	manager = QueueManager(address=('',5000),authkey=b'abc')

	manager.start()

	task = manger.get_task_queue()
	result_queue = manager.get_result_queue()

	for i in range(10):
		n = random.randint(0,10000)
		print('Put task %d...' % n)
		task.Put(n)

	print('Try get result...')

	for i in range(10):
		r =result.get(timeout = 10)
		print('Result: %s' % r)
	manager.shutdown()
	print('manger exit.')
