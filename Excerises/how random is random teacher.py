'''
    Program to generate a frequency chart on
    randomly generated integers in teh range 1 to 99
 
    --> generate N random numbers
    --> calculate frequency of each number
    --> write the integer and its frequency to a file
    --> use Pandas to analyse the data
    --> use MatPlotLib to plot a frequency diagram
 
'''
 
# Imports
import random
import pandas as pd
import matplotlib.pyplot as plt
import datetime
 
 
dataList = []       # randomly generated numbers
freqList = []       # integer and its frequency
dataString = ""     # convert to string for writing to file
 
def writeData():
    ''' write the data to a file '''
 
    global dataString
    file = open("randomData.csv", "w")  # open file for append
    file.write("data,frequency\n") # write headings
    createData()                    # create teh random data
    file.write(dataString)          # write data to file
    file.close()                    # close the file
 
def createData():
    ''' generat erandom data and count its frequency '''
    global dataString
    global freqList
 
    population = int(input("How many random numbers? "))
    # generate 50 random numbers
    print(f"Clock start: {datetime.datetime.now()}")
    for date in range(0,population ):
        dataList.append(random.randint(1, 99))       # my random data
    print(f"Clock stop: {datetime.datetime.now()}")
 
    dataList.sort()
 
    #convert integer list into list with integer and frequency
    for i in dataList:
        if i not in freqList:
            freqList.append(i)
            freqList.append(dataList.count(i))
   
    # create a  text string for writing to file
    for i in range(0, len(freqList) - 1, 2):
         dataString += f"{freqList[i]},{freqList[i + 1]}\n"
 
def plotData():
 
    ''' plot a chart '''
 
    # read in the file
    stats = pd.read_csv("sample.csv", header=0, sep=",")
 
    #print the data and some info
    print(f'Rows: {stats.shape[0]}, columns : {stats.shape[1]}')
    print(stats.info())      # print data types
    print(stats.describe())  # analyse the data
 
 
    # plot the data
    stats.plot(x="data", y="frequency", kind="bar")
 
    # display the chart
    plt.title("Fig 1.0 Average Pulse vs Calories Burned")
    plt.xlabel("Data")
    plt.ylabel("Freq")
 
    plt.ylim(ymin=0)    # start from y axis = 0
    plt.xlim(xmin=0)    # start from x axis = 0
 
    plt.show()          # show the plot
 
 
#------------------------
 
writeData()
plotData()