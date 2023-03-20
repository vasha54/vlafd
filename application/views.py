from django.shortcuts import render
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import View

from application.forms import LoginForm

from core.settings import NAME_APP, NAME_APP_SHORT

# Create your views here.

class ViewApp(View):
    template_name = 'page_build.html'
    
    def __init__(self, **kwargs):
        super(ViewApp,self).__init__(**kwargs)
        self.data={}
    
    def dispatch(self,request,*args,**kwargs):
        return super(ViewApp,self).dispatch(request,*args,**kwargs)
    
    def getDataInit(self,_request=None):
        dataInit = {
            'nameApp':NAME_APP,
            'nameAppShort':NAME_APP_SHORT,
        }
        
        if _request != None:
            if _request.user != None:
                if hasattr(_request.user, 'nameCompleted'):
                    dataInit['nameCompleted'] = _request.user.nameCompleted()
                if hasattr(_request.user, 'getRol'):
                    dataInit['rol'] = _request.user.getRol()
                if hasattr(_request.user, 'logo'):
                    dataInit['url_avatar'] = _request.user.logo.url
        
        return dataInit
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit()
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit()
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    

class LoginView(ViewApp):
    template_name = 'index.html'
    form_class = LoginForm
    
    def dispatch(self,*args,**kwargs):
        return super(LoginView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        self.data = self.getDataInit()
        form = self.form_class()
        self.data['form'] =form
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        self.data = self.getDataInit()
        
        form = self.form_class(request.POST or None)
        
        if form.is_valid() == True:
            usernameF = form.cleaned_data['username']
            passwordF = form.cleaned_data['password']
            
            user = authenticate(username=usernameF, password=passwordF)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/home')
                else:
                    self.data['messageError']='Usuario no esta activo. Contacte con los adminstradores.'
            else:
                self.data['messageError']='Credenciales incorrectas.'
            self.data['form'] = form 
            return render(request,self.template_name,self.data)
        else:
            self.data['form'] = form 
            return render(request,self.template_name,self.data)
        
class HomeView(ViewApp):
    template_name = 'home.html'
    form_class = None
    
    def dispatch(self,*args,**kwargs):
        return super(HomeView,self).dispatch(*args,**kwargs)
    
    def get(self,request, *args, **kwargs):
        self.data = self.getDataInit()
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        self.data = self.getDataInit()
        return render(request, self.template_name,self.data)
    
    