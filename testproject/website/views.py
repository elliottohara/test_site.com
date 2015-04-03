from django.db import connection
from django.shortcuts import render, render_to_response, get_object_or_404
# Create your views here.
from django.views.generic import DetailView
import requests
from website.models import Staff, Class, SimplePage, FontPageSlide


def index(request):
    slides = FontPageSlide.objects.all()
    return render(request, 'index.html', {'slides': slides})


def classes(request):
    return render_to_response('classes.html')


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


def generic(request, view_name):
    return render_to_response("%s.html" % view_name)


def media(request):
    return render_to_response('media.html')


def account(request):
    return render_to_response('account.html')


def merchandise(request):
    return render_to_response('merchandise.html')


class SimplePageView(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(SimplePage, url=self.args[0])