from django.contrib import admin
from django.urls import path
from Gestoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home_aluno/', views.home_aluno, name='home_aluno'),
    path('home_professor/', views.home_professor, name='home_professor'),
    path('cursos/', views.cursos, name='cursos'),
    path('edit/<int:cursos_id>/', views.edit_cursos, name='edit_cursos'),
    path('delete/<int:cursos_id>/', views.delete_cursos, name='delete_cursos'),
    path('novo/', views.novo_cursos, name='novo_cursos'),
    path('aulas/<int:curso_id>/', views.aulas, name='aulas'),
    path('novo_aluno/', views.novo_aluno, name='novo_aluno'),
    path('novo_professor/', views.novo_professor, name='novo_professor'),
    path('edit_aluno/<int:aluno_id>/', views.edit_aluno, name='edit_aluno'),
    path('delete_aluno/<int:aluno_id>/', views.delete_aluno, name='delete_aluno'),
    path('delete_professor/<int:professor_id>/', views.delete_professor, name='delete_professor'),
    path('edit_professor/<int:professor_id>/', views.edit_professor, name='edit_professor'),
]