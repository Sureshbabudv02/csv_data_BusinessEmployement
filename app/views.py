from django.shortcuts import render

# Create your views here.
import csv
from app.models import *
from django.http import HttpResponse

def insert_data(self):
    with open('C:\\Users\\dspsu\\OneDrive\\Desktop\\Djangoprojects\\Msb1\\Scripts\\projectnd20csv\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            sr=i[0]
            p=i[1]
            dv=i[2]
            su=i[3]
            st=i[4]
            u=i[5]
            m=i[6]
            sub=i[7]
            g=i[8]
            srt_1=i[9]
            srt_2=i[10]
            srt_3=i[11]

            IO=BusinessEmployment(series_reference=sr,period=p,data_value=dv,suppressed=su,status=st,units=u,magnitude=m,subject=sub,group=g,Series_title_1=srt_1,Series_title_2=srt_2,Series_title_3=srt_3)
            IO.save()
    return HttpResponse('<h1>Inserted BusinessEmployment data SuccessFully</h1>')


