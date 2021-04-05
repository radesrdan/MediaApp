import json 
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator



def MediaContent(request,id):
    i=id
    with open("website/resource/content.json") as f:
        result = json.loads(f.read())
    content = {}
    content ['contentUrl'] = result[i]["contentUrl"]
    content ['mediaType'] =  result[i]["mediaType"]
    content ['previewUrl'] = result[i]["previewUrl"]
    content ['title'] = result[i]["title"]
    if content ['mediaType'] == "video":
        content ['description'] = result[i]["description"]
    return render(request,"website/detail.html",content)
    

def ListView(request):
    with open("website/resource/content.json") as f:
        result = json.loads(f.read())

    paginator = Paginator(result, 9)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)

    return render(request,"website/list.html",{'content':content})


