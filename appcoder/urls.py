from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("estudiantes/actualizar/<id>/", editar_estudiante, name="coder-estudiantes-editar"),
    path("estudiantes/borrar/<id>/", eliminar_estudiante, name="coder-estudiantes-borrar"),
    path("estudiantes/buscar/", buscar_alumnos, name="coder-estudiantes-buscar"),
    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/actualizar/<id>/", editar_profesor, name="coder-profesores-editar"),
    path("profesores/borrar/<id>/", eliminar_profesor, name="coder-profesores-eliminar"),
    path("profesores/crear/", creacion_profesores, name="coder-profesores-crear"),
    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/borrar/<id>/", eliminar_curso, name="coder-cursos-borrar"),
    path("cursos/actualizar/<id>/", editar_curso, name="coder-cursos-editar"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultados_busqueda_cursos, name="coder-cursos-buscar-resultados"),

    #Levantar por vistas basadas en clases
    path("entregables/", EntregablesList.as_view(), name="coder-entregables"),
    path("entregables/detalle/<pk>/", EntregablesDetail.as_view(), name="coder-entregables-detail"),
    path("entregables/crear/", EntregableCreate.as_view(), name="coder-entregables-create"),
    path("entregables/actualizar/<pk>/", EntregableUpdate.as_view(), name="coder-entregables-update"),
    path("entregables/borrar/<pk>/", EntregableDelete.as_view(), name="coder-entregables-delete"),

    path("test/", test)
]