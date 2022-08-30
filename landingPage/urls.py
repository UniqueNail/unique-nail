from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    
    path('geis', views.geis, name='geis'),
    path('gelBase', views.gelBase, name='gelBase'),
    path('gelClear', views.gelClear, name='gelClear'),
    path('gelCover', views.gelCover, name='gelCover'),
    path('gelNude', views.gelNude, name='gelNude'),
    path('gelPink', views.gelPink, name='gelPink'),
    path('gelPinkNude', views.gelPinkNude, name='gelPinkNude'),
    path('gelWhite', views.gelWhite, name='gelWhite'),
    
    path('preparadores', views.preparadores, name='preparadores'),
    path('prep', views.prep, name='prep'),
    path('phBonder', views.phBonder, name='phBonder'),
    path('primerAcido', views.primerAcido, name='primerAcido'),
    path('primerAdesivador', views.primerAdesivador, name='primerAdesivador'),
    
    path('finalizadores', views.finalizadores, name='finalizadores'),
    path('cleanser', views.cleanser, name='cleanser'),
    path('topCoat', views.topCoat, name='topCoat'),
    path('oleodecuticula', views.oleodecuticula, name='oleodecuticula'),

    path('blindagem', views.blindagem, name='blindagem'),
    path('kitblindagem', views.kitblindagem, name='kitblindagem'),
    path('passo1', views.passo1, name='passo1'),
    path('passo2', views.passo2, name='passo2'),
    path('passo3', views.passo3, name='passo3'),
    path('passo5', views.passo5, name='passo5'),

    path('fibrafioafio', views.fibrafioafio, name='fibrafioafio'),    

    path('remov', views.remov, name='remov'),

    path('monomer', views.monomer, name='monomer'),

    path('brocas', views.brocas, name='brocas'),

]