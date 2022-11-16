from django.http import HttpResponse
from appcoder.models import Curso, Profesor, Estudiante
from appcoder.forms import ProfesorFormulario, EstudianteFormulario
from django.shortcuts import render

# Dependencias para resolver apertura de archivos usando rutas relativas
from proyectocoder.settings import BASE_DIR
import os

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):

    return render(request, "appcoder/cursos.html")
    

def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, "appcoder/curso_formulario.html")


def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")


def creacion_estudiantes(request):

    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = formulario.cleaned_data

            estudiante = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiante.save()

    formulario = EstudianteFormulario()
    return render(request, "appcoder/estudiantes_formulario.html", {"formulario": formulario})


def profesores(request):
    return render(request, "appcoder/profesores.html")



def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save()


    formulario = ProfesorFormulario()    
    contexto = {"formulario": formulario}
    return render(request, "appcoder/profesores_formularios.html", contexto)







def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")

def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder/resultados_busquedas_cursos.html", {"cursos": cursos})





def buscar_alumnos(request):

    if request.GET:
        nombre_alumno = request.GET.get("nombre_alumno", "")
        if nombre_alumno == "":
            estudiantes = []
        else:
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre_alumno)
        return render(request, "appcoder/busqueda_estudiantes.html", {"listado_alumnos": estudiantes})

    return render(request, "appcoder/busqueda_estudiantes.html", {"listado_alumnos": []})




def entregables(request):
    return render(request, "appcoder/entregables.html")


# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     # Respuesta casera
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
#     cadena_respuesta += "</ul>"

#     return HttpResponse(cadena_respuesta)

def test(request):
    ruta = os.path.join(BASE_DIR, "appcoder/templates/appcoder/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)

    return HttpResponse(file.read())