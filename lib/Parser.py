# README
# This class is used to parse files containing lolcode
from subprocess import Popen, PIPE, STDOUT #Subprocess is used to run the lolcode through lci, the lolcode interpreter

#This method takes as an argument a file containing lolcode and read line by line
#When it encounters the <lolxd> tags it reads the text in between and runs it as lolcode
def parse(file):
	parsed = '' #Contains final parsed text after all lolcode is ran
	f = open(file,"r")

	for line in f:#Iterate through lines in file
		if(line.strip() != "<lolxd>"): #.strip() is used to remove any whitespace from the tag since it wouldn't detect <lolxd> otherwise
			parsed = parsed+line
		else:
			lolline = f.readline()
			lolcode = '' #Final lolcode after it's all read
			while(lolline.strip() != "</lolxd>"):
				lolcode = lolcode+lolline
				lolline = f.readline()
			#Run the code through lci. - is passed as an argument so it takes input through stdin instead of a file
			lciProcess = Popen(['lci','-'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
			lolcode = bytes(lolcode,'utf-8')
			stdout_data = lciProcess.communicate(input=lolcode)[0]
			parsed = parsed + stdout_data.decode('utf-8') #decode output since it's in binary as opposed to string
	return parsed