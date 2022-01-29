import numpy as np
from G_code import *

f = open("myfile.txt", "w") # Leave as .txt for readability but can change to .g or . gcode

home(f)

positioning(f,'a')

####-----------------------------------------------------------------------####
#### Sample motion path, trace out 100 mm square 10 times 50mm from origin ####
####-----------------------------------------------------------------------####

motion = np.zeros((40,4))
x = np.tile([50,100,100,50],10)
y = np.tile([50,50,100,100],10)
motion[:,0] = x # x cordinate array
motion[:,1] = y # y cordinate array
motion[:,2] = 50 # z cordinate array
motion[:,3] = 1500 #feed mm/min
motion[0,3] = 700 #feed mm/min

writemotion(f,motion)
home(f)

