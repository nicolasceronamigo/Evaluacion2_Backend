from django.urls import path
from . import views

urlpatterns = [
	path('', views.inicio, name='inicio'), 
	path('libros/', views.libros, name='libros'),
	path('crear_libro/', views.crear_libro, name='crear_libro'),
	path('editar_libro/<int:id>', views.editar_libro, name='editar_libro'),
	path('eliminar_libro/<int:id>', views.eliminar_libro, name='eliminar_libro'),
	path('consultar_libro/<int:id>', views.consultar_libro, name='consultar_libro'),
]