from django import forms

class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)
   
   def __init__(self, *arg,**kwargs):
      super(LoginForm, self).__init__(*arg,**kwargs)
      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['password'].widget.attrs['class'] = 'form-control'
      self.persons = None
      
   def is_valid(self):
      valid = super(LoginForm,self).is_valid()
      return valid
         
         
         

