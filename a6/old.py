import hashlib

def encryption(plaintext,key):
	if key=="":
		ciphertext=""
		for letter in plaintext:
			ciphertext=ciphertext+chr(ord(letter)+3)
		print "Encrypted password: ",ciphertext
		return ciphertext
	
	if key!="":
		dict={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
		vigenere_table=[['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
				['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
				['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
				['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'],
				['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D'],
				['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E'],
				['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F'],
				['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G'],
				['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H'],
				['J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I'],
				['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J'],
				['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K'],
				['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L'],
				['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M'],
				['O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
				['P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
				['Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
				['R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
				['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
				['T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
				['U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
				['V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
				['W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
				['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'],
				['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'],
				['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']]
		sup_key=""
		i=0
		for letter in plaintext:
			sup_key=sup_key+key[i]
			if i==len(key)-1:
				i=0
			else:
				i=i+1
		print "Support key is: ",sup_key
		i=0
		ciphertext=""
		for letter in plaintext:
			ciphertext=ciphertext+vigenere_table[dict[letter]][dict[sup_key[i]]]
			i=i+1

		print "Encrypted password is: ",ciphertext
		return ciphertext


usernames=[]
passwords=[]
methods=[]
keys=[]
while True:
	choice=raw_input("Enter choice:\n1. Signup\n2. Login\n3. Exit")
	if choice=="1":
		uname=raw_input("Enter the username:")
		password=raw_input("Enter the password:")
		method=raw_input("Choose method of encryption:\n1. Caesar cipher\n2. Polyalphabetic cipher\n")
		if method=="1":
			enc_pass=encryption(password,"")
			methods.append(1)
			keys.append("")
		if method=="2":
			k=raw_input("Enter the encryption key:")
			enc_pass=encryption(password,k)
			methods.append(2)
			keys.append(k)
		m=hashlib.sha1()
		m.update(enc_pass)
		digest=m.hexdigest()
		usernames.append(uname)
		passwords.append(digest)

	if choice=="2":
		uname=raw_input("Enter username:")
		password=raw_input("Enter password:")
		for i in range(len(usernames)):
			if usernames[i]==uname:
				method=methods[i]
				if method=="1":
					enc_pass=encryption(password,"")
				if method=="2":
					k=keys[i]
					enc_pass=encryption(password,k)
				m=hashlib.sha1()
				m.update(enc_pass)
				digest=m.hexdigest()
				if digest==passwords[i]:
					print "Authentication successful!"
					break
				else:
					print "Invalid password!"
					break
		if i==len(usernames):
			print "Invalid username!"
	if choice=="3":
		break
	
