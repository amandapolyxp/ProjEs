from django.shortcuts import render
from django.forms.fields import NullBooleanField
import gitlab
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from gitlab.v4.objects import projects
from gitbuster.forms import tokenProj
# Create your views here.
    
class Projeto(View):
    form = tokenProj
    template = 'funciona.html'
    nomeDele = None
    
    def get(self, request):
        form = self.form()
        nomeDele = self.nomeDele
        return render(request, self.template, {'form': form, 'nome': nomeDele})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            projeto = form.cleaned_data['projeto']
            gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
            self.nomeDele = gl.projects.get(projeto).name
            return render(request, self.template, {'form': form, 'nome': self.nomeDele})
        
        return render(request, self.template, {'form': form, 'nome': self.nomeDele})


    
