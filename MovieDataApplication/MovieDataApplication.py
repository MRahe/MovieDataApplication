"""
Author: Michael Rahe    
Date: 1/1/2021
About: This application is used to make a .csv file that contains data from diffrent video formats in a file to give a brake down of eachone.
"""

import os
import csv 
import cv2

#Globe Data
FileFormatArr = ['.mp4', '.mkv', '.m4v']

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

    sumGB = sum * 10**-9
    return sumGB

#Uses cv2 to get height, width, and the runtime of the movie.
def GetDimensions(filename, moviesFilePath):
    video = cv2.VideoCapture(filename)

    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)  
    fps = video.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
    frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    runtime = (frameCount/fps)/60
    print(runtime)

    return [height,width, runtime]
    #return arr

#main function 
if __name__ == "__main__":
    dimensionsArr = []
    formatType = ''
    csvFilename = 'temp.csv'
    moviesFilePath = 'M:\\Movies'

    csvFilePath = os.path.join('C:\\Test Folder', csvFilename)
    print('Your .csv path is: ' + csvFilePath)

    print("Starting looking through: " + moviesFilePath)

    with open(csvFilePath, 'w', newline='') as file:
        csvWriter = csv.writer(file, delimiter= ',', quotechar= ' ', quoting= csv.QUOTE_MINIMAL)

        movieArr = os.listdir(moviesFilePath)

        csvWriter.writerow(['Name', ' Year', ' File Size', ' Duration', ' Width', ' Height', ' Format' ])

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
                    formatType = x[len(x) - 4: len(x)]
                    dimensionsArr = GetDimensions(x,moviesFilePath)
               
            
            height = dimensionsArr[0]
            width = dimensionsArr[1]
            duration = dimensionsArr[2] 

            csvWriter.writerow([name, year, size, duration, width, height, formatType])
                   
    print('finished')