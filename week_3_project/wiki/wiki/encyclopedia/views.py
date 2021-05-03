from django.shortcuts import render
from django import forms
from . import util
from django.urls import reverse
import random
import markdown

class NewTaskForm(forms.Form):
    search_entry = forms.CharField(label="Search:")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def wiki(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html", {
            "error": "Requested Page Not Found."
        })
    return render(request, "encyclopedia/wiki.html", {
        "entry": entry,
        "entry_body": markdown.markdown(util.get_entry(entry))
    })

def wiki_search(request):
    search_entry = request.POST.get("search_term")
    if util.get_entry(search_entry) == None:
        match_entries = []
        entries = util.list_entries()
        for item in entries:
            if search_entry.lower() in item.lower():
                match_entries.append(item) 
        if len(match_entries) < 1:
            return render(request, "encyclopedia/error.html", {
            "error": "No entry matches your search term. Feel free to create an entry!"
            })
        return render(request, "encyclopedia/search_match.html", {
            "match_entries": match_entries
        })        
    return render(request, "encyclopedia/wiki.html", {
        "entry": search_entry,
        "entry_body": markdown.markdown(util.get_entry(search_entry))
    })

def newpg(request):
    if request.method == "POST":
        title = request.POST.get("newpg_title")
        text = request.POST.get("newpg_text")
        entries = util.list_entries()
        for entry in entries:
            if title == entry:
                return render(request, "encyclopedia/error.html",{
                    "error": "Topic Page Already Exists."
                })
        util.save_entry(title, text)
        return wiki(request, title)
    else:
        return render(request, "encyclopedia/newpg.html")

def editpg(request):
    if request.method == "POST":
        util.save_entry(request.POST.get("entry"), request.POST.get("newpg_text"))
        return wiki(request, request.POST.get("entry"))
        

    else:
        entry = request.GET.get("entry_name")    
        return render(request, "encyclopedia/editpg.html",{
            "entry": entry,
            "entry_body": util.get_entry(entry)
        } )
def randompg(request):
    entries = util.list_entries()
    index = random.randint(0, len(entries)-1)
    return wiki(request, entries[index])