#This is a data organization file. Files prduced via monte carlo simulation by Dr. Vogel
#provide the coordinates for both the position and classical magnetic moments for all the monomers for a given polymer configuration.
#The purpose of this program is to organize the data in a fashion similar to Quinn's data processing program.
#This way, we can keep the framwork of the tensorflow scripts on CoLab as similar as possible.
#It'll also be a script that is accesible to everyone since Quinn's program is written in MATLAB.

#You will need to move and slightly tweek the numbers in this script manually
#depending on the bin-range you're in to process the data correctly.
#The program will only work if it is within the /HOME/Bin_#-# directory (In which HOME can be path of your choosing...)
#The program will attempt to access the bin directories through the /HOME/Bin_#-#/Bin000## path.
#The file produced in this script will be written within the /HOME/Bin_#-# path.


#For my path, it will be listed as
#/Users/quantum_kitty/Documents/ML-monomer-programs/Bins_0-9


#--------------------Begin Main Program------------------
#--------------------Begin Main Program------------------
#--------------------Begin Main Program------------------
#--------------------Begin Main Program------------------
#--------------------Begin Main Program------------------
#--------------------Begin Main Program------------------

import math
import os


#set up files to be inputed to script.


#Choose the desired path write out the output file. In my terminal, this will be the default as I still work through the first bin.
myPath = "/Users/quantum_kitty/Documents/ML-monomer-programs/Bins_0-9/"

#Chose the desired bin to run through here... the value should always be a string number...
BinRun = "9"

#store all of the files in a list from a particular directory
file_path = os.listdir(myPath+"Bin0000"+BinRun)

#Though "file_path" reads and stores the files, the working directory is still the home directory. Change this with the line below.
os.chdir(myPath+"Bin0000"+BinRun)

#choose outname, the "shift-0 component will determine if we translate/rotate the data to produce more "fake" data for the machine learning algorithm.
outname =  myPath + "Bin_0000" + BinRun + "-shift-0" + "-pos" + ".csv"

Myfile = open(outname,"a")


for j in file_path:
    with open( j, 'r') as reader:
        for line in reader.readlines():        #initialize job loop (this one should go on for a while...) #before linesplit, each index is a line in the input file.
            line = line.strip()
            line = line.split() #this beaks up each number in a given line into individual elements determined by the list 'line'

            #Just in case there are float conversion issues down the line, I'm just going to do it here.
            for i in range((len(line))):      #Right now python interprets the incoming data files as string elements, iterate through each element and convert it to a float.
                line[i] = float(line[i])

            #initialize the relevent lists so that
            position = []
         #    magmoment = []
            for i in range((len(line))/6):
                #append coordinate data only to the position list.
                position.append(line[i])
                position.append(line[i+1])
                position.append(line[i+2])
                #same idea with the magnetic moment.
            #    magmoment.append(line[i+3])
            #    magmoment.append(line[i+4])
            #    magmoment.append(line[i+5])
            for i in position:
                Myfile.write(str(i)+",")
    Myfile.write("\n")
Myfile.close()
