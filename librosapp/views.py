from django.shortcuts import render, redirect
from .models import Libro


# Create your views here.
def inicio(request):
    return render(request, "librosapp/inicio.html")

def libros(request):
    libros = Libro.objects.all()
    return render(request, "librosapp/libros.html", {'libros': libros})

def crear_libro(request):
    if request.method == "POST":
        titulo = request.POST["titulo"].strip()
        autor = request.POST["autor"].strip()
        editorial = request.POST["editorial"].strip()
        errores = []
        if not titulo:
            errores.append("El título no puede estar vacío.")
        if not autor:
            errores.append("El autor no puede estar vacío.")
        if not editorial:
            errores.append("La editorial no puede estar vacía.")
        if not errores:
            Libro.objects.create(titulo=titulo, autor=autor, editorial=editorial)
            return redirect("libros")
        return render(request, "librosapp/crear_libro.html", {
            "errores": errores,
            "titulo": titulo,
            "autor": autor,
            "editorial": editorial
        })
    return render(request, "librosapp/crear_libro.html")

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        libro.titulo = request.POST["titulo"].strip()
        libro.autor = request.POST["autor"].strip()
        libro.editorial = request.POST["editorial"].strip()
        libro.estado = request.POST["estado"]
        errores = []
        if not libro.titulo:
            errores.append("El título no puede estar vacío.")
        if not libro.autor:
            errores.append("El autor no puede estar vacío.")
        if not libro.editorial:
            errores.append("La editorial no puede estar vacía.")
        if not libro.estado:
            errores.append("El estado no puede estar vacío.")
        if not errores:
            libro.save()
            return redirect("libros")    
        return render(request, "librosapp/editar_libro.html", {
                    "errores": errores,
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "editorial": libro.editorial,
                    "estado": libro.estado
                })
    return render(request, "librosapp/editar_libro.html", {
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "editorial": libro.editorial,
                    "estado": libro.estado
                })

def eliminar_libro(request, id):
    pass