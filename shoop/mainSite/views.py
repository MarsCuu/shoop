# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def index(request):
    template = get_template("index.html")
    html = template.render(locals())
    return HttpResponse(html)

#add item
def addItem(request):
    template = get_template("additem.html")
    html = template.render(locals())
    return HttpResponse(html)
@csrf_exempt
def item(request):
    print('item')
    template = get_template("index.html")
    if request.method=='POST':
        print("post")

        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        item_num = request.POST.get('item_num')
        item_des =request.POST.get('item_des')

        print("%s %s %s %s " % (item_name,item_price,item_num,item_des))
        myFile = request.FILES.get("item_pic")
        if myFile is not None:
            print("file")

    html = template.render(locals())

    return HttpResponse(html)