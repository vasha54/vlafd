from django.http import HttpResponseRedirect


from accescontrol.models import UserDRPA

from core import util


def changeStatusUsserAccesControl(request,usuario_id,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    try:
        user = UserDRPA.objects.get(username=usuario_id)
        user.is_active = False if user.is_active== True else True
        user.save()
    except UserDRPA.DoesNotExist:
        pass
    
    return HttpResponseRedirect(url)