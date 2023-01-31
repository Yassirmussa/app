from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
'''def hello(request):
    test = """<h1> Hello dear Customer</h1>"""
    return HttpResponse(test)'''

def about(request):
    #y=input("your name:")
    return render(request, 'about.html',{'name':'abra', 'last':'Juma'})

def tim(request):
    tempe = loader.get_template('time.html')
    contex= {
        "fruits":["banana","apple"]
    }
    return HttpResponse(tempe.render(contex,request))
 # function to add tow numbers
def add(request):
    val1 = eval(request.GET['num1'])
    val2 = eval(request.GET['num2'])
    resu = val1 + val2
    return render(request, 'result.html',{'result': resu})