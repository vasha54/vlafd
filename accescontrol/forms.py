from django import forms
from accescontrol.models import UserDRPA
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AddUserAccesControlForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(AddUserAccesControlForm, self).__init__(*args, **kwargs)
        #self.fields['password1']=forms.CharField(widget=forms.PasswordInput)
        # self.fields['first_name'].widget.attrs['class'] ='form-control'
        # self.fields['last_name'].widget.attrs['class'] ='form-control'
        # self.fields['email'].widget.attrs['class'] ='form-control'
        # self.fields['username'].widget.attrs['class'] ='form-control'
        # self.fields['avatar'].widget.attrs['class'] ='form-control'
        # self.fields['numberPhone'].widget.attrs['class'] ='form-control'
        # self.fields['numberMobile'].widget.attrs['class'] ='form-control'
        # self.fields['password'].widget.attrs['class'] ='form-control'
        
    class Meta:
        model = UserDRPA
        fields = ['numberPhone','numberMobile','avatar','first_name','username','last_name','email','is_active']
        exclude = []
        
class UpdateUserAccesControlForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UpdateUserAccesControlForm, self).__init__(*args, **kwargs)
        #self.fields['password1']=forms.CharField(widget=forms.PasswordInput)
        # self.fields['first_name'].widget.attrs['class'] ='form-control'
        # self.fields['last_name'].widget.attrs['class'] ='form-control'
        # self.fields['email'].widget.attrs['class'] ='form-control'
        # self.fields['username'].widget.attrs['class'] ='form-control'
        # self.fields['avatar'].widget.attrs['class'] ='form-control'
        # self.fields['numberPhone'].widget.attrs['class'] ='form-control'
        # self.fields['numberMobile'].widget.attrs['class'] ='form-control'
        # self.fields['password'].widget.attrs['class'] ='form-control'
        
    class Meta:
        model = UserDRPA
        fields = ['first_name','username','last_name','numberPhone','numberMobile','avatar','email','is_active']#[]
        exclude = []#['password']
            

        
            

        

    