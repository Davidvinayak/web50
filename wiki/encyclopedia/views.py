import markdown2
from random import choice
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request,title):
    data = util.get_entry(title)
    if data:
        html = markdown2.markdown(data)
        return render(request,"encyclopedia/entry.html",{
            "content":html,"title":title
        })
    else:
        return render(request,"encyclopedia/error.html")
def search(request):
    entries = util.list_entries()
    if request.method == 'POST':
        entry_search = request.POST['q']
        sub_entries = [entry for entry in entries if entry_search in entry]
        if entry_search in entries:
            return entry(request,entry_search)
        elif sub_entries is not None:
            return render(request,"encyclopedia/searchresults.html",{
                "results":sub_entries
            })
        else:
            return render(request,"encyclopedia/error.html",{"message":'The page you are trying to access doesn\'t exist'})

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        entries = util.list_entries()
        if title in entries:
             return render(request,"encyclopedia/error.html",{"message":'The page you are trying to create already exist'})
        util.save_entry(title,content)
    return render(request,"encyclopedia/newpage.html")
def edit(request,ptitle):
    data = util.get_entry(ptitle)
    return  render(request,"encyclopedia/edit.html",{
        "content":data,"title":ptitle
    })
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
    return entry(request,title)

def random(request):
    entries = util.list_entries()
    random_entry = choice(entries)
    return entry(request,random_entry)