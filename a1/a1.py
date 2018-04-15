import unittest,os
def read(filename):
	desc=open(filename,'r')
	input_arr=[]
	for i in desc:
		input_arr.append(int(i))
	return (input_arr)

def sort(lst):
	lst.sort()
	return lst

def search(lst,key,start,end):
	if(start<=end):
		mid=(end+start)/2
		if(key==lst[mid]):
			return mid
		elif(key<lst[mid]):
			return search(lst,key,start,mid-1)
		elif(key>lst[mid]):
			return search(lst,key,mid+1,end)

class Test(unittest.TestCase):
	def test_postive(self):
		self.assertEqual(search([0,1,2,3,4,5],1,0,5),1)
	def test_negative(self):
		self.assertEqual(search([0,1,2,3,4,5],10,0,5),None)

some=read("input.txt")
print "Input Array is :",some

srt=sort(some)
print "\nSorted Array is :",srt

x=input("\nEnter the key to be searched\t")
ind=search(srt,x,0,len(srt)-1)
print "\nValue found at index :",ind

print("Unit testing :")
unittest.main()
