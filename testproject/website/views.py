from django.db import connection
from django.shortcuts import render, render_to_response, get_object_or_404
import requests
# Create your views here.
from website.models import Staff, Class


def index(request):
    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')


def test(request):
    return render_to_response('test.html')


def classes(request):
    #page = requests.get("https://www.google.com/calendar/embed?showTitle=0&amp;showNav=0&amp;showDate=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;mode=WEEK&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=1kep159mvkfr73ubkk8qhcrie8%40group.calendar.google.com&amp;color=%23875509&amp;ctz=America%2FChicago")
    return render_to_response('classes.html')
    #return render(request, 'classes.html', {'calendar_html': page.text})



def staff(request):
    #return render_to_response('staff.html')
    members = Staff.objects.all().order_by('sort_order')
    return render(request, 'staff.html', {'staff': members})


def staffdetail(request, staff_name):
    member = get_object_or_404(Staff, url=staff_name)
    return render(request,'staffdetail.html',{'member': member})


def class_detail(request, class_name):
    c = get_object_or_404(Class, url=class_name)
    return render(request,'class_detail.html', {'klass': c})


def sql(request):
    s, x, headers = '', '', []
    if request.method == 'POST':
        s = request.POST['sql']
        cursor = connection.cursor()
        cursor.execute(s)
        headers = cursor.description
        x = cursor.fetchall()

    return render(request, 'sql.html', {'sql': s, 'results': x, 'headers': headers})


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def children(request):
    return render_to_response('children.html')