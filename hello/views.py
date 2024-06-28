from django.http import HttpResponse

def home(request):
    return HttpResponse("Nome: Murilo Ferri Schirmer | Disciplina:Cloud Computing & Site Reliability Engineering")