from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def sobre(request):
    return render(request,'sobre.html')

def geis(request):
    return render(request,'geis.html')

def gel(request, gel_id):
    return render(request,'gel.html')

def gelBase(request):
    return render(request,'geis/gelBase.html')

def gelClear(request):
    return render(request,'geis/gelClear.html')

def gelCover(request):
    return render(request,'geis/gelCover.html')

def gelNude(request):
    return render(request,'geis/gelNude.html')

def gelPink(request):
    return render(request,'geis/gelPink.html')

def gelPinkNude(request):
    return render(request,'geis/gelPinkNude.html')

def gelWhite(request):
    return render(request,'geis/gelWhite.html')
