
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')


def eggs(request):
    textarea=request.GET['textarea']
    wordlist=textarea.split()
    worddictionary = {}
    for words in wordlist:
        if words in worddictionary:
            worddictionary[words]+=1
        else:
            worddictionary[words]=1
    #textarea1=request.GET['textarea1']
    return render(request,'eggs.html',{'textarea':textarea,'worddictionary':worddictionary})
