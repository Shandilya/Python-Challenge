#import dependicies
import os
import csv
import sys
poll_data_csv = os.path.join("C:/Users/Deepti/washu/WASHSTL201806DATA4-Class-Repository-DATA/Week 3 - Python/Homework/PyPoll/Resources","election_data.csv")    
# open and read csv commands
with open(poll_data_csv, newline ="") as electiondatacsv:
    csvreader = csv.reader(electiondatacsv, delimiter = ',')
    csvheader = next(electiondatacsv) 
    totalvotes = 0
    candvotes = []
    candidates = []
    allcandname = []
    #candname = []
    # listofcands = []
    candvotes = 0
    percentvotes = []
    i=0
    kv = 0
    cv = 0
    lv= 0
    ov= 0
    for row in csvreader:
        totalvotes = totalvotes + 1 
        
        allcandname.append(row[2])
    # print total no of votes
    #print(totalvotes)
    # looping
    for i in range(0, totalvotes): 
        if allcandname[i] == "Khan":
          kv = kv +1
          perck=(kv/totalvotes *100)
          wname ="Khan"
        elif allcandname[i] == "Correy":
            cv = cv + 1
            percc=(cv/totalvotes * 100)
            wname="Correy"
        elif allcandname[i] == "Li":
            lv = lv + 1
            percl=(lv/totalvotes * 100)
            wname ="Li"
        elif allcandname[i] == "O'Tooley":
            ov = ov + 1
            perco=(ov/totalvotes * 100)
            wname ="O'Tooley"
        if (kv>cv):
            winner =kv
            wname ="Khan"
        elif (kv>lv):
            winner = lv
            wname ="Li"
        elif (lv>ov):
            winner =ov
            wname ="O'Tooley"
        else:
            wname="Correy"
            print("winner" + str(wname))

    print("Election Results")
    print("-------------------------------------")
    print("Total Votes  :" + str(totalvotes) )
    print("-------------------------------------")
    # two ways of printing output
    #print("Khan : " + str( perck ) + "%" + "( " + str(kv)+ " )")
    print(f" Khan : {perck:.3f} % ({kv})")
    print(f" Correy : {percc:.3f} % ({cv})")
    print(f" Li : {percl:.3f} % ({lv})")
    print(f" O'Tooley : {perco:.3f} % ({ov})")
    print("--------------------------------------")
    print(f" Winner : {wname}")
    print("--------------------------------------")
    
    # Below are samples to check results
    #print("Khan  Total " + str(kv))
    #print("Khan  % " + str(perck))
    #print("Correy  Total " + str(cv))
    #print("Correy  % " + str(percc))
    #print("Li  Total " + str(lv))
    #print("Li  % " + str(percl))
    #print("otooley  Total " + str(ov))
    #print("otoo  % " + str(perco))

    # Printing the output to the txt file created.
    # Export the results to text file

fileoutput = "C:/Users/Deepti/Python-Challenge/PyPoll/pypoll.txt"
with open(fileoutput, "w") as txt_file:
    sys.stdout = txt_file
    # Generate Output Summary
    print("Election Results")
    print("-------------------------------------")
    print("Total Votes  :" + str(totalvotes) )
    print("-------------------------------------")
    # two ways of printing output
    #print("Khan : " + str( perck ) + "%" + "( " + str(kv)+ " )")
    print(f" Khan : {perck:.3f} % ({kv})")
    print(f" Correy : {percc:.3f} % ({cv})")
    print(f" Li : {percl:.3f} % ({lv})")
    print(f" O'Tooley : {perco:.3f} % ({ov})")
    print("--------------------------------------")
    print(f" Winner : {wname}")
    print("--------------------------------------")