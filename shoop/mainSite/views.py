# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
import os
from  mainSite.models import items

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
    #print('item')
    #template = get_template("index.html")
    if request.method == 'GET':
        all_item = items.objects.all()
        print(all_item)
        return render(request,'items.html',{'itemList':all_item})



    if request.method=='POST':
        #print("post")

        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        item_num = request.POST.get('item_num')
        item_des =request.POST.get('item_des')

        print("%s %s %s %s " % (item_name,item_price,item_num,item_des))
        item_file = request.FILES.get("item_pic")
        if not item_file:
            return HttpResponse("no files for upload!")
        file_name = item_file.name.split('.')
        newFile = item_name+'.'+file_name[1]
        destination = open(os.path.join("static/uploads",newFile),'wb+')
        item_pic = "/static/uploads/%s" % (newFile)
        print(item_pic)
        for chunk in item_file.chunks():
            destination.write(chunk)
        destination.close()
       # return HttpResponse("upload over")
    new_item=items.objects.create(item_name=item_name,item_price=item_price,item_num=item_num,item_des=item_des,item_pic=item_pic)
    new_item.save()
    #print(destination)


    #


    return HttpResponseRedirect("/index",{"pic_src":item_pic})