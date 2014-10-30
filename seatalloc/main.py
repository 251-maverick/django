import csv

##do v need to read xlsx file
with open('closingRankData-2012.csv', newline='') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile, delimiter=',')
    #print (rankdata)
    rankdata=[]
    for r in read:
        rankdata.append(r)
    #print (rankdata)
            
def seatfinder(rank, cat):
        inclusive = []
        eligible = []
        #rankdata.open('closingRankData-2012.csv','rb')
        for row in rankdata:
            if row[cat] > rank:
                inclusive.append(row[0])
            elif rank < row[cat+1]:
                eligible.append(row[0])
        
        if len(inclusive)==0:
            return "-1"
        #print ('inclusive', inclusive)
        #print ('eligible', eligible)
        ##sorting by insti
        ch = inclusive[0][0]
        insti = []
        main = []
        for prog in inclusive:
            if prog[0]==ch:
                insti.append(prog)
            else:
                main.append(insti)
                insti = []
                ch=prog[0]
        # for item in main:
#             print(item)
        
            
        insti = []
        main2 = []
        for prog in inclusive:
            if prog[0]==ch:
                insti.append(prog)
            else:
                main2.append(insti)
                insti = []
                ch=prog[0]
                
        # for item in main2:
#             print(item)
        return (main,main2)
        

                                
def editpref(pref):                             #pref is a list of candid, pref1 pref2..
    with open('mydata.csv', 'a', newline='') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=',')
        mywriter.writerow(pref)
        
def info(candidate):        ##think of a better way
    with open('mydata.csv', newline='') as csvfile:
        prefdata = csv.reader(csvfile, delimiter=',')
        #for i in prefdata:        
        for row in prefdata:
            print (row[0])
            if row[0]==[candidate][0]:
                print (row)
                return row
        return -1
    
#prog name->code
    
pref =[]
pref.append(3)
pref.append(4)       
#x=input()            
editpref(pref)
#info(x)                
seatfinder("3100",3)

#def progcode(codemap):
    

# with open('prog.csv', newline='') as read:
#     next(read)
#     data = csv.reader(read, delimiter=',')
#     #print (rankdata)
#     progdata =[]
#     for r in data:
#         progdata[r[0]]=[r[1],r[2]]
    

def writeprog():
    with open('data.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',)
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])