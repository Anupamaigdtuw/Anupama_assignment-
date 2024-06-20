#
import csv
data_list = [
    ["University","student name "," year"," department"],
    ["DU"," Khushi","2nd","Maths" ],
    ["DU"," Ojasvani","2nd","Maths"],
    ["BHU"," urvi ","2nd","Maths"]
]
with open('firstfile.csv', 'w', newline='') as file:
     writer = csv.writer(file,delimiter='|')
     writer.writerows(data_list)