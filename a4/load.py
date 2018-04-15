from pymongo import MongoClient
from datetime import datetime
def LoadFromFile_StoreToDatabase(filename):
	conn=MongoClient('mongodb://%s:%s@127.0.0.1' % ('admin','admin123'))
	#connection = MongoClient("127.0.0.1",27017)
	#mongo -u admin -p admin123 --authenticationDatabase admin
	db=conn.test.a4
	
	fd=open(filename,'r').read().strip().split("\n")
	for line in fd:
		record=line.strip().split(",")
		print record
		
		record=[int(e) for e in record]
		post={"PID":record[0],"time":str(datetime.now()),"dataItem":record[1]}
		db.insert_one(post)
		
LoadFromFile_StoreToDatabase('data.txt')
