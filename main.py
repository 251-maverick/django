import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
import django
django.setup()

from seatalloc.models import Program 
def populate():
    with open('data_u-2012.csv', newline='') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=';')
        #print (rankdata)
        rankdata=[]
        for r in read:
            rankdata.append(r)
    for r in rankdata:
       print (r)
       p=Program(institute=r[0],department=r[1],code1=r[2],openrank1=int(r[3]),closerank1=int(r[4]),openrank2=int(r[5]),closerank2=int(r[6]),openrank3=int(r[7]),closerank3=int(r[8]),openrank4=int(r[9]),closerank4=int(r[10]),openrank5=int(r[11]),closerank5=int(r[12]),openrank6=int(r[13]),closerank6=int(r[14]),openrank7=int(r[15]),closerank7=int(r[16]),openrank8=int(r[17]),closerank8=int(r[18]))
       p.save()
            
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
