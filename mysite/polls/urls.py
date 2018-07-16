from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('form',views.form, name='form'),
	path('addchoice', views.addchoice, name= 'addchoice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)