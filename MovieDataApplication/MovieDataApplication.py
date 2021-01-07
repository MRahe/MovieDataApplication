"""
Author: Michael Rahe    
Date: 1/1/2021
About: This application is used to make a .csv file that contains data from diffrent video formats in a file to give a brake down of eachone.
"""

import os
import csv 
import math

class MovieData:
     def __init__(self, name, year, fileSize, duration, lenght, width):
        self.name = name
        self.year = year
        self.fileSize = fileSize
        self.duration = duration
        self.length = length
        self.width = width

def RemoveBadFiles(arr):
    count = 0
    for m in arr:
        temp = str(m)
        if '.parts' in temp or '.ini' in temp:
            arr.pop(count)
        count+=1

        #reurns the
def GetFileSize(arr):
    sum = 0

    for i in arr:
        sum += os.path.getsize(os.getcwd() + '\\'+ i)
    sumGB = sum * math.pow(10, -9)
    return sumGB
  
        

if __name__ == "__main__":
    csvFilename = 'temp.csv'
    moviesFilePath = 'M:\\Movies'

    csvFilePath = os.path.join('C:\\Test Folder', csvFilename)
    print('Your .csv path is: ' + csvFilePath)

    print("Starting looking through: " + moviesFilePath)

    with open(csvFilePath, 'w', newline='') as file:
        csvWriter = csv.writer(file, delimiter= ',', quotechar= '|', quoting= csv.QUOTE_MINIMAL)

        movieArr = os.listdir(moviesFilePath)

        csvWriter.writerow(['Name', ' Year', ' File Size', ' duration', ' Length', ' Width'])

        
        RemoveBadFiles(movieArr)
  

        for m in movieArr:
            temp = str(m)
            name = temp[:len(temp) - 7]
            year = temp[len(temp) - 5: len(temp)-1]

            #print(name)
            #print(year)

            os.chdir('M:\\Movies\\' + temp)

            print("Current working directory is:" + os.getcwd())

            dataArr = os.listdir(os.getcwd())
            size = GetFileSize(dataArr)

            csvWriter.writerow([name,year, size])
            #os.chdir('..')
            

            
                

    print('finished')

