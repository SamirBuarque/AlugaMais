from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class sign_up_form(UserCreationForm):
    email = forms.EmailField(label="", max_length="50",
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) #attrs = css que esse widget vai receber.
    
    first_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome'})) 
    
    last_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Último nome'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2') #django espera por esses campos: username, password1 e password2

    """ 
    *args é um parâmetro obrigatório na função, apenas um.

    **kwargs são parâmetros opcionais na função, que podem ser ou não declarados.

    args e kwargs são convenções e podem ter qualquer outro nome.
    """
    def __init__(self, *args, **kwargs):
        super(sign_up_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

        



    