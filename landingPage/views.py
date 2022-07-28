from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def sobre(request):
    return render(request,'sobre.html')


# Géis
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


#Higienizadores
def higienizadores(request):
    return render(request, 'higienizadores.html')

def higienizadores1(request):
    return render(request, 'higienizadores1.html')

def prep(request):
    return render(request, 'higienizadores/prep.html')

def cleanser(request):
    return render(request, 'higienizadores/cleanser.html')


#Blindagem
def blindagem(request):
    return render(request, 'blindagem.html')

def phBonder(request):
    return render(request, 'blindagem/phBonder.html')

def primerAdesivador(request):
    return render(request, 'blindagem/primerAdesivador.html')

def primerAcido(request):
    return render(request, 'blindagem/primerAcido.html')

def topCoat(request):
    return render(request, 'blindagem/topCoat.html')


#Removedor
def remov(request):
    return render(request, 'remov.html')

#Acrílico
def monomer(request):
    return render(request, 'monomer.html')

#Brocas
def brocas(request):
    return render(request, 'brocas.html')