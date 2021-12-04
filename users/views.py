from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from .forms import UserRegistForm, UserLoginForm, UserTokenForm, UserProjectForm
from django.contrib import messages
from .models import ExtraData
import gitlab
from gitbuster.forms import tokenProj

# Create your views here.
class Register(View):
    form = UserRegistForm
    template_name = 'register.html'
    
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})
        

class UserTokenView(View):
    form = UserTokenForm
    template_name = 'token.html'
    
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form(request.POST, instance=request.user.extradata)
        
        if form.is_valid():
            form.save()
            return redirect('token')  
        
        return render(request, self.template_name, {'form': form})
        
        
class UserProjView(View):
    form = UserProjectForm
    template_name = 'proj.html'
    
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form(request.POST, instance=request.user.extradata)
        if form.is_valid():
            form.save()
            return redirect('proj')     
    
        return render(request, self.template_name, {'form': form})  

class UserIssuesView(View):
    form = tokenProj
    template_name = 'issues.html'

    def get(self, request):
        return render(request, self.template_name)
    

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            projeto = form.cleaned_data['projeto']
            gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
            #print(gl.projects.get(projeto).name)
            return render(request, self.template_name, {'Issues Statics': gl.projects.get(projeto).issues.list()})
    
        return render(request, self.template_name)

class UserFilesView(View):
    form = tokenProj
    template_name = 'files.html'

    def get(self, request):
        return render(request, self.template_name)


class UserTeamView(View):
    form = tokenProj
    template_name = 'team.html'

    def get(self, request):
        return render(request, self.template_name)

class UserRepoView(View):
    form = tokenProj
    template_name = 'repo.html'

    def get(self, request):
        return render(request, self.template_name)

