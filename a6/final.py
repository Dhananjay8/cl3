import string
class InvalidKeyException: pass
class InvalidMode: pass
class cipher:

	@staticmethod
	def numerickeys(keystr):
		return [ord(x)- ord('a') for x in list(keystr.strip().lower())]
		
	@staticmethod
	def caesar(text,key,mode='encrypt'):
		return text.lower().translate(cipher.table(key,mode))
		
	@staticmethod
	def table(key,mode):
		a=string.ascii_lowercase
		b=a[key:]+a[:key]
		if mode=='encrypt':
			return string.maketrans(a,b)
		return string.maketrans(b,a)
	
	@staticmethod
	def vignere(text,keystr,mode='encrypt'):
		text=text.strip().lower()
		l=len(text)
		keys=cipher.numerickeys(keystr)
		tables=[cipher.table(key,mode) for key in keys]
		return "".join([c.translate(tables[i%l]) for i,c in enumerate(text)])
		
pt=raw_input("Plain Text: ")
key1=int(raw_input("Caesor Key: "))
key2=str(raw_input("Vigenere Key: "))

ct = cipher.caesar(pt,key1+1,mode='encrypt')
print "Plain Text", cipher.caesar(ct,key1+1,mode='decrypt')
print "Cipher Text", ct

ct = cipher.vignere(pt,key2,mode='encrypt')
print "Plain Text", cipher.vignere(ct,key2,mode='decrypt')
print "Cipher Text", ct
