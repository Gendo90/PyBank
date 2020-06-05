import os
import csv

#format filepath to the budget_data.csv file
budget_filepath = os.path.join('.', "Resources", "budget_data.csv")

#open the budget_data.csv file for reading
with open(budget_filepath, 'r') as budget_data:
    #convert contents of budget_data.csv file to an array
    budget_arr = csv.reader(budget_data, delimiter=",")

    #store header for column names and then go to next line
    header = next(budget_arr)

    budget_list = [(row[0], int(row[1])) for row in budget_arr]

    months = set()
    changes_arr = []
    total = 0



    for i, row in enumerate(budget_list):
        months.add(row[0])

        total += row[1]

        if(i>0):
            changes_arr.append(row[1]-int(budget_list[i-1][1]))


    max_change_profit = max(changes_arr)
    #need to add one here to index to make sure it gets the month that has
    #the change recorded, not the previous month - disallows first month from
    #being chosen!
    max_change_profit_month = budget_list[changes_arr.index(max_change_profit)+1][0]

    max_change_loss = min(changes_arr)
    #need to add one here to index to make sure it gets the month that has
    #the change recorded, not the previous month - disallows first month from
    #being chosen!
    max_change_loss_month = budget_list[changes_arr.index(max_change_loss)+1][0]


    output_strings = []

    analysis_header1 = "Financial Analysis"
    analysis_header2 = "-"*50
    output_strings.append(analysis_header1)
    output_strings.append(analysis_header2)

    months_output = "Total months: {}".format(len(months))
    output_strings.append(months_output)

    sum_total = "Total: ${:,}".format(total)
    output_strings.append(sum_total)

    avg_change = "Average Change: ${:,.2f}".format(sum(changes_arr)/len(changes_arr))
    output_strings.append(avg_change)

    greatest_inc = "Greatest Increase in Profits: {} ${:,}".format(max_change_profit_month, max_change_profit)
    output_strings.append(greatest_inc)

    greatest_decr = "Greatest Decrease in Profits: {} ${:,}".format(max_change_loss_month, max_change_loss)
    output_strings.append(greatest_decr)

    for item in output_strings:
        print(item)

#output filepath to "analysis.txt"
output_filepath = os.path.join('.', "Analysis", "output.txt")

#open file as a variable, then write to the variable:
with open(output_filepath, "w", newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter='\n')

    output_writer.writerow(output_strings)
