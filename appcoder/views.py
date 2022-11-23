from django.http import HttpResponse
from appcoder.models import Curso, Profesor, Estudiante, Entregable
from appcoder.forms import ProfesorFormulario, EstudianteFormulario, CursoFormulario, UserRegisterForm
from django.shortcuts import render, redirect

# Dependencias para resolver apertura de archivos usando rutas relativas
from proyectocoder.settings import BASE_DIR
import os

#Class-Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#Protección por sesiones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "appcoder/index.html")


@login_required
def cursos(request):

    errores = ""

    #Validamos tipo de petición
    if request.method == 'POST':
        #Cargamos los datos en el formulario
        formulario = CursoFormulario(request.POST)

        #Validamos los datos
        if formulario.is_valid():
            #Recuperamos los datos sanitizados
            data = formulario.cleaned_data
            #Creamos el curso
            curso = Curso(nombre=data["nombre"], camada=data["camada"])
            #Guardamos el curso
            curso.save()
        else:
            #si el formulario no es valido, guardamos los errores para mostrarlos
            errores = formulario.errors

    #Recuperar todos los cursos de la BD
    cursos = Curso.objects.all() #Obtener todos los registros de ese modelo
    #Creamos el formulario vacío
    formulario = CursoFormulario()
    #Creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": errores}
    #Retornamos la respuesta
    return render(request, "appcoder/cursos.html", contexto)

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
    
        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = CursoFormulario(initial={"nombre":curso.nombre, "camada":curso.camada})
        return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": ""})


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")

def estudiantes(request):
    errores = ""

    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            estudiante = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiante.save()
        else:
            errores = formulario.errors
    
    estudiantes = Estudiante.objects.all()
    formulario = EstudianteFormulario()

    contexto = {"listado_estudiantes": estudiantes, "formulario": formulario, "errores": errores}
    return render(request, 'appcoder/estudiantes.html', contexto)

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)

    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            estudiante.nombre = data["nombre"]
            estudiante.apellido = data["apellido"]
            estudiante.email = data["email"]
            estudiante.save()
            return redirect("coder-estudiantes")
        else:
            return render(request, "appcoder/editar_estudiante.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = EstudianteFormulario(initial={"nombre":estudiante.nombre, "apellido":estudiante.apellido, "email":estudiante.email})
        return render(request, "appcoder/editar_estudiante.html", {"formulario": formulario, "errores": ""})

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()

    return redirect("coder-estudiantes")

def profesores(request):
    errores = ""

    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
        else:
            errores = formulario.errors
    
    profesores = Profesor.objects.all()
    formulario = ProfesorFormulario()

    contexto = {"listado_profesores": profesores, "formulario": formulario, "errores": errores}
    return render(request,"appcoder/profesores.html", contexto)

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            profesor.save()
            return redirect("coder-profesores")
        else:
            return render(request, "appcoder/editar_profesor.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "appcoder/editar_profesor.html", {"formulario": formulario, "errores": ""})

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    return redirect("coder-profesores")


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


def test(request):
    ruta = os.path.join(BASE_DIR, "appcoder/templates/appcoder/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)

    return HttpResponse(file.read())

#Vistas basadas en clases

class EntregablesList(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "appcoder/list_entregables.html"

class EntregablesDetail(DetailView):
    model = Entregable
    template_name = "appcoder/detail_entregable.html"

class EntregableCreate(CreateView): #Todas las clases aceptar el atributo template_name
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "appcoder/entregable_form.html"

class EntregableUpdate(UpdateView):
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["fecha_de_entrega", "entregado"]

class EntregableDelete(DeleteView):
    model = Entregable
    success_url = "/coder/entregables/"

#Login

def iniciar_sesion(request):

    errors = ""
    
    if request.method == 'POST':

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("coder-inicio")
            else:
                return render(request, "appcoder/login.html", {"form": formulario, "errors": "Credenciales Inválidas"})
        else:

            return render(request, "appcoder/login.html", {"form": formulario, "errors": errors})            


    formulario = AuthenticationForm()
    return render(request, "appcoder/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("coder-inicio")
        else:
            return render(request, "appcoder/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()
    return render(request, "appcoder/register.html", {"form": formulario})
