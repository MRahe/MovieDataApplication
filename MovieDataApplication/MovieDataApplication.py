"""
Author: Michael Rahe    
Date: 1/1/2021
About: This application is used to make a .csv file that contains data from diffrent video formats in a file to give a brake down of eachone.
"""

import os
import csv 
import math
import cv2

#Globe Data
FileFormatArr= ['.mp4', '.mkv', '.m4v']

def RemoveBadFiles(arr):
    count = 0
    for m in arr:
        temp = str(m)
        if '.parts' in temp or '.ini' in temp:
            arr.pop(count)
        count+=1

#returns the total file size of a directory.
def GetFileSize(arr):
    sum = 0

    for i in arr:
        sum += os.path.getsize(os.getcwd() + '\\'+ i)

    sumGB = sum * math.pow(10, -9)
    return sumGB

def GetDimensions(filename):
    video = cv2.VideoCapture(filename)

    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)  

    arr = [height,width]
    return arr

     

if __name__ == "__main__":
    dimensionsArr = []
    csvFilename = 'temp.csv'
    moviesFilePath = 'M:\\Movies'

    csvFilePath = os.path.join('C:\\Test Folder', csvFilename)
    print('Your .csv path is: ' + csvFilePath)

    print("Starting looking through: " + moviesFilePath)

    with open(csvFilePath, 'w', newline='') as file:
        csvWriter = csv.writer(file, delimiter= ',', quotechar= '|', quoting= csv.QUOTE_MINIMAL)

        movieArr = os.listdir(moviesFilePath)

        csvWriter.writerow(['Name', ' Year', ' File Size', ' Duration', ' height', ' Width'])

        
        RemoveBadFiles(movieArr)

        for m in movieArr:
            temp = str(m)
            name = temp[:len(temp) - 7]
            year = temp[len(temp) - 5: len(temp)-1]

            os.chdir('M:\\Movies\\' + temp)

            dataArr = os.listdir(os.getcwd())
            
            size = GetFileSize(dataArr)

            for x in dataArr:
                if x[len(x) - 4: len(x)] in FileFormatArr:
                     #print(x)
                     dimensionsArr = GetDimensions(x)
               

            duration = 'Duration' 
            height = dimensionsArr[0]
            width = dimensionsArr[1]

            
            csvWriter.writerow([name,year, size, duration, height, width])
                   
    print('finished')

