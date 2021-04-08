#importing stuff

import os
import csv
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, "r") as csv_file:

    csvreader = csv.reader(csv_file)
    next(csvreader)
    num_of_months = 0
    net_total = 0

    
    last_number = 867884

    change_list = []
    date_list = []
    maxi = 0
    mini = 1000000000
    for items in csvreader:
        date_list.append(items[0])
        num_of_months = num_of_months + 1
        current_number = int(items[1])
        change = current_number - last_number

        if change !=0:
            change_list.append(change)

        # if len(change_list) != 0:
        #     if change > change_list[-1]:
        #         maxi = change
      
        net_total = net_total + current_number

        last_number = current_number


    average = sum(change_list) / len (change_list)
    max = max(change_list)
    maxpos = change_list.index(max) 
    
    
    min = min(change_list)
    minpos = change_list.index(min)
    






print(f'''
Financial Analysis
----------------------------
Total Months: {num_of_months}
Total: ${net_total}
Average  Change: ${average}
Greatest Increase in Profits: {date_list[maxpos + 1]} (${max})
Greatest Decrease in Profits: {date_list[minpos + 1]} (${min})

''')




outF = open("Analysis/My_Output_File.txt", "w")
outF.write(f'''
Financial Analysis
----------------------------
Total Months: {num_of_months}
Total: ${net_total}
Average  Change: ${average}
Greatest Increase in Profits: {date_list[maxpos + 1]} (${max})
Greatest Decrease in Profits: {date_list[minpos + 1]} (${min})

''')
outF.write("\n")
outF.close()