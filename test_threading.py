from time import ctime, sleep
from threading import Thread

class worker(Thread):
	def run(self):
		print("entry threading worker: ", ctime())
		for x in range(0, 10):
			print(x)
			sleep(1)
		print("leave threading worker: ", ctime())

class waiter(Thread):
	def run(self):
		print("entry threading waiter: ", ctime())
		for x in range(100, 103):
			print(x)
			sleep(5)
		print("leave threading waiter: ", ctime())

def run():
	print("start run: ", ctime())
	worker().start()
	waiter().start()
	print("end run: ", ctime())

if __name__ == "__main__":
	print("entry main: ", ctime())
	run()
	print("leave main: ", ctime())
