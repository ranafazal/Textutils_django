from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def analyze(request):

    #GET THE TEXT
    djtext = request.POST.get('text', 'default')

    #CHECK BOX VALUES
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #CHECK WHICH CHECKBOX IS ON
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>,/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'REMOVE EXTRA SPACE', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = djtext
        count = 0
        for i in range(0, len(analyzed)):
            if analyzed[i] != ' ':
                count = count + 1
        params = {'purpose': 'CHARACTERS COUNT', 'analyzed_text': count}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please Select any operation and Try Again....!!")

    return render(request, 'analyze.html', params)
