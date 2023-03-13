from django.contrib import admin
from django.db.models import Value, Count
from django.db.models.functions import Concat
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.utils.html import format_html
from accescontrol.models import UserDRPA,Role
from accescontrol.forms import AddUserAccesControlForm, UpdateUserAccesControlForm
from core.settings import ITEM_PER_PAGE
# Register your models here.

class RoleAdmin(GroupAdmin):
    list_display = ['name','countUsers']
    list_per_page = ITEM_PER_PAGE
    search_fields = ['name__contains']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _countUsers=Count('user')
        )

        return queryset
    
    def countUsers(self, _obj):
        return _obj._countUsers
    countUsers.short_description= 'Cantidad de usuarios'
    countUsers.admin_order_field = "_countUsers"

class UserDRPAAdmin(UserAdmin):
    list_display  = ('photo','nameCompleted','email','active','numberPhone','numberMobile')
    search_fields = ['username__contains','first_name__contains','last_name__contains','email__contains','numberPhone__contains','numberMobile__contains']
    list_filter = ['is_active']
    filter_horizontal = ('groups', 'user_permissions',) 
    list_per_page = ITEM_PER_PAGE
    
    
    add_form = AddUserAccesControlForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}
    
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email', 'numberPhone','numberMobile','avatar','password','is_superuser', 'is_staff', 'is_active', 'groups'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1','password2','email', 'numberPhone','numberMobile','avatar','is_superuser', 'is_staff', 'is_active', 'groups'),
        }),
        
    )
    
    @admin.display(ordering=Concat('last_name', Value(' '), 'first_name'))
    def nameCompleted(self,_obj):
        return format_html('<a href="/admin/accescontrol/userdrpa/{}/change" >{}</a>',_obj.pk,_obj.nameCompleted()) 
    nameCompleted.short_description = "Nombre y apellidos"
    
    @admin.display(ordering='is_active')
    def active(self,_obj):
        if _obj.is_active == True:
            return format_html('<a href="/accescontrol/changestatus/{}"> <i class="nav-icon fas fa-toggle-on" title="Habilitada"></i></a>',_obj.username)
        else:
            return format_html('<a href="/accescontrol/changestatus/{}"> <i class="nav-icon fas fa-toggle-off" title="Deshabilitada"></i></a>',_obj.username)
    active.short_description = "Estado de la cuenta"
    
    def photo(self,_obj):
        if _obj.avatar !=None :
            return format_html('<img src="{}" width="24px" height="24px">',_obj.avatar.url)
    photo.short_description = ""

admin.site.register(UserDRPA,UserDRPAAdmin)
admin.site.register(Role,RoleAdmin)
