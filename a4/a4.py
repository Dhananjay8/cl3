import threading,random,time
from pymongo import MongoClient

class Process(threading.Thread):
	running = True
	conn=MongoClient('mongodb://admin:admin123@127.0.0.1')
	#connection = MongoClient("127.0.0.1",27017)
	count=0
	
	@staticmethod
	def ReadFromDatabase(self,index):
		print "Reading data..."
		db=Process.conn.test.a4
		limit=self.count
		cursor=db.find({"PID":index})[limit:limit+1]
		print cursor[0]
		self.count+=1
		self.count%=9

	def __init__(self,i,xname,key1,key2):
		threading.Thread.__init__(self)
		self.name=xname
		self.index=i
		self.key1=key1
		self.key2=key2

	def run(self):
		while(self.running):
			time.sleep(random.uniform(3,13))
			print '%s wants to access' % self.name
			self.access()

	def access(self):
		key11,key22=self.key1,self.key2
		while self.running:
			key11.acquire(True)
			locked=key22.acquire(False)
			if locked:
				break
			key11.release()
			print '%s acquires lock' %self.name
			key11,key22=key22,key11
		else:
			return
		self.accessing()
		key22.release()
		key11.release()

	def accessing(self):
		print '%s starts accessing database' %self.name
		Process.ReadFromDatabase(self,self.index)
		time.sleep(random.uniform(1,10))
		print '%s finishes access and leaves' %self.name

def SharedMemory():
	keys=[threading.Lock() for n in range(5)]
	processNames = ('Suarez','Coutinho','Iniesta','Busquets','Messi')
	processes=[Process(i,processNames[i],keys[i%5],keys[(i+1)%5]) for i in range(5)]
	random.seed(5627)
	Process.running=True
	for p in processes:
		p.start()
	time.sleep(10)
	Process.running=False
	print 'Finishing...'

SharedMemory()
