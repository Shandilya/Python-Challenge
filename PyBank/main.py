# import dependencies
import os
import csv
import sys
budget_data_csv = os.path.join("C:/Users/Deepti/washu/WASHSTL201806DATA4-Class-Repository-DATA/Week 3 - Python/Homework/PyBank/Resources","budget_data.csv")
# open and read csv commands
with open(budget_data_csv, newline ="") as calculatingbudgetdatacsvfile:
    csvreader = csv.reader(calculatingbudgetdatacsvfile, delimiter = ',')
    csv_header = next(calculatingbudgetdatacsvfile) 
    monthscount = []
    sumtotal = []
    totaldiff = []
    averagechange= []
    revchange = []
    date = []
    z = 0
    # Looping
    for row in csvreader:
        monthscount.append(int(row[1]))
        sumtotal.append(int(row[1]))
        date.append(row[0])
        
    for i in range (0 ,len(sumtotal)): 
        #Checking the output below to ensure it is calculating right. Displaying the output for reference.
        print("sumtotal values " + "i :" + str(i) + "  " + str(sumtotal[i]))

    # Testing code to check whether the sum and total months are correct.
    #print("total months " + str(len(monthscount)))
    #print("sum total  "  + str(sum(sumtotal)))
   

    revchange.append(sumtotal[0])
    for i in range (1 ,len(sumtotal)): 
        revchange.append(sumtotal[i] - sumtotal[i-1])
    
    for i in range (0 ,len(revchange)):
        #Below code to check whether the revenue change is correct and as per the given index. Displaying the output for reference and cross check.
        print("Revchange " + str(i) + " " + str(revchange[i]))
        #revchange.append(sumtotal[i] - sumtotal[i-1])
        

        averagecal =sum(revchange) / len(revchange)
        #print("avg difference is " + str(averagecal))
        greatincprofit = max(revchange)
        #print(greatincprofit)
        greatdecprofit = min(revchange)
        #print(greatdecprofit)
        #print("max value" + str(sumtotal.index(max(revchange))))
        maxdate = str(date[revchange.index(max(revchange))])
        mindate = str(date[revchange.index(min(revchange))])
        #print("max date" + maxdate)
        #print("min data" + mindate)
   
   # Printing Output to the terminal
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months : " + str(len(monthscount)))
    print ("Total : $ " + str(sum(sumtotal)))
    print("Average Change : $ " + str(averagecal) )
    print("Greatest Increase in Profits : " + maxdate + " ($" + str(greatincprofit) + ")")
    print("Greatest Decrease in Profits : " + mindate + " ($" + str(greatdecprofit) + ")")

# Printing the output to the txt file created.
# Export the results to text file
fileoutput = "C:/Users/Deepti/Python-Challenge/PyBank/pybank.txt"
with open(fileoutput, "w") as txt_file:
    sys.stdout = txt_file
    # Generate Output Summary
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months : " + str(len(monthscount)))
    print ("Total : $ " + str(sum(sumtotal)))
    print("Average Change : $ " + str(averagecal) )
    print("Greatest Increase in Profits : " + maxdate + " ($" + str(greatincprofit) + ")")
    print("Greatest Decrease in Profits : " + mindate + " ($" + str(greatdecprofit) + ")")
    
