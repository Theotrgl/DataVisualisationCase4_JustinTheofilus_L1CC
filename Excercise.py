import csv
import statistics as st
import matplotlib.pyplot as plt

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    
    wr = open("newActivityKuDataSet.csv","w")
    wr.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2]))
    wr.write("\n")
    
    n=0
    for row in reader:
        if(row[0] == 'NA'):
            row[0] = 0
            n+=1
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2]))
        wr.write("\n")
     
    wr.close()

filename="newActivityKuDataSet.csv"
with open(filename) as f:
    reader=csv.reader(f)
    headerRow=next(reader)

    print(headerRow)

    wr = open("newActivity.csv","w")
    wr.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2])+","+"Type of Day")
    wr.write("\n")

    listofWeekendDatesOct=["06","07","13","14","20","21","27","28"]
    listofWeekendDatesNov=["03","04","10","11","17","18","24","25"]
    wd=0
    we=0
    
    for row in reader:
        date_split=row[1].split(sep="-")
        date=[]
        date.append(date_split[2])
        month=[]
        month.append(date_split[1])
        ##print(date)
        ##print(month)
        for i in date:
            for m in month:
                if i in listofWeekendDatesOct and m=="10":
                    wr.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+"Weekend")
                    wr.write("\n")
                    we+=1
                elif i in listofWeekendDatesNov and m=="11":
                    wr.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+"Weekend")
                    wr.write("\n")
                    we+=1
                else:
                    wr.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+"Weekday")
                    wr.write("\n")
                    wd+=1
                
    wr.close()
    print(wd, we)

newFile = 'newActivity.csv'
with open(newFile) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    dictDateWD = {}   #stores number of steps per day
    dictIntervalWD = {} #stores number of steps per 5 min interval
    dictDateWE ={}
    dictIntervalWE={}
    
    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])
        dayType= row[3]
        if dayType== "Weekday":
                  
            dictDateWD.setdefault(str(date),[])
            dictDateWD[str(date)].append(int(steps))
                
            dictIntervalWD.setdefault(interval,[])
            dictIntervalWD[interval].append(int(steps))
        if dayType=="Weekend":

            dictDateWE.setdefault(str(date),[])
            dictDateWE[str(date)].append(int(steps))
                
            dictIntervalWE.setdefault(interval,[])
            dictIntervalWE[interval].append(int(steps))

    listDateWD = []
    listTotalWD = []
    listDateWE = []
    listTotalWE = []


    for i in dictDateWD.keys():
        listDateWD.append(i)
        listTotalWD.append(sum(dictDateWD.get(i)))
    for i in dictDateWE.keys():
        listDateWE.append(i)
        listTotalWE.append(sum(dictDateWE.get(i)))
    
    print (listTotalWD)
    print(listTotalWE)

    listAvePerIntervalWD = []
    for i in dictIntervalWD.keys():
        listAvePerIntervalWD.append(st.mean(dictIntervalWD.get(i)))
    
    fig = plt.figure(dpi=80,figsize=(20,6))
    plt.plot(list(dictIntervalWD.keys()),listAvePerIntervalWD,c='blue')
    plt.title("Average Daily Activity For Every Weekday")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken (Weekday)")
    fig.autofmt_xdate()
    plt.savefig('ActivityWD.svg')
    plt.show()

    listAvePerIntervalWE=[]
    for i in dictIntervalWE.keys():
        listAvePerIntervalWE.append(st.mean(dictIntervalWE.get(i)))
    fig = plt.figure(dpi=80,figsize=(20,6))
    plt.plot(list(dictIntervalWE.keys()),listAvePerIntervalWE,c='red')
    plt.title("Average Daily Activity For Every Weekend")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken (Weekend)")
    fig.autofmt_xdate()
    plt.savefig('ActivityWE.svg')
    plt.show()



            

