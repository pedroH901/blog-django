from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_posts, name='lista_de_posts'),
    path('post/<int:pk>/', views.detalhe_do_post, name='detalhe_do_post'),
]