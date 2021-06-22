# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # return HttpResponse("hello aksh bhai")
#     return HttpResponse('<h1>Aksh Desai</h1>  <a href="https://www.youtube.com/" tabindex="1">Django CodeWthHarry</a>')
# def about(request):
#     return HttpResponse("About Harry bhai")

def index(request):
    # return HttpResponse('''Home <a href="/spaceremove">Go to space</a>''')
    # params = {'name':'harry', 'place':'Mars'}

    return render(request, 'index.html')

# def removepunc(request):
#     djtext = request.GET.get('text1', 'default1')
#     print(djtext)
#     dic = {'a':djtext}
#     return HttpResponse('reove punc ')
#
# def capfirst(request):
#     return HttpResponse('Capitalize first')
#
# def newlineremove(request):
#     return HttpResponse("Newline remove")
#
# def spaceremove(request):
#     return HttpResponse('Space Remover <a href="/admin">Go to Home</a>')
#
# def charcount(request):
#     return HttpResponse('Charcount')

def analyze(request):
    djtext = request.POST.get('text1', 'default')
    print(type(djtext))
    removepunc = request.POST.get('removepunc', 'off')
    print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(fullcaps)
    # analyzed = djtext
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        # return HttpResponse("removepunc")
        djtext = analyzed
        # return render(request, 'anaylize.html', params)
    if fullcaps == "on":
      analyzed = ""
      for i in djtext:
          analyzed = analyzed + i.upper()
      params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
      # return HttpResponse("removepunc")
      djtext = analyzed
      # return render(request, 'anaylize.html', params)
    if newlineremover == "on":
        analyzed = ""
        for i in djtext:
            if i != "\n" and i != '\r':
                analyzed += i

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # return HttpResponse("removepunc")
        djtext = analyzed
        # return render(request, 'anaylize.html', params)
    if extraspaceremover == 'on':
        analyzed = ""
        for index, i in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed += i
        params = {'purpose': 'Removed Extra space Remover', 'analyzed_text': analyzed}
        # return HttpResponse("removepunc")
        # djtext = analyzed
        # return render(request, 'anaylize.html', params)

    # else:
    #     return HttpResponse("Error")
    if (removepunc != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and fullcaps != 'on'):
        return HttpResponse("Error. Please selct the any operation and try again....")
    return render(request, 'anaylize.html', params)