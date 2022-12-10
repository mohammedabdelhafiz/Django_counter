from django.shortcuts import render

def index(request):
    counter=1
    request.session['counter']+=counter
    return render(request,'basic.html')


# def delete():
#     del request.session['counter']