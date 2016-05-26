import numpy as np
# with open('drake.txt', 'rb') as f:
#     content = f.read().lower()

#     unwanted = ['(', ')', '\\', '"', '\'',';',':','!']
     
#     for c in unwanted:
#      content = content.replace(c,"")
    
#     words = content.split
#     print content
#version1
def lineReturn(string):
	# string = "ROUND0: 267 Ms [|GREEN|GREEN|GREEN|GREEN|]"
	wordlist = string.split()
	# print wordlist

	# here is the list require
	roundlist=wordlist[0]
	timelist = wordlist[1]
	sequentlist = wordlist[3].split("|")
	outseq = []
	Green = "GREEN"
	Red = "Red"
	Yellow = "Yellow"

	result = ""

	for i in range(1,5):
		if Green in sequentlist[i]:
			outseq.append("G")
		if sequentlist[i]== Red:
			outseq.append("R")	
		if sequentlist[i]== Yellow:
			outseq.append("Y")	
	result = timelist+","+"".join(outseq)
	print result
with open('Result_4.txt') as f:
    lines = f.readlines()
    # print "ROUND" in lines[6].replace("\n","")
    # # print lines
    for line in lines:
    	line = line.replace("\n","")
    	if "ROUND" in line:
    		lineReturn(line)
# androidfile = open("output_4raw.csv","w+")
# androidfile.write(firstline)
# androidfile.write("\n")
# 	androidfile.writelines(",".join(line)) 
# 	androidfile.write("\n")
# androidfile.close()
#verstion2
# data=[]
# # 7trials by 8 participant
# nameline = []
# def lineReturn(string):
# 	# string = "ROUND0: 267 Ms [|GREEN|GREEN|GREEN|GREEN|]"
# 	wordlist = string.split()
# 	# print wordlist
# 	# here is the list require
# 	roundlist=wordlist[0]
# 	timelist = wordlist[1]
# 	sequentlist = wordlist[3].split("|")
# 	outseq = []
# 	result = ""
# 	result = timelist
# 	return result

# with open('Result_8.txt') as f:
#     lines = f.readlines()
#     # print "ROUND" in lines[6].replace("\n","")
#     # # print lines
#     for line in lines:
#     	line = line.replace("\n","")
#     	if "ROUND" in line:
#     		result = lineReturn(line)
#     		data.append(result)


# for i in range(1,9):
# 	string = "name"+str(i)
# 	nameline.append(string)
# # print nameline
# firstline = ",".join(nameline)
# print firstline
# outputMatric= []

# outputMatric = np.reshape(data,(-1,7))
# for line in outputMatric.T:
# 	print ",".join(line)
# # print outputMatric.T

# file2metric=[]
# with open ("HCI_file.csv") as f2:
# 	lines = f2.readlines();
# 	for line in lines:
# 		file2metric.append(line.split(",")[0])
# # print np.size(file2metric)
# # print np.size(data)
# outputMatric2 = np.reshape(file2metric,(-1,7))

# for line in outputMatric2.T:
# 	print ",".join(line)
# 		# print line.replace("\n","").split()[0]
# #output process
# outputfile = open ("output_8.csv","w+")
# outputfile.write(firstline)
# outputfile.write("\n")
# for line in outputMatric.T:
# 	outputfile.writelines(",".join(line)) 
# 	outputfile.write("\n")
# outputfile.close()

# androidfile = open("output_android.csv","w+")
# androidfile.write(firstline)
# androidfile.write("\n")
# for line in outputMatric2.T:
# 	androidfile.writelines(",".join(line)) 
# 	androidfile.write("\n")
# androidfile.close()