from django.shortcuts import render
import markdown
from . import util  
import random

def convertToHTML(title):
    content = util.get_entry(title)
    md = markdown.Markdown()
    if content != None:
        return md.convert(content)
    else:
        return None

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request , title):
    htmlContent = convertToHTML(title)
    if htmlContent != None:
        return render(request , "encyclopedia/showEntry.html", {
            "content": htmlContent,
            "title" : title
        })
    else:
        return render(request , "encyclopedia/err.html", {
            "ERR": "This entry does not exist!"
        })

def search(request):
    if request.method == "POST":
        enteredSearch = request.POST["q"]
        htmlContent = convertToHTML(enteredSearch)
        if htmlContent != None:  
            return render(request , "encyclopedia/showEntry.html", {
                "content": htmlContent ,
                "title": enteredSearch
            })
        else:
            list = []
            for entry in util.list_entries():
                if enteredSearch.lower() in entry.lower():
                    list.append(entry)
            return render(request, "encyclopedia/search.html", {
                "list": list
            })

        
def NewPage(request):
    if request.method == "POST":
        title = request.POST["title"]
        enteredTitle = util.get_entry(title)
        content = request.POST["content"]
        if enteredTitle == None:
            util.save_entry(title,content)
            htmlContent = convertToHTML(title)
            return render(request, "encyclopedia/showEntry.html",{
                "title": title,
                "content": htmlContent
            })
        else:
            return render(request, "encyclopedia/err.html", {
                "ERR": "Entered page already EXISTS!"
            })
    elif request.method == "GET":
        return render(request, "encyclopedia/newPage.html")

def edit(request):
    if request.method == "POST":       
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": content
        })
    
def saveEdited(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        htmlContent = convertToHTML(title)
        return render(request, "encyclopedia/showEntry.html",{
            "title": title,
            "content": htmlContent
        })

def randomPage(requset):
    list = util.list_entries()
    randomTitle = random.choice(list)
    htmlContent = convertToHTML(randomTitle)
    return render(requset, "encyclopedia/showEntry.html",{
            "title": randomTitle,
            "content": htmlContent
        })
