import json
from django.shortcuts import render
from django.http import HttpResponse

def MediaContent(request):
    i=5
    with open("website/resource/content.json") as f:
        result = json.loads(f.read())
    content = {}
    content ['contentUrl'] = result[i]["contentUrl"]
    content ['mediaType'] =  result[i]["mediaType"]
    content ['previewUrl'] = result[i]["previewUrl"]
    content ['title'] = result[i]["title"]
    if content ['mediaType'] == "video":
        content ['description'] = result[i]["description"]
    return render(request,"website/home.html",content)