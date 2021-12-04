from django.forms.fields import NullBooleanField
import gitlab
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from gitlab.v4.objects import projects
from ProjEs.forms import tokenProj
from django.shortcuts import redirect

#utilização de forms e view para obter o projeto

class Projeto(View):
    form = tokenProj
    template_name = 'funciona.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            projeto = form.cleaned_data['projeto']
            gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
            print(gl.projects.get(projeto).name)
            return HttpResponseRedirect('')
        
        return render(request, self.template_name, {'form': form})


