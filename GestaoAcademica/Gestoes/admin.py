from django.contrib import admin
from .models import Aluno, Professor,Curso,Aula

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Aula)

