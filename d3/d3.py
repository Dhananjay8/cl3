from random import randint
import hashlib
from math import floor

def isprime(n):
	if n==1 or n==0:
		return False
	return all([n%i for i in range(2,int(floor(n**0.5))+1)])
	
def modpow(base,exp,mod):
	ans=1
	for i in range(exp):
		ans=(ans*base)%mod
	return ans

def modinv(num,mod):
	for i in range(1,mod):
		if (num*i)%mod==1:
			return i
			
def gen_p(q):
	assert (isprime(q)), "Must be Prime!!"
	mul=2
	while True:
		p=mul*q+1
		mul+=1
		if isprime(p):
			return p
	
def gen_g(p,q):
	for h in range(2,p-1):
		g=modpow(base=h,exp=(p-1)/q,mod=p)
		if g>1:
			return g
	raise
	
def gen_keys(p,q,g):
	pr=randint(1,q-1)
	pu=modpow(base=g,exp=pr,mod=p)
	return pr,pu

def gen_hash(text):
	return int(hashlib.sha1(text).hexdigest(),16)

def gen_signature(Hm,p,q,g,pr):
	k=randint(2,q-1)
	kinv=modinv(num=k,mod=q)
	r=modpow(base=g,exp=k,mod=p)%q
	s=(kinv*(Hm+pr*r))%q
	return r,s

def verify(Hm,r,s,p,q,g,pu):
	w=modinv(num=s,mod=q)
	u1=(Hm*w)%q
	u2=(r*w)%q
	v=modpow(base=g,exp=u1,mod=p)*modpow(base=pu,exp=u2,mod=p)
	v=(v%p)%q
	print 'v & r:',v,r
	if v==r:
		return True
	return False	


q=int(raw_input("Enter q:"))
p=gen_p(q)
print "p,q :", p,q
g=gen_g(p,q)
print "g: ",g
pr,pu=gen_keys(p,q,g)
print "Private and Public Keys: ",pr,pu
text=str(raw_input("Enter Text Message: "))
hashh=gen_hash(text)
print hashh
r,s=gen_signature(hashh,p,q,g,pr)
print verify(hashh,r,s,p,q,g,pu)
