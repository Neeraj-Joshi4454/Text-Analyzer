from django.http import HttpResponse, response
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    inputstr = request.GET.get('inputText','default')
    removePunc = request.GET.get('removePunc','off')
    upperCase = request.GET.get('upperCase','off')
    lengthOfPara = request.GET.get('lengthOfPara','off')
    removeNewLine = request.GET.get('removeNewLine','off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover','off')
    analyzed = ""


    if(removePunc == 'on'):

        Punctuations = '''!()[]{}-:;'"\/,.<>?@#$%^&*_~'''
        for i in inputstr:
            if i not in Punctuations:
                analyzed = analyzed + i
        params = {'purpose': 'Remove Punctuations', 'analyzed_text':analyzed}

        return render(request,'analyze.html',params)
    elif(upperCase == 'on'):
        analyzed = inputstr.upper()
        params = {'purpose': 'Conver Into Uppercase', 'analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    elif(lengthOfPara == 'on'):
        analyzed = len(inputstr)
        params = {'purpose': 'Check the length of the Paragraph', 'analyzed_text':'Number of charcter in your text is'+analyzed}
        return render(request,'analyze.html',params)
    
    elif(removeNewLine == 'on'):
        analyzed = ""
        for char in inputstr:
            if(char !='\n'):
                analyzed = analyzed + char

        params = {'purpose': 'Remove New Line', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(extraSpaceRemover == 'on'):
        analyzed = ""
        for index, char in enumerate(inputstr):
            if not(inputstr[index]== " " and inputstr[index+1] == " "):
                analyzed = analyzed + char
        
        params = {'purpose': 'Remove extra spaces', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Please Select The Option First")


