from django.shortcuts import render,get_object_or_404, redirect
from .models import Aluno, Professor, Curso, Aula
from django.contrib import messages 

def home(request):
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    return render(request, 'home.html', {'alunos': alunos, 'professores': professores})

#cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def edit_cursos(request, cursos_id):
    cursos = get_object_or_404(Curso, pk=cursos_id)
    professores = Professor.objects.all()  # Obtendo todos os professores

    if request.method == 'POST':
        cursos.nome = request.POST.get('nome')
        cursos.descricao = request.POST.get('descricao')
        cursos.carga_horaria = request.POST.get('carga_horaria')
        professor_id = request.POST.get('professor')
        
        # Verificando se o professor selecionado é válido
        if professor_id:
            professor = get_object_or_404(Professor, pk=professor_id)
            cursos.professor = professor
        else:
            cursos.professor = None  # Se nenhum professor for selecionado

        cursos.save()
        return redirect('home')
    else:
        return render(request, 'edit_cursos.html', {'cursos': cursos, 'professores': professores})
    
def delete_cursos(request, cursos_id):
    cursos = get_object_or_404(Curso, pk=cursos_id)
    
    if request.method == 'POST':
        cursos.delete()
        messages.success(request, 'curso deletado com sucesso.')
        return redirect('home')

    return render(request, 'delete_cursos.html', {'cursos': cursos})


def novo_cursos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        carga_horaria = request.POST.get('carga_horaria')
        professor_id = request.POST.get('professor')

        # Verifica se um professor foi selecionado
        if professor_id:
            professor = get_object_or_404(Professor, pk=professor_id)
        else:
            professor = None

        # Cria o objeto Curso no banco de dados
        Curso.objects.create(
            nome=nome,
            descricao=descricao,
            carga_horaria=carga_horaria,
            professor=professor
        )
        
        # Redireciona o usuário para a página inicial após a criação do curso
        return redirect('home') 

    # Se o método for GET, renderiza o formulário com os professores disponíveis
    professores = Professor.objects.all()  # Obtém todos os professores
    return render(request, 'novo_cursos.html', {'professores': professores})



#aulas
    
def aulas(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    aulas = Aula.objects.filter(curso=curso)
    return render(request, 'aulas.html', {'curso': curso, 'aulas': aulas})
#aluno
def home_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        genero = request.POST.get('genero')
        
        Aluno.objects.create(nome=nome, email=email, matricula=matricula,
                             endereco=endereco, telefone=telefone, genero=genero)
        return redirect('home_aluno')  # Redireciona de volta para a página de lista de alunos após a criação

    alunos = Aluno.objects.all().order_by('data_de_ingresso')
    return render(request, 'home_aluno.html', {'alunos': alunos})

def delete_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno deletado com sucesso.')
        return redirect('home')

    return render(request, 'delete_aluno.html', {'aluno': aluno})

def novo_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        data_de_ingresso = request.POST.get('data_de_ingresso')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        genero = request.POST.get('genero')

        Aluno.objects.create(
            nome=nome,
            email=email,
            matricula=matricula,
            data_de_ingresso=data_de_ingresso,
            endereco=endereco,
            telefone=telefone,
            genero=genero
        )

        return redirect('home') 

    return render(request, 'novo_aluno.html')

def edit_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.email = request.POST.get('email')
        aluno.matricula = request.POST.get('matricula')
        aluno.endereco = request.POST.get('endereco')
        aluno.telefone = request.POST.get('telefone')
        aluno.save()
        return redirect('home')
    else:
        return render(request, 'edit_aluno.html', {'aluno': aluno})

 #professores   
def home_professor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        formacao = request.POST.get('formacao')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        genero = request.POST.get('genero')
        
        Professor.objects.create(nome=nome, email=email, formacao=formacao,
                             endereco=endereco, telefone=telefone, genero=genero)
        return redirect('home_professor') 

    professores = Professor.objects.all().order_by('data_de_contratacao')
    return render(request, 'home_professor.html', {'professores': professores})

    
def delete_professor(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    
    if request.method == 'POST':
        professor.delete()
        messages.success(request, 'Professor deletado com sucesso.')
        return redirect('home')

    return render(request, 'delete_professor.html', {'professor': professor})

def edit_professor(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    if request.method == 'POST':
        professor.nome = request.POST.get('nome')
        professor.email = request.POST.get('email')
        professor.formacao = request.POST.get('formacao')
        professor.telefone = request.POST.get('telefone')
        professor.save()
        return redirect('home')

    return render(request, 'edit_professor.html', {'professor': professor})

def novo_professor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        formacao = request.POST.get('formacao')
        data_de_contratacao = request.POST.get('data_de_contratacao')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        genero = request.POST.get('genero')

        Professor.objects.create(
            nome=nome,
            email=email,
            formacao=formacao,
            data_de_contratacao=data_de_contratacao,
            endereco=endereco,
            telefone=telefone,
            genero=genero
        )

        return redirect('home')  # Redirecione para onde você deseja após a adição do aluno

    return render(request, 'novo_professor.html')

