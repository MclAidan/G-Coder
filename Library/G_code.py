
####-----------------####
#### Home all axises ####
####-----------------####

def home(f):
	f.write("G28\n") #home 
	pass


####-----------------####
#### Set positioning ####
####-----------------####

def positioning(f,t): #positioning: t = (  'a, for absolute, 'r' for realative)
	
	if t =='a' or t =='A':
		f.write("G90\n") # Set Absolute sysetm
		pass

	elif t == 'r'or t =='R':
		f.write("G91\n")  # Set Realative sysetm
		pass	
	else:
		raise ValueError('Invalid Positioning Specifier')


	pass

####--------------------------####
#### Motion array output ####
####--------------------------####

def writemotion(f,array): # array must be [n,4] in the format (x,y,z,feed)
	print(len(array))
	for i in range(len(array)):
		f.write("G1 X" + str(array[i,0]) + " Y" + str(array[i,1]) + " Z"+ str(array[i,2])+ " F"+ str(array[i,3])+"\n")
		pass

	pass

