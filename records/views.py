from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext


from models import Record
import datetime

def import_csv(request):
    ret={}
    import csv
    reader = csv.reader(open('programming-sample.tab', 'rb'))
    for index,row in enumerate(reader):
        if index >0:
            m=int(row[1])
            d=int(row[2])
            if m>12:
                my_date= datetime.date(2012,m-12,d)
            else:
                my_date= datetime.date(2011,m,d)
                
            r=Record(body=row[3],title=row[0], date=my_date)
            r.save()
        #~ print 'Month: ' + row[1]
        #~ print 'Day: ' + row[2]
    
    return render_to_response('records/importing.html', ret)

def recovery_list(request, year, month, day):
    ret={}
    my_date= datetime.date(int(year),int(month),int(day))
    object_list=Record.objects.filter(date=my_date)
    for o in object_list:
        a=o.body.split(' ')
        print len(a)
        o.lar=len(a)
    return render_to_response('records/list_by_date.html', locals())

def count_words(request):
    object_list=Record.objects.all()
    total_number=0
    for o in object_list:
        a=o.body.split(' ')
        total_number+=len(a)
    return render_to_response('records/count_words.html', locals())
