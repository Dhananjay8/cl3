import random, math
class Dsa:
	def __init__(self):
		self.p=None
		self.q=None
		self.g=None
		self.x=None
		self.y=None
		self.k=None
		self.H=None

	def isPrime(self,a):
		if a<=1 or a%2==0:
			return False
		if a==2:
			return True
		i=3
		while i<=math.ceil(math.pow(a,0.5)):
			if a%i==0:
				return False
			i+=2
		return True

	def genG(self):
		primeList=[]
		for x in range(4,100):
			if self.isPrime(x):
				primeList.append(x)
		self.p=random.choice(primeList)
		print "Value of p is ",self.p

		for i in range(1,self.p-1):
			if (self.p-1)%i==0:
				if self.isPrime(i):
					self.q=i
		print "Value of q is ",self.q

		h=random.randint(2,self.p-1)
		print "value of h is ",h

		self.g=pow(h,(self.p-1)/self.q)%self.p
		print "value of g is ",self.g

	def genK(self):
		self.x=random.randint(1,self.q-1)
		self.y=pow(self.g,self.x)%self.p
		print "Private Key, Public Key: ", self.x,self.y

		self.k=random.randint(1,self.q-1)
		print "Value of K is ",self.k

	def createSign(self):  
		self.H=int(raw_input("Enter an Integer Hash: "))
		r=math.pow(self.g,self.k)%self.p
		r=r%self.q
		print "r component of signature is ",r#int(r)
		s=((self.H+self.x*r)/self.k)%self.q
		print "s component of signature is ",s#int(s)
		return r,s

	def calW(self,s):
		z=self.q
		s=s%self.q
		for i in range(1,z+1):
			if (s*i)%z==1%z:
				#print "got inverse"
				return i
		return pow(int(s),z-2,z)

	def calU1(self,r,s):
		return (self.H*self.calW(s))%self.q

	def calU2(self,r,s):
			return (r*self.calW(s))%self.q

	def verifySign(self,r,s):
		u1=self.calU1(r,s)
		u2=self.calU2(r,s)
		return ((math.pow(self.g,u1)*math.pow(self.y,u2))%self.p)%self.q

d=Dsa()
d.genG()
d.genK()
rc,sc=d.createSign()
v=d.verifySign(rc,sc)
print "V is ",v
