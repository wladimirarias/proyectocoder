from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EstudianteFormulario(forms.Form):
    
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
    email = forms.EmailField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)
    camada = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1","password2"]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput, required=False)
   
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]

        # ? La siguiente linea elimina cualquier mensaje de ayuda en los campos
        # ?help_texts = { k: "" for k in fields }
        help_texts = { "email": "Indica un correo electronico que uses habitualmente", "first_name": "", "last_name": "", "password1": ""}

class AvatarForm(forms.Form):
    imagen = forms.ImageField()