import os,unittest,threading
import xml.etree.ElementTree as dsp

def read(filename):
	with open(filename) as f:
		tree=dsp.parse(filename)
		root=tree.getroot()
		arr=root.text.split()
		arr=[int(x) for x in arr]
		print arr
		return arr
	
def party(arr,low,high):
	index=(low-1)
	pivot=arr[high]
	for i in range(low,high):
		if arr[i]<=pivot :
			index=index+1
			arr[i],arr[index]=arr[index],arr[i]
	arr[index+1],arr[high]=arr[high],arr[index+1]
	return (index+1)

def QS(arr,low,high):
	if low<high:
		pivot=party(arr,low,high)
		t1=threading.Thread(QS(arr,low,pivot-1))
		t2=threading.Thread(QS(arr,pivot+1,high))
		t1.start()
		t2.start()
		t1.join()
		t2.join()


class Test(unittest.TestCase):
	def test_postive(self):
		self.assertEquals(read("input.xml"),[17, 31, 3, 66, 1, 69, 25, 15, 93, 64])
	def test_negative(self):
		self.assertRaises(IOError,read,"input.txt")

lst=read('input.xml')
print lst
QS(lst,0,len(lst)-1)
print "Sorted Array:"+ str(lst)

print "\nTesting Results...."
unittest.main()
