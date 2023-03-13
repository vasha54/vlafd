from django.forms import BaseFormSet
from urllib.parse import urlparse
from django.conf import settings as djangosettings
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.http import HttpResponseRedirect, HttpResponse
from core import settings


from unidecode import unidecode
import qrcode
import re


def limitPagesShow(_min,_current,_max):
    limits=[]
    if _current - 2 >=_min:
        limits.append(_current - 2)
    else:
        limits.append(_min)
    
    limits.append(min(limits[0]+4,_max))
    
    if(limits[1]-limits[0]<4):
        i=limits[1]
        while limits[1]-limits[0]<4 and i <= _max:
            limits[1]=i
            i=i+1
            
        i=limits[0]
        while limits[1]-limits[0]<4 and i >= _min:
            limits[0]=i
            i=i-1
            
    return limits

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def canRemoveUserDRPA(_user):
    canRemove = True
    #TODO Falta definir bajo que criterios vamos a eliminar los usuarios
    return canRemove

def generateQRTouristResource(_request,_resource):
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4)
    domainWeb = _request.META['HTTP_HOST']
    protocol = 'http://'
    suffix ='/api/v1/touristresource/post/'
    strUIID = str(_resource.id)
    url = protocol+domainWeb+suffix+strUIID
    info = url
    print(url)
    # Agregamos la informacion
    qr.add_data(info)
    qr.make(fit=True)
    # Creamos una imagen para el objeto código QR
    imagen = qr.make_image()
    #Guardemos la imagen con la extension que queramos
    
    imagen.save('medias/qr_resources/'+strUIID+'.svg')
    

def generateSLUG(_name):
    slug = str(_name)
    slug = unidecode(slug) #Convertir texto Unicode en ASCII para quitar tildes y eñes
    slug = re.sub(r'[^\w\s]', '', slug) #Elimino todos los caracteres no alfanumericos
    slug = slug.lower() #Convetir a minusculas  
    slug = re.sub(r"\s+", '-',slug) #Sustituir un espacio o una secuencias de espacio por un guion
    return  slug

class RequeridFormSet(BaseFormSet):
    def __init__(self,*args,**kwargs):
        super(RequeridFormSet,self).__init__(*args,**kwargs)
        for form in self.forms:
            form.empty_permitted = False
            



def set_language(request,*args,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    
    if request.method == 'POST':
        language = 'es'
        next_url = '/admin/'
        if 'language' in request.POST.keys():
            language = request.POST['language']
        
        if 'next' in request.POST.keys():
            next_url = request.POST['next'] 
        
        
        for lang, _ in settings.LANGUAGES:
            translation.activate(lang)
            try:
                view = resolve(urlparse(request.META.get('HTTP_REFERER')).path)
            except Resolver404:
                view = None
                
            if view:
                break
        
        if view:
            translation.activate(language)
            #next_url= reverse(view.url_name,args=view.args,kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(djangosettings.LANGUAGE_COOKIE_NAME,language)
        else:
            response = HttpResponseRedirect(next_url)
        return response
    else:
        return HttpResponseRedirect(url)
           


