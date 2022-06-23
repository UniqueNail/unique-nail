Passos executados no terminal

1° Criar ambiente virtual ($python3 -m venv ./venv) dentro da pasta do projeto.


2° Carregar ambiente virtual ($venv/Scripts/activate) executar comando no VsCode.


3° Instalar Django ($ pip install django).


4° Iniciar projeto Django ($django-admin startproject uniquenaillandingpage .).


5° Configurar arquivo "settings.py":
	
	LANGUAGE_CODE = 'pt-br'
	TIME_ZONE = 'America/Sao_Paulo'


6° Para Rodar o servidor ($python manage.py runserver).



7° Criar aplicação ($python manage.py startapp landingPage).



8° Registrar aplicação criada no settings.py
	INSTALLED_APPS = [
	'landingPage'
	]


9° Criar arquivo "urls.py" na pasta do app e importar o app:
	from django.urls import path

	from . import views

	urlpatterns = [
    		path('', views.index, name='index')
	]


10° Registrar requisição no arquivo "views.py":
	def index(request):
    		return render('<h1>Unique Nail</h1>')



11° Incluir caminho no arquivo "urls.py" da pasta do projeto:
	from django.urls import path, include

	urlpatterns = [
    		path('', include('landingPage.urls')),
   		path('admin/', admin.site.urls),
	]


12° Criar pasta templates dentro da pasta do app para adicionar os htmls.


13° Especificar caminho da pasta templates no "settings.py":
	TEMPLATES = [
   		 {
        		'BACKEND': 'django.template.backends.django.DjangoTemplates',
        		'DIRS': [os.path.join(BASE_DIR, 'landingPage/templates')],
        		'APP_DIRS': True,
      			'OPTIONS': {
            			'context_processors': [
                			'django.template.context_processors.debug',
                			'django.template.context_processors.request',
                			'django.contrib.auth.context_processors.auth',
                			'django.contrib.messages.context_processors.messages',
          			],
       			},
   		 },
	]


14° Especificar caminho da pasta statics no "settings.py":
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'uniquenaillandingpage/static' )
]


15° Criar pasta static no diretório do projeto e colocar os arquivos css dentro.


16° Executar comando ($ python .\manage.py collectstatic) para o Django coletar os arquivos estáticos.


17° Colocar na primeira linha do "index.html" {% load static %} para o Django saiba que precisa executar arquivos estáticos neste documento.


18° Colocar {% static 'caminho/do/arquivo' %} em cada link de pastas e imagens e {% url 'caminho/da/página' %} para links.


19° Configurar caminho das outras páginas em "urls.py" e "views.py":
urls.py =>
		urlpatterns = [
    			path('', views.index, name='index'),
    			path('sobre', views.sobre, name='sobre')
		]
views.py =>
		def sobre(request):
    			return render(request,'sobre.html')


20° Criar arquivo "base.html" para evitar repetições de código no html:
Iniciar arquivo "base.html" com {% load static %}, acrescentar informações como o head com os links do css e js e colocar {% block content %} {% endblock %} para indicar onde vai o conteúdo.
Nas outras Páginas .html iniciar com {% extends 'base.html' %} {% load static %} {% block content %} e no final do conteúdo finalizar o bloco com {% endblock %}.


21° Criar pasta partials dentro de templates para adicionar blocos de códigos que irão se repetir em várias páginas como o menu e o rodapé:
Para isso basta criar um arquivo com o código e incluir {% include 'partials/footer.html' %} onde será usado.

