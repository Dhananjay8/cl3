from flask import *
app=Flask(__name__)

class plagiarismCheker:
	def __init__(self,filename):
		self.filename=filename
		self.lineScore=0
		self.wordScore=0
		self.dataLines=[]
		self.inpLines=[]
		self.dataWords=set()
		self.inpWords=set()
		
	def loadData(self):
		temp=[]
		with open(self.filename) as f:
			for lines in f:
				for line in lines.split('.'):
					line=line.replace(",",'')
					line=line.replace(".\n",'')
					line=line.replace("\n",'')
					line=line.replace(":",'')
					line=line.replace("'",'')
					line=line.lower()
					self.dataLines.append(line)
					temp=line.split()
					for val in temp:
						self.dataWords.add(val)
	def loadInput(self,string):
		temp=[]
		for line in string.split('.'):
				line=line.replace(",",'')
				line=line.replace(".\n",'')
				line=line.replace("\n",'')
				line=line.replace(":",'')
				line=line.replace("'",'')
				line=line.lower()
				self.inpLines.append(line)
				temp=line.split()
				for val in temp:
					self.inpWords.add(val)

	def scoreByWords(self):
			for dword in self.dataWords:
				for iword in self.inpWords:
					if(dword==iword):
						self.wordScore+=1
			print self.wordScore
			self.wordScore=float(self.wordScore)/float(len(self.dataWords))*100
	
	def scoreByLines(self):
			for dline in self.dataLines:
				for iline in self.inpLines:
					if(dline==iline and ((dline or iline)!='')):
						self.lineScore+=1
			print self.lineScore
			self.lineScore=float(self.lineScore)/float(len(self.dataLines))*100

	def checkPlagiarism(self):
		self.scoreByWords()
		self.scoreByLines()	
		print "Score by word matching = ",self.wordScore
		print "Score by line matching = ",self.lineScore
		print "Average Score =",float((self.wordScore+self.lineScore)/2)
		return "Score :="+str(float((self.wordScore+self.lineScore)/2))	
		
@app.route('/')
def f():
	return render_template("b2.html")
	
@app.route('/', methods=['POST'])
def g():
	obj=plagiarismCheker('data.txt')
	obj.loadData()
	line=request.form['value']
	obj.loadInput(line)
	score=obj.checkPlagiarism()
	return score
	
if __name__ == "__main__":
	app.run('localhost',debug=True)
