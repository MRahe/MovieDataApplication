"""
Author: Michael Rahe    
Date: 1/1/2021
About: This application is used to make a .csv file that contains data from diffrent video formats in a file to give a brake down of eachone.
"""

import os
import csv 


csvFilename = 'temp.csv'
moviesFilePath = 'D:\\Temp'

csvFilePath = os.path.join('C:\\Test Folder', csvFilename)
print('Your .csv path is: ' + csvFilePath)


print("Starting looking through: " + moviesFilePath)

with open(csvFilePath, 'w', newline='') as file:
    csvWriter = csv.writer(file, delimiter= ',', quotechar= '|', quoting= csv.QUOTE_MINIMAL)

    arr = os.listdir(moviesFilePath)

    csvWriter.writerow(['Name', 'Year', 'File Size', 'Lenght', 'Width'])

    for f in arr:
        temp = str(f)
        if temp[0] != '.':
            print(temp)
            csvWriter.writerow([temp])



        
       
print('finished')
