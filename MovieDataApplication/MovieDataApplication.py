"""
Author: Michael Rahe    
Date: 1/1/2021
About: This application is used to make a .csv file that contains data from diffrent video formats in a file to give a brake down of eachone.
"""

import os
import csv 

class MovieData:
     def __init__(self, name, year, fileSize, duration, lenght, width):
        self.name = name
        self.year = year
        self.fileSize = fileSize
        self.duration = duration
        self.length = length
        self.width = width

if __name__ == "__main__":
    csvFilename = 'temp.csv'
    moviesFilePath = 'D:\\Temp'

    csvFilePath = os.path.join('C:\\Test Folder', csvFilename)
    print('Your .csv path is: ' + csvFilePath)

    print("Starting looking through: " + moviesFilePath)

    with open(csvFilePath, 'w', newline='') as file:
        csvWriter = csv.writer(file, delimiter= ',', quotechar= '|', quoting= csv.QUOTE_MINIMAL)

        movieArr = os.listdir(moviesFilePath)

        csvWriter.writerow(['Name', ' Year', ' File Size', ' Length', ' Width'])

        for m in movieArr:
            temp = str(m)
            if temp[0] != '.':
                name = temp[:len(temp) - 7]
                year = temp[len(temp) - 5: len(temp)-1]
                print(name)
                print(year)
                csvWriter.writerow([name,year])

    print('finished')

